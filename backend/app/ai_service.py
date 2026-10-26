import json
import logging
import os
import re
from typing import Dict, Any, List, Optional
from .config import settings
from .schemas import (
    HintResponse,
    ExplainErrorResponse,
    ExplainConceptResponse,
    CodeQualityResponse,
    EdgeCaseResponse,
    EdgeCaseItem,
)

logger = logging.getLogger("ai_service")

# Initialize Gemini Client if API key is provided
_gemini_client = None

def get_gemini_client():
    global _gemini_client
    api_key = settings.GEMINI_API_KEY or os.environ.get("GEMINI_API_KEY", "")
    if not api_key:
        return None
    if _gemini_client is None:
        try:
            from google import genai
            _gemini_client = genai.Client(api_key=api_key)
        except Exception as e:
            logger.warning(f"Failed to initialize google-genai client: {e}")
            return None
    return _gemini_client

def call_gemini(prompt: str, system_instruction: str = "") -> Optional[str]:
    """Helper to safely query Gemini with error catching."""
    client = get_gemini_client()
    if not client:
        return None
    try:
        response = client.models.generate_content(
            model=settings.GEMINI_MODEL,
            contents=prompt,
            config={
                "system_instruction": system_instruction,
                "temperature": 0.3,
            }
        )
        return response.text
    except Exception as e:
        logger.error(f"Gemini API call failed: {e}")
        return None

def extract_json(raw_text: str) -> Optional[Dict[str, Any]]:
    """Extract JSON object from model response even if surrounded by markdown fences."""
    if not raw_text:
        return None
    cleaned = raw_text.strip()
    # Strip markdown ```json ... ```
    if cleaned.startswith("```"):
        match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", cleaned)
        if match:
            cleaned = match.group(1).strip()
    try:
        return json.loads(cleaned)
    except Exception:
        # Fallback regex search for { ... }
        match = re.search(r"\{[\s\S]*\}", cleaned)
        if match:
            try:
                return json.loads(match.group(0))
            except Exception:
                pass
    return None

# ==============================================================================
# 1. SOCRATIC DEBUGGING & ADAPTIVE 3-LEVEL HINT SYSTEM
# ==============================================================================

def generate_socratic_hint(
    problem_title: str,
    problem_desc: str,
    learning_obj: str,
    student_code: str,
    execution_result: Optional[Dict[str, Any]],
    hint_level: int, # 1, 2, or 3
    previous_hints: List[str],
    student_weaknesses: List[str] = None
) -> HintResponse:
    """
    Produces adaptive Socratic hints:
    - Level 1: Conceptual question
    - Level 2: Directional clue
    - Level 3: Specific guidance
    NEVER directly writes the corrected code.
    """
    weakness_context = f"Student known recurring weaknesses: {', '.join(student_weaknesses)}" if student_weaknesses else ""

    system_prompt = (
        "You are an expert Socratic Python Programming Tutor. Your mission is to help the student learn "
        "by guiding them to discover and fix bugs on their own. "
        "CRITICAL RULES:\n"
        "1. NEVER give the direct solution or write the corrected code for the student.\n"
        "2. Do not say 'Change line X to Y'. Instead ask thought-provoking questions.\n"
        "3. Match the requested Hint Level strictly:\n"
        "   - Level 1 (Conceptual): Ask a broad question about the concept, loop boundaries, types, or data structures.\n"
        "   - Level 2 (Directional): Point the student's attention to the specific variable, condition, or block causing the unexpected behavior.\n"
        "   - Level 3 (Specific): Give focused guidance comparing the expected vs actual state at that step, bringing them within reach of fixing it.\n"
        "4. Output strictly valid JSON matching the schema."
    )

    prompt = f"""
Problem: {problem_title}
Objective: {learning_obj}
Problem Description:
{problem_desc}

{weakness_context}

Student's Current Python Code:
```python
{student_code}
```

Execution Result:
{json.dumps(execution_result, indent=2) if execution_result else "Code has not run or syntax error"}

Requested Hint Level: {hint_level} (1=Conceptual, 2=Directional, 3=Specific)
Previous hints already shown: {json.dumps(previous_hints)}

Return ONLY a JSON object with this exact structure:
{{
  "bug_category": "one of: syntax_error, variable_error, conditional_logic, loops, indexing, functions, data_structures, type_error, logical_error, edge_case",
  "hint_level": {hint_level},
  "hint_title": "Short title describing the focal area",
  "socratic_question": "A sharp Socratic question that makes the student think about what their code is actually doing",
  "hint_body": "Explanation of the concept or guidance tailored to Level {hint_level}",
  "targeted_line": <optional line number integer or null>,
  "should_reveal_solution": false,
  "next_hint_available": { "true" if hint_level < 3 else "false" }
}}
"""
    raw_response = call_gemini(prompt, system_instruction=system_prompt)
    parsed = extract_json(raw_response) if raw_response else None

    if parsed and "socratic_question" in parsed:
        return HintResponse(
            bug_category=parsed.get("bug_category", "logical_error"),
            hint_level=hint_level,
            hint_title=parsed.get("hint_title", f"Level {hint_level} Hint"),
            socratic_question=parsed.get("socratic_question", "What did you expect this code to produce?"),
            hint_body=parsed.get("hint_body", "Review your logic step by step."),
            targeted_line=parsed.get("targeted_line"),
            should_reveal_solution=False,
            next_hint_available=(hint_level < 3)
        )

    # Heuristic Socratic Fallback
    return _fallback_socratic_hint(student_code, execution_result, hint_level, problem_title)

def _fallback_socratic_hint(
    student_code: str,
    execution_result: Optional[Dict[str, Any]],
    hint_level: int,
    problem_title: str
) -> HintResponse:
    """Intelligent rule-based Socratic hints when offline/no API key."""
    status = (execution_result or {}).get("status", "")
    err_type = (execution_result or {}).get("error_type", "")
    err_msg = (execution_result or {}).get("error_message", "")
    err_line = (execution_result or {}).get("error_line")

    category = "logical_error"
    title = "Investigating Behavior"
    question = "What values do your variables hold when your code executes?"
    body = "Trace your code step by step with pencil and paper for a small input."

    if err_type == "IndexError" or "index" in err_msg.lower():
        category = "indexing"
        title = "List Index Boundary"
        if hint_level == 1:
            question = "How many elements are currently in your list, and what is the valid index of the last element?"
            body = "Remember that Python lists use zero-based indexing: a list with N items has valid indices from 0 up to N - 1."
        elif hint_level == 2:
            question = "At what point in your loop or slice does the index value exceed the length of the list?"
            body = "Take a close look at the stopping condition of your loop or the offset you are adding to the index."
        else:
            question = "Could your index be reaching len(collection) instead of stopping before it?"
            body = "Check line " + str(err_line or "of your loop") + ". Notice that accessing `list[len(list)]` will immediately trigger an IndexError."

    elif err_type == "TypeError" or "type" in err_msg.lower():
        category = "type_error"
        title = "Data Type Compatibility"
        if hint_level == 1:
            question = "What data types are you attempting to combine or operate on?"
            body = "Operations like `+` behave differently between numbers (addition) and strings or lists (concatenation)."
        elif hint_level == 2:
            question = "Is one of your variables holding a string or None where an integer or list was expected?"
            body = "Inspect the type of the value returned or passed into this operation."
        else:
            question = "Does the function signature or operation require explicit type conversion (e.g. `int()`, `str()`)?"
            body = "Verify the types on line " + str(err_line or "where the error triggered") + " before carrying out the operation."

    elif err_type == "NameError" or "is not defined" in err_msg.lower():
        category = "variable_error"
        title = "Variable Scope & Definition"
        if hint_level == 1:
            question = "Has this variable been assigned a value before your code attempts to read from it?"
            body = "Python executes sequentially from top to bottom; a variable must exist before it is referenced."
        elif hint_level == 2:
            question = "Is there a typo in the spelling or capitalization of the variable name?"
            body = "Python identifiers are case-sensitive. Check that your definition and usage match letter-for-letter."
        else:
            question = "Is the variable defined inside a different scope or conditional block that didn't run?"
            body = "Check line " + str(err_line or "indicated in the error") + " to verify where this identifier was initialized."

    elif status == "syntax_error":
        category = "syntax_error"
        title = "Python Syntax Structure"
        if hint_level == 1:
            question = "Does every statement, loop, and conditional follow Python's grammatical rules?"
            body = "Python requires colons `:` at the end of `def`, `if`, `for`, `while`, and balanced brackets `()`, `[]`, `{}`."
        elif hint_level == 2:
            question = "Is there an unclosed quote, mismatched bracket, or missing colon near the indicated line?"
            body = "Syntax errors often point to the line immediately following the actual missing punctuation."
        else:
            question = "Look at the exact character right before the red indicator. Is a colon, comma, or parenthesis missing?"
            body = "Review lines " + str(err_line or "around the error") + " carefully."

    elif status == "wrong_answer":
        category = "logical_error"
        title = "Expected vs Actual Output"
        if hint_level == 1:
            question = "What does the problem expect for the first failing test case compared to what your code returned?"
            body = "Notice if the output differs in data type (e.g. integer vs float, list vs element) or calculation value."
        elif hint_level == 2:
            question = "Does your function explicitly `return` the final result, or does it only print it (or return None)?"
            body = "Remember that grading checks the value returned by `return`, not output printed with `print()`."
        else:
            question = "Walk through the first failing test case by hand. Does your condition branch as expected?"
            body = "Check your return statement and whether the accumulator or loop condition updates properly."

    return HintResponse(
        bug_category=category,
        hint_level=hint_level,
        hint_title=title,
        socratic_question=question,
        hint_body=body,
        targeted_line=err_line,
        should_reveal_solution=False,
        next_hint_available=(hint_level < 3)
    )

# ==============================================================================
# 2. CONTEXTUAL ERROR EXPLANATION (Section 9)
# ==============================================================================

def explain_runtime_error(
    problem_title: str,
    student_code: str,
    error_type: str,
    error_message: str,
    error_line: Optional[int]
) -> ExplainErrorResponse:
    """Translates technical errors into student-friendly contextual language."""
    system_prompt = (
        "You are an encouraging coding teacher. Explain the Python error in simple, friendly, intuitive language. "
        "Do NOT invent errors. Base your explanation strictly on the provided code and Python error. "
        "Return strictly valid JSON."
    )
    prompt = f"""
Problem: {problem_title}
Student's Code:
```python
{student_code}
```
Error Type: {error_type}
Error Message: {error_message}
Error Line: {error_line}

Return ONLY JSON:
{{
  "error_type": "{error_type}",
  "friendly_summary": "One sentence non-jargon explanation of what happened",
  "what_happened": "Detailed clear description of what Python tried to do",
  "why_it_happened": "Why the student's code at line {error_line} caused this",
  "guiding_question": "A Socratic question to guide the student to the fix",
  "bug_category": "category identifier (e.g. indexing, type_error, syntax_error)"
}}
"""
    raw = call_gemini(prompt, system_instruction=system_prompt)
    parsed = extract_json(raw) if raw else None

    if parsed and "friendly_summary" in parsed:
        return ExplainErrorResponse(
            error_type=error_type,
            friendly_summary=parsed.get("friendly_summary", ""),
            what_happened=parsed.get("what_happened", ""),
            why_it_happened=parsed.get("why_it_happened", ""),
            guiding_question=parsed.get("guiding_question", ""),
            bug_category=parsed.get("bug_category", "runtime_error")
        )

    # Heuristic fallback explanations
    translations = {
        "IndexError": {
            "summary": "Your program reached for a slot in the list that doesn't exist.",
            "what": "Python tried to access an item at an index number beyond the valid range of the collection.",
            "why": f"On line {error_line or 'in your code'}, the index requested was greater than or equal to the total number of items.",
            "question": "How many items are in the list, and what is the highest valid index you can access?",
            "cat": "indexing"
        },
        "TypeError": {
            "summary": "Your code tried to perform an action on incompatible data types.",
            "what": "An operation or function was applied to an object of inappropriate type (e.g. adding text to a number).",
            "why": f"The values involved on line {error_line or 'in your code'} cannot be processed together with this operator.",
            "question": "What type of data does each variable hold right before this line runs?",
            "cat": "type_error"
        },
        "ZeroDivisionError": {
            "summary": "Your program attempted to divide a number by zero.",
            "what": "In mathematics and programming, division by zero is undefined and causes a halt.",
            "why": f"The divisor variable on line {error_line or 'in your expression'} evaluated to 0.",
            "question": "Under what condition could the denominator become 0, and how can you check for that beforehand?",
            "cat": "conditional_logic"
        },
        "KeyError": {
            "summary": "Your code looked for a key that isn't inside the dictionary.",
            "what": "You tried to retrieve a dictionary value using a key that does not exist.",
            "why": f"The dictionary does not have the specified key at line {error_line or 'in your code'}.",
            "question": "Have you checked whether the key exists using `in` or `dict.get()` before reading it?",
            "cat": "data_structures"
        },
        "NameError": {
            "summary": "Python encountered a variable name it doesn't recognize.",
            "what": "A variable was used before it was assigned or its name was misspelled.",
            "why": f"On line {error_line or 'in your code'}, Python looked for an identifier that has not been defined in this scope.",
            "question": "Is the variable created before this line, and is the spelling exact?",
            "cat": "variable_error"
        }
    }

    t = translations.get(error_type, {
        "summary": f"Your program encountered a {error_type}.",
        "what": error_message or "An unexpected runtime condition stopped your program.",
        "why": f"Line {error_line or 'in your code'} triggered an unhandled exception.",
        "question": "What assumptions did your code make about the input or state at this step?",
        "cat": "runtime_error"
    })

    return ExplainErrorResponse(
        error_type=error_type,
        friendly_summary=t["summary"],
        what_happened=t["what"],
        why_it_happened=t["why"],
        guiding_question=t["question"],
        bug_category=t["cat"]
    )

# ==============================================================================
# 3. CONCEPT EXPLANATION IN CONTEXT (Section 14)
# ==============================================================================

def explain_concept_in_context(
    problem_title: str,
    student_code: str,
    selected_text: str,
    concept_name: Optional[str] = None
) -> ExplainConceptResponse:
    """Explains a programming concept related directly to the student's current code."""
    system_prompt = (
        "You are an encouraging computer science professor. Explain the requested Python concept "
        "specifically in the context of the student's problem and code. "
        "Keep it clear, concise, and provide a small code snippet. Return strictly valid JSON."
    )
    prompt = f"""
Problem: {problem_title}
Selected Text: "{selected_text}"
Concept Name: "{concept_name or selected_text}"

Student's Python Code:
```python
{student_code}
```

Return ONLY JSON:
{{
  "concept_name": "{concept_name or selected_text}",
  "explanation": "Clear, accessible explanation of what this concept does in Python",
  "context_in_your_code": "How this concept applies to the student's current code or problem",
  "mini_example": "A short 2-3 line Python example demonstrating proper usage",
  "pro_tip": "A best-practice tip or common pitfall to watch out for"
}}
"""
    raw = call_gemini(prompt, system_instruction=system_prompt)
    parsed = extract_json(raw) if raw else None

    if parsed and "explanation" in parsed:
        return ExplainConceptResponse(
            concept_name=parsed.get("concept_name", concept_name or selected_text),
            explanation=parsed.get("explanation", ""),
            context_in_your_code=parsed.get("context_in_your_code", ""),
            mini_example=parsed.get("mini_example", ""),
            pro_tip=parsed.get("pro_tip", "")
        )

    # Heuristic fallback concept explanation
    target = (concept_name or selected_text).lower().strip()
    return ExplainConceptResponse(
        concept_name=concept_name or selected_text,
        explanation=f"'{target}' is a fundamental Python construct used to manipulate values and control program flow.",
        context_in_your_code=f"In your code for {problem_title}, this construct allows you to process inputs cleanly.",
        mini_example=f"# Example using {target}\nresult = [x for x in [1, 2, 3] if x > 1]",
        pro_tip=f"Always test edge cases such as empty inputs or zero when working with {target}."
    )

# ==============================================================================
# 4. CODE QUALITY COACHING (Section 13)
# ==============================================================================

def coach_code_quality(
    problem_title: str,
    student_code: str
) -> CodeQualityResponse:
    """Evaluates working code for readability, PEP 8, unnecessary complexity, and structure."""
    system_prompt = (
        "You are a Senior Python Software Engineer coaching a student. "
        "Evaluate code quality, readability, variable names, excessive nesting, and Pythonic practices. "
        "Ask questions rather than rewriting everything. Return strictly valid JSON."
    )
    prompt = f"""
Problem: {problem_title}
Student's Code:
```python
{student_code}
```

Return ONLY JSON:
{{
  "score": <integer from 1 to 100 based on code quality and clean style>,
  "readability_feedback": "Paragraph summarizing how easy or difficult the code is to read and understand",
  "strengths": ["List of 2-3 things the student did well (e.g. clear logic, concise check)"],
  "improvement_questions": ["List of 2-3 Socratic questions prompting better names, less nesting, or fewer temp variables"],
  "pythonic_tips": ["List of 2 actionable tips on idiomatic Python (e.g. list comprehensions, dict.get, in operator)"]
}}
"""
    raw = call_gemini(prompt, system_instruction=system_prompt)
    parsed = extract_json(raw) if raw else None

    if parsed and "readability_feedback" in parsed:
        return CodeQualityResponse(
            score=parsed.get("score", 85),
            readability_feedback=parsed.get("readability_feedback", "Your code executes properly!"),
            strengths=parsed.get("strengths", ["Logical structure is sound"]),
            improvement_questions=parsed.get("improvement_questions", ["Could variable names be more descriptive?"]),
            pythonic_tips=parsed.get("pythonic_tips", ["Consider using Python built-in helpers"])
        )

    # Heuristic fallback
    lines = [l for l in student_code.splitlines() if l.strip()]
    score = 80
    strengths = ["Your code successfully addresses the functional requirements."]
    questions = []
    tips = []

    if any(len(l) - len(l.lstrip()) > 12 for l in lines):
        questions.append("Notice deep nesting in your code. Could early returns or guard clauses flatten the structure?")
        score -= 10
    else:
        strengths.append("Good control of nesting and indentation depth.")

    if any(var in student_code for var in ["temp", "flag", "x", "a", "b"]):
        questions.append("Are single-letter or generic variable names like 'temp' conveying their clear purpose?")
        tips.append("Use descriptive variable names such as `total_sum` or `word_counts` to make your code self-documenting.")
    else:
        strengths.append("Clean and understandable variable naming.")

    tips.append("Follow PEP 8 guidelines for 4-space indentation and snake_case function naming.")

    return CodeQualityResponse(
        score=score,
        readability_feedback="Your solution is functional and clean. Looking closely at naming and structure can elevate it further.",
        strengths=strengths,
        improvement_questions=questions or ["Could any temporary variables be simplified?"],
        pythonic_tips=tips
    )

# ==============================================================================
# 5. EDGE-CASE COACHING (Section 15)
# ==============================================================================

def generate_edge_case_challenges(
    problem_title: str,
    student_code: str,
    predefined_edge_cases: Optional[List[Dict[str, Any]]] = None
) -> EdgeCaseResponse:
    """Challenges students with boundary conditions, unusual inputs, and edge cases."""
    system_prompt = (
        "You are an expert tutor emphasizing software robustness. Once a basic solution works, "
        "encourage the student to consider boundary inputs and edge cases. Return strictly valid JSON."
    )
    prompt = f"""
Problem: {problem_title}
Student's Working Code:
```python
{student_code}
```
Predefined problem edge cases: {json.dumps(predefined_edge_cases or [])}

Return ONLY JSON:
{{
  "challenge_title": "Edge Case Challenge: Make Your Code Bulletproof",
  "intro_message": "Congratulate them on passing initial tests, and introduce edge cases.",
  "edge_cases": [
    {{
      "name": "Edge case name (e.g. Empty Input, Negative Numbers, Duplicate Values)",
      "input_example": "Exact representation of the boundary input",
      "why_important": "Why real-world code must account for this scenario",
      "what_could_go_wrong": "What would happen if the current code ran this input"
    }}
  ],
  "socratic_challenge_question": "A question asking the student how their current code would behave under these conditions."
}}
"""
    raw = call_gemini(prompt, system_instruction=system_prompt)
    parsed = extract_json(raw) if raw else None

    if parsed and "edge_cases" in parsed:
        cases = []
        for c in parsed.get("edge_cases", []):
            cases.append(EdgeCaseItem(
                name=c.get("name", "Boundary Case"),
                input_example=c.get("input_example", ""),
                why_important=c.get("why_important", ""),
                what_could_go_wrong=c.get("what_could_go_wrong", "")
            ))
        return EdgeCaseResponse(
            challenge_title=parsed.get("challenge_title", "Edge-Case Challenge"),
            intro_message=parsed.get("intro_message", "Great job getting the core solution working! Now test its robustness."),
            edge_cases=cases,
            socratic_challenge_question=parsed.get("socratic_challenge_question", "What happens if you pass an empty input?")
        )

    # Fallback to predefined problem edge cases
    cases = []
    if predefined_edge_cases:
        for ec in predefined_edge_cases:
            cases.append(EdgeCaseItem(
                name=ec.get("name", "Boundary Value"),
                input_example=ec.get("input_example", "[]"),
                why_important=ec.get("why_important", "Ensures code does not crash on unexpected inputs."),
                what_could_go_wrong=ec.get("what_could_go_wrong", "Potential index error or unhandled empty condition.")
            ))
    else:
        cases.append(EdgeCaseItem(
            name="Empty Collection",
            input_example="[] or ''",
            why_important="Functions should handle empty structures without raising IndexError.",
            what_could_go_wrong="Accessing index 0 will fail."
        ))

    return EdgeCaseResponse(
        challenge_title="Edge-Case Challenge: Beyond the Happy Path",
        intro_message="Awesome work! Your code passes the basic tests. But how resilient is it against unexpected inputs?",
        edge_cases=cases,
        socratic_challenge_question="If an unexpected boundary value arrives, does your code handle it gracefully or raise an unhandled exception?"
    )
