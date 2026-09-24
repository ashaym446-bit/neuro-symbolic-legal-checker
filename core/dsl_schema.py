from enum import Enum
from typing import List, Dict, Optional, Any, Union
from pydantic import BaseModel, Field

class InvariantType(str, Enum):
    QUANTITATIVE_CONSISTENCY = "quantitative_consistency" # e.g. Leverage ratio bounds & debt ceilings
    TEMPORAL_PRECEDENCE = "temporal_precedence"           # e.g. Notice period must elapse before acceleration
    MUTUAL_EXCLUSION = "mutual_exclusion"                 # e.g. Permitted liens vs Absolute negative pledge
    CROSS_DEFAULT_TRIGGER = "cross_default_trigger"       # e.g. Subsidiary default thresholds

class VariableType(str, Enum):
    REAL = "real"       # Continuous values: dollar amounts, ratios, percentages
    INTEGER = "integer" # Discrete values: business days, months, notice count
    BOOLEAN = "boolean" # States: is_default, is_acquisition_period, has_notice_served

class ContractVariable(BaseModel):
    name: str = Field(description="Unique variable identifier, e.g., 'total_debt', 'ebitda', 'cure_period_days'")
    var_type: VariableType = Field(default=VariableType.REAL, description="Data type for SMT solver representation")
    description: Optional[str] = Field(default="", description="Legal meaning of this variable in the contract")
    unit: Optional[str] = Field(default=None, description="e.g. USD, Ratio, Days, Boolean")

class ContractClause(BaseModel):
    clause_id: str = Field(description="Section or Article identifier, e.g. 'Section 6.01(a)'")
    title: str = Field(description="Short clause heading, e.g. 'Maximum Consolidated Leverage Ratio'")
    original_text: str = Field(description="Exact excerpt from the contract")
    formula: str = Field(description="Formal mathematical or logic expression, e.g. 'total_debt / ebitda <= 3.5'")
    condition: Optional[str] = Field(default="True", description="Precondition if applicable, e.g. 'is_acquisition_period == False'")
    referenced_variables: List[str] = Field(default_factory=list, description="Variables appearing in this clause")

class LegalInvariant(BaseModel):
    invariant_id: str = Field(description="Unique ID for this invariant, e.g. 'INV-001'")
    name: str = Field(description="Human readable name of the legal invariant rule")
    invariant_type: InvariantType
    description: str = Field(description="What safety or consistency property must always hold true")
    formal_condition: str = Field(description="Formula that must ALWAYS hold, e.g. 'total_debt <= 30000000'")
    target_clause_ids: List[str] = Field(default_factory=list, description="Clauses involved in this invariant")

class ContractAST(BaseModel):
    contract_title: str = Field(description="Document title, e.g. 'Senior Secured Credit Facility'")
    borrower: Optional[str] = Field(default="Borrower")
    lender: Optional[str] = Field(default="Administrative Agent / Lenders")
    variables: List[ContractVariable] = Field(default_factory=list)
    clauses: List[ContractClause] = Field(default_factory=list)
    invariants: List[LegalInvariant] = Field(default_factory=list)

class VerificationResultStatus(str, Enum):
    PROVED_VALID = "PROVED_VALID"             # Mathematically proved: invariant cannot be violated
    VIOLATION_DETECTED = "VIOLATION_DETECTED" # Conflict/loophole found! Counterexample generated
    SOLVER_TIMEOUT = "SOLVER_TIMEOUT"
    PARSE_ERROR = "PARSE_ERROR"

class InvariantCheckResult(BaseModel):
    invariant_id: str
    invariant_name: str
    status: VerificationResultStatus
    solver_time_ms: float
    counterexample: Optional[Dict[str, Any]] = None
    explanation: Optional[str] = None
    suggested_redline: Optional[str] = None
    involved_clauses: List[str] = Field(default_factory=list)

class FullVerificationReport(BaseModel):
    contract_title: str
    total_clauses: int
    total_invariants_checked: int
    violations_count: int
    results: List[InvariantCheckResult]
