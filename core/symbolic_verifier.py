import time
import ast
from typing import Dict, Any, Tuple, Optional
import z3
from core.dsl_schema import (
    ContractAST,
    ContractVariable,
    VariableType,
    VerificationResultStatus,
    InvariantCheckResult,
    FullVerificationReport
)

class Z3ExpressionBuilder:
    """Safely converts Python-like AST arithmetic and boolean expressions into Z3 formulas."""
    
    def __init__(self, z3_vars: Dict[str, Any]):
        self.z3_vars = z3_vars

    def parse_expr(self, expr_str: str) -> Any:
        expr_str = expr_str.strip()
        if not expr_str or expr_str == "True":
            return z3.BoolVal(True)
        if expr_str == "False":
            return z3.BoolVal(False)

        # Handle simple implication 'A => B'
        if "=>" in expr_str:
            parts = expr_str.split("=>", 1)
            left = self.parse_expr(parts[0])
            right = self.parse_expr(parts[1])
            return z3.Implies(left, right)

        try:
            tree = ast.parse(expr_str, mode='eval')
            return self._eval_ast(tree.body)
        except Exception as e:
            raise ValueError(f"Failed to parse expression '{expr_str}': {str(e)}")

    def _eval_ast(self, node: ast.AST) -> Any:
        if isinstance(node, ast.Name):
            var_name = node.id
            if var_name in self.z3_vars:
                return self.z3_vars[var_name]
            elif var_name.lower() == "true":
                return z3.BoolVal(True)
            elif var_name.lower() == "false":
                return z3.BoolVal(False)
            else:
                # Create a default Real variable on the fly if missing
                v = z3.Real(var_name)
                self.z3_vars[var_name] = v
                return v

        elif isinstance(node, ast.Constant):
            if isinstance(node.value, bool):
                return z3.BoolVal(node.value)
            elif isinstance(node.value, (int, float)):
                return z3.RealVal(node.value)
            elif isinstance(node.value, str):
                return node.value
            return node.value

        elif isinstance(node, ast.UnaryOp):
            operand = self._eval_ast(node.operand)
            if isinstance(node.op, ast.Not):
                return z3.Not(operand)
            elif isinstance(node.op, ast.USub):
                return -operand
            elif isinstance(node.op, ast.UAdd):
                return operand

        elif isinstance(node, ast.BinOp):
            left = self._eval_ast(node.left)
            right = self._eval_ast(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            elif isinstance(node.op, ast.Sub):
                return left - right
            elif isinstance(node.op, ast.Mult):
                return left * right
            elif isinstance(node.op, ast.Div):
                return left / right

        elif isinstance(node, ast.Compare):
            left = self._eval_ast(node.left)
            comparisons = []
            cur_left = left
            for op, comparator in zip(node.ops, node.comparators):
                right = self._eval_ast(comparator)
                if isinstance(op, ast.Lt):
                    cmp = (cur_left < right)
                elif isinstance(op, ast.LtE):
                    cmp = (cur_left <= right)
                elif isinstance(op, ast.Gt):
                    cmp = (cur_left > right)
                elif isinstance(op, ast.GtE):
                    cmp = (cur_left >= right)
                elif isinstance(op, ast.Eq):
                    cmp = (cur_left == right)
                elif isinstance(op, ast.NotEq):
                    cmp = (cur_left != right)
                else:
                    raise NotImplementedError(f"Unsupported comparison operator: {type(op)}")
                comparisons.append(cmp)
                cur_left = right
            if len(comparisons) == 1:
                return comparisons[0]
            return z3.And(*comparisons)

        elif isinstance(node, ast.BoolOp):
            values = [self._eval_ast(v) for v in node.values]
            if isinstance(node.op, ast.And):
                return z3.And(*values)
            elif isinstance(node.op, ast.Or):
                return z3.Or(*values)

        raise NotImplementedError(f"Unsupported AST node type: {type(node)}")


class SymbolicContractVerifier:
    """Symbolic Verification Engine using Z3 SMT Solver."""

    def __init__(self, timeout_ms: int = 5000):
        self.timeout_ms = timeout_ms

    def _setup_variables(self, variables: list) -> Dict[str, Any]:
        z3_vars = {}
        for var in variables:
            if var.var_type == VariableType.REAL:
                z3_vars[var.name] = z3.Real(var.name)
            elif var.var_type == VariableType.INTEGER:
                z3_vars[var.name] = z3.Int(var.name)
            elif var.var_type == VariableType.BOOLEAN:
                z3_vars[var.name] = z3.Bool(var.name)
            else:
                z3_vars[var.name] = z3.Real(var.name)
        return z3_vars

    def verify_contract(self, ast_model: ContractAST) -> FullVerificationReport:
        z3_vars = self._setup_variables(ast_model.variables)
        expr_builder = Z3ExpressionBuilder(z3_vars)

        # 1. Translate all valid clauses into Z3 assertions
        clause_formulas = []
        for clause in ast_model.clauses:
            try:
                cond = expr_builder.parse_expr(clause.condition or "True")
                body = expr_builder.parse_expr(clause.formula)
                # Formally: Condition => Formula
                clause_formulas.append(z3.Implies(cond, body))
            except Exception as e:
                print(f"[Verifier Warning] Could not parse clause {clause.clause_id}: {e}")

        results = []
        violations_count = 0

        # 2. Check each Invariant
        for inv in ast_model.invariants:
            start_time = time.perf_counter()
            solver = z3.Solver()
            solver.set("timeout", self.timeout_ms)

            # Realistic domain bounds (Financial variables should be non-negative)
            for name, v in z3_vars.items():
                if isinstance(v, (z3.ArithRef,)):
                    # E.g., debt, days, EBITDA generally >= 0
                    solver.add(v >= 0)

            # Add all contract clauses as baseline system axioms
            for c_f in clause_formulas:
                solver.add(c_f)

            try:
                inv_expr = expr_builder.parse_expr(inv.formal_condition)
                
                # SMT Proof Principle:
                # To PROVE that invariant (I) always holds:
                # We assert (NOT I).
                # If solver returns UNSAT => No counterexample can ever exist => Invariant holds!
                # If solver returns SAT => A violation state exists => We have found a loophole/bug!
                solver.add(z3.Not(inv_expr))

                check_status = solver.check()
                elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)

                if check_status == z3.unsat:
                    # Formally proved!
                    results.append(InvariantCheckResult(
                        invariant_id=inv.invariant_id,
                        invariant_name=inv.name,
                        status=VerificationResultStatus.PROVED_VALID,
                        solver_time_ms=elapsed_ms,
                        involved_clauses=inv.target_clause_ids,
                        explanation="Formally verified. Under all admissible legal states, this invariant holds without contradiction."
                    ))

                elif check_status == z3.sat:
                    # Counterexample found!
                    violations_count += 1
                    model = solver.model()
                    
                    # Convert model into human readable dictionary
                    counterexample_dict = {}
                    for decl in model.decls():
                        name = decl.name()
                        val = model[decl]
                        if z3.is_rational_value(val):
                            counterexample_dict[name] = float(val.as_fraction())
                        else:
                            counterexample_dict[name] = str(val)

                    results.append(InvariantCheckResult(
                        invariant_id=inv.invariant_id,
                        invariant_name=inv.name,
                        status=VerificationResultStatus.VIOLATION_DETECTED,
                        solver_time_ms=elapsed_ms,
                        counterexample=counterexample_dict,
                        involved_clauses=inv.target_clause_ids,
                        explanation=f"Invariant violated! The solver constructed a mathematical scenario where all contract clauses are formally satisfied but the invariant fails."
                    ))

                else:
                    results.append(InvariantCheckResult(
                        invariant_id=inv.invariant_id,
                        invariant_name=inv.name,
                        status=VerificationResultStatus.SOLVER_TIMEOUT,
                        solver_time_ms=elapsed_ms,
                        involved_clauses=inv.target_clause_ids,
                        explanation="Solver could not determine satisfiability within allocated time limit."
                    ))

            except Exception as e:
                elapsed_ms = round((time.perf_counter() - start_time) * 1000, 2)
                results.append(InvariantCheckResult(
                    invariant_id=inv.invariant_id,
                    invariant_name=inv.name,
                    status=VerificationResultStatus.PARSE_ERROR,
                    solver_time_ms=elapsed_ms,
                    involved_clauses=inv.target_clause_ids,
                    explanation=f"Error constructing formal constraint: {str(e)}"
                ))

        return FullVerificationReport(
            contract_title=ast_model.contract_title,
            total_clauses=len(ast_model.clauses),
            total_invariants_checked=len(ast_model.invariants),
            violations_count=violations_count,
            results=results
        )
