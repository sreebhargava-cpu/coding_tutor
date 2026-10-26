import sys
import os
import json

# Add backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import SessionLocal, Base, engine
from app.routes import problems, tutor, progress
from app.schemas import (
    HintRequest,
    ExplainErrorRequest,
    ExplainConceptRequest,
    CodeQualityRequest,
    EdgeCaseRequest,
    RecordAttemptRequest,
    ExecutionResultPayload
)

def run_all_tests():
    db = SessionLocal()
    try:
        print("1. Testing problems.list_problems...")
        prob_list = problems.list_problems(db)
        assert len(prob_list) >= 8, f"Expected at least 8 problems, found {len(prob_list)}"
        print(f"   [PASS]: {len(prob_list)} problems found")

        print("2. Testing problems.get_problem...")
        p1 = problems.get_problem("p1_celsius_to_fahrenheit", db)
        assert p1.title == "Temperature Converter"
        assert len(p1.test_cases) >= 5
        print(f"   [PASS]: Loaded '{p1.title}' with {len(p1.test_cases)} test cases")

        print("3. Testing Socratic Hint generation (Level 1)...")
        exec_payload = ExecutionResultPayload(
            status="runtime_error",
            error_type="IndexError",
            error_message="list index out of range",
            error_line=2,
            stdout="",
            stderr="",
            passed_tests=0,
            total_tests=5,
            test_results=[],
            execution_time_ms=10.0
        )
        hint_req = HintRequest(
            problem_id="p1_celsius_to_fahrenheit",
            code="def celsius_to_fahrenheit(celsius):\n    return celsius[10]",
            execution_result=exec_payload,
            current_hint_level=1,
            previous_hints=[],
            attempt_number=1
        )
        hint = tutor.get_socratic_hint(hint_req, db)
        assert hint.hint_level == 1
        assert hint.should_reveal_solution is False
        assert len(hint.socratic_question) > 0
        print(f"   [PASS]: Socratic question: \"{hint.socratic_question}\"")

        print("4. Testing Socratic Hint progression (Level 2)...")
        hint_req_lvl2 = HintRequest(
            problem_id="p1_celsius_to_fahrenheit",
            code="def celsius_to_fahrenheit(celsius):\n    return celsius[10]",
            execution_result=exec_payload,
            current_hint_level=2,
            previous_hints=[hint.socratic_question],
            attempt_number=2
        )
        hint2 = tutor.get_socratic_hint(hint_req_lvl2, db)
        assert hint2.hint_level == 2
        print(f"   [PASS]: Level 2 Clue: \"{hint2.socratic_question}\"")

        print("5. Testing tutor.explain_error (Contextual Plain English)...")
        err_req = ExplainErrorRequest(
            problem_id="p1_celsius_to_fahrenheit",
            code="def celsius_to_fahrenheit(celsius):\n    return celsius[10]",
            error_type="IndexError",
            error_message="list index out of range",
            error_line=2
        )
        err_res = tutor.explain_error(err_req, db)
        assert err_res.error_type == "IndexError"
        assert len(err_res.friendly_summary) > 0
        print(f"   [PASS]: Summary: \"{err_res.friendly_summary}\"")

        print("6. Testing tutor.explain_concept...")
        concept_req = ExplainConceptRequest(
            problem_id="p1_celsius_to_fahrenheit",
            code="def celsius_to_fahrenheit(celsius):\n    return (celsius * 9 / 5) + 32",
            selected_text="range()",
            concept_name="range()"
        )
        concept_res = tutor.explain_concept(concept_req, db)
        assert len(concept_res.explanation) > 0
        print(f"   [PASS]: Explained '{concept_res.concept_name}'")

        print("7. Testing tutor.get_code_quality...")
        quality_req = CodeQualityRequest(
            problem_id="p1_celsius_to_fahrenheit",
            code="def celsius_to_fahrenheit(celsius):\n    result = (celsius * 9 / 5) + 32\n    return result"
        )
        quality_res = tutor.get_code_quality(quality_req, db)
        assert 0 <= quality_res.score <= 100
        assert len(quality_res.strengths) > 0
        print(f"   [PASS]: Quality Score {quality_res.score}/100, Strengths: {len(quality_res.strengths)}")

        print("8. Testing tutor.get_edge_cases...")
        edge_req = EdgeCaseRequest(
            problem_id="p1_celsius_to_fahrenheit",
            code="def celsius_to_fahrenheit(celsius):\n    return (celsius * 9 / 5) + 32"
        )
        edge_res = tutor.get_edge_cases(edge_req, db)
        assert len(edge_res.edge_cases) > 0
        print(f"   [PASS]: Generated {len(edge_res.edge_cases)} edge cases")

        print("9. Testing progress.record_attempt...")
        attempt_req = RecordAttemptRequest(
            problem_id="p1_celsius_to_fahrenheit",
            code="def celsius_to_fahrenheit(celsius):\n    return (celsius * 9 / 5) + 32",
            status="passed",
            passed_tests=5,
            total_tests=5,
            execution_time_ms=14.5,
            hints_used=1
        )
        att_res = progress.record_attempt(attempt_req, db)
        assert att_res["status"] == "success"
        assert att_res["is_solved"] is True
        print(f"   [PASS]: Attempt recorded, attempt_id: {att_res['attempt_id']}")

        print("10. Testing progress.get_progress_summary...")
        summary = progress.get_progress_summary(db)
        assert summary.problems_solved >= 1
        assert summary.total_attempts >= 1
        assert len(summary.common_difficulties) > 0
        print(f"   [PASS]: Solved: {summary.problems_solved}, Total attempts: {summary.total_attempts}")

        print("\n" + "="*50)
        print("ALL 10 COMPREHENSIVE BACKEND TEST SUITES PASSED!")
        print("="*50)

    finally:
        db.close()

if __name__ == "__main__":
    run_all_tests()
