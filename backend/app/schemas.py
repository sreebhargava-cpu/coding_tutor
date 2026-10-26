from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict
from datetime import datetime

class TestCaseItem(BaseModel):
    input: Any
    input_str: Optional[str] = None
    expected: Any
    expected_str: Optional[str] = None
    is_hidden: bool = False
    explanation: Optional[str] = None

class ProblemBase(BaseModel):
    id: str
    title: str
    difficulty: str
    category: str
    learning_objective: str
    order_index: int = 0

class ProblemSummary(ProblemBase):
    is_solved: bool = False
    attempt_count: int = 0

    class Config:
        from_attributes = True

class ProblemDetail(ProblemBase):
    description: str
    starter_code: str
    function_name: str
    test_cases: List[TestCaseItem]
    edge_cases: Optional[List[Dict[str, Any]]] = None
    is_solved: bool = False

    class Config:
        from_attributes = True

class TestResultDetail(BaseModel):
    test_index: int
    input_str: str
    expected_str: str
    actual_str: Optional[str] = None
    passed: bool
    is_hidden: bool = False
    error: Optional[str] = None

class ExecutionResultPayload(BaseModel):
    status: str # passed, wrong_answer, runtime_error, syntax_error, timeout
    error_type: Optional[str] = None
    error_message: Optional[str] = None
    error_line: Optional[int] = None
    stdout: Optional[str] = ""
    stderr: Optional[str] = ""
    passed_tests: int = 0
    total_tests: int = 0
    test_results: List[TestResultDetail] = []
    execution_time_ms: float = 0.0

class HintRequest(BaseModel):
    problem_id: str
    code: str
    execution_result: Optional[ExecutionResultPayload] = None
    current_hint_level: int = 1
    previous_hints: List[str] = []
    attempt_number: int = 1

class HintResponse(BaseModel):
    bug_category: str
    hint_level: int # 1: Conceptual, 2: Directional, 3: Specific
    hint_title: str
    socratic_question: str
    hint_body: str
    targeted_line: Optional[int] = None
    should_reveal_solution: bool = False
    next_hint_available: bool = True

class ExplainErrorRequest(BaseModel):
    problem_id: str
    code: str
    error_type: str
    error_message: str
    error_line: Optional[int] = None

class ExplainErrorResponse(BaseModel):
    error_type: str
    friendly_summary: str
    what_happened: str
    why_it_happened: str
    guiding_question: str
    bug_category: str

class ExplainConceptRequest(BaseModel):
    problem_id: str
    code: str
    selected_text: str
    concept_name: Optional[str] = None

class ExplainConceptResponse(BaseModel):
    concept_name: str
    explanation: str
    context_in_your_code: str
    mini_example: str
    pro_tip: str

class CodeQualityRequest(BaseModel):
    problem_id: str
    code: str

class CodeQualityResponse(BaseModel):
    score: int # 0 - 100
    readability_feedback: str
    strengths: List[str]
    improvement_questions: List[str]
    pythonic_tips: List[str]

class EdgeCaseRequest(BaseModel):
    problem_id: str
    code: str

class EdgeCaseItem(BaseModel):
    name: str
    input_example: str
    why_important: str
    what_could_go_wrong: str

class EdgeCaseResponse(BaseModel):
    challenge_title: str
    intro_message: str
    edge_cases: List[EdgeCaseItem]
    socratic_challenge_question: str

class RecordAttemptRequest(BaseModel):
    problem_id: str
    code: str
    status: str
    error_type: Optional[str] = None
    error_message: Optional[str] = None
    error_line: Optional[int] = None
    bug_category: Optional[str] = None
    passed_tests: int = 0
    total_tests: int = 0
    execution_time_ms: float = 0.0
    hints_used: int = 0

class DifficultyStat(BaseModel):
    category: str
    display_name: str
    count: int

class ProgressSummaryResponse(BaseModel):
    problems_attempted: int
    problems_solved: int
    total_problems: int
    success_rate_percent: float
    total_attempts: int
    common_difficulties: List[DifficultyStat]
    recurring_weaknesses: List[str]
    suggested_focus: str
    recent_attempts: List[Dict[str, Any]]
