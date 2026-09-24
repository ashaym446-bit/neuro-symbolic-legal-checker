import json
import os
import unittest
from core.dsl_schema import ContractAST, VerificationResultStatus
from core.symbolic_verifier import SymbolicContractVerifier
from core.explainer import LegalExplainer

class TestNeuroSymbolicVerifier(unittest.TestCase):

    def setUp(self):
        self.verifier = SymbolicContractVerifier()
        self.explainer = LegalExplainer()

    def test_contract_1_leverage_conflict(self):
        """Contract 1 should detect SAT (violation) on the debt ceiling during step-up."""
        with open("sample_contracts/contract_1_leverage_conflict.json", "r") as f:
            data = json.load(f)
        ast_model = ContractAST(**data)
        report = self.verifier.verify_contract(ast_model)

        self.assertEqual(report.violations_count, 1)
        res = [r for r in report.results if r.invariant_id == "INV-001"][0]
        self.assertEqual(res.status, VerificationResultStatus.VIOLATION_DETECTED)
        self.assertIsNotNone(res.counterexample)
        
        # Test explainer fallback
        enriched = self.explainer.explain_counterexample(res, ast_model.clauses, use_llm=False)
        self.assertIn("Mathematical Violation Detected", enriched.explanation)
        self.assertIn("Recommended Amendment", enriched.suggested_redline)

    def test_contract_2_temporal_deadlock(self):
        """Contract 2 should detect SAT on the 15-day grace period vs 5-day acceleration."""
        with open("sample_contracts/contract_2_temporal_deadlock.json", "r") as f:
            data = json.load(f)
        ast_model = ContractAST(**data)
        report = self.verifier.verify_contract(ast_model)

        self.assertEqual(report.violations_count, 1)
        res = report.results[0]
        self.assertEqual(res.status, VerificationResultStatus.VIOLATION_DETECTED)
        self.assertIsNotNone(res.counterexample)

    def test_contract_3_sound_facility(self):
        """Contract 3 should be proved valid (UNSAT for violation condition)."""
        with open("sample_contracts/contract_3_clean_facility.json", "r") as f:
            data = json.load(f)
        ast_model = ContractAST(**data)
        report = self.verifier.verify_contract(ast_model)

        self.assertEqual(report.violations_count, 0)
        res = report.results[0]
        self.assertEqual(res.status, VerificationResultStatus.PROVED_VALID)

if __name__ == '__main__':
    unittest.main()
