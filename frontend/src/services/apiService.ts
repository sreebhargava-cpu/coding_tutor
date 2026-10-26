import {
  ProblemSummary,
  ProblemDetail,
  HintResponse,
  ExplainErrorResponse,
  ExplainConceptResponse,
  CodeQualityResponse,
  EdgeCaseResponse,
  ProgressSummary,
  ExecutionResult,
} from '../types';

const API_BASE = '/api';

export async function fetchProblems(): Promise<ProblemSummary[]> {
  const res = await fetch(`${API_BASE}/problems`);
  if (!res.ok) throw new Error('Failed to fetch problems');
  return res.json();
}

export async function fetchProblemDetail(problemId: string): Promise<ProblemDetail> {
  const res = await fetch(`${API_BASE}/problems/${problemId}`);
  if (!res.ok) throw new Error(`Failed to fetch problem ${problemId}`);
  return res.json();
}

export async function requestSocraticHint(
  problemId: string,
  code: string,
  executionResult: ExecutionResult | null,
  currentHintLevel: number,
  previousHints: string[],
  attemptNumber: number
): Promise<HintResponse> {
  const res = await fetch(`${API_BASE}/tutor/hint`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      problem_id: problemId,
      code,
      execution_result: executionResult,
      current_hint_level: currentHintLevel,
      previous_hints: previousHints,
      attempt_number: attemptNumber,
    }),
  });
  if (!res.ok) throw new Error('Failed to request hint');
  return res.json();
}

export async function requestExplainError(
  problemId: string,
  code: string,
  errorType: string,
  errorMessage: string,
  errorLine?: number
): Promise<ExplainErrorResponse> {
  const res = await fetch(`${API_BASE}/tutor/explain-error`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      problem_id: problemId,
      code,
      error_type: errorType,
      error_message: errorMessage,
      error_line: errorLine,
    }),
  });
  if (!res.ok) throw new Error('Failed to explain error');
  return res.json();
}

export async function requestExplainConcept(
  problemId: string,
  code: string,
  selectedText: string,
  conceptName?: string
): Promise<ExplainConceptResponse> {
  const res = await fetch(`${API_BASE}/tutor/explain-concept`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      problem_id: problemId,
      code,
      selected_text: selectedText,
      concept_name: conceptName || selectedText,
    }),
  });
  if (!res.ok) throw new Error('Failed to explain concept');
  return res.json();
}

export async function requestCodeQuality(
  problemId: string,
  code: string
): Promise<CodeQualityResponse> {
  const res = await fetch(`${API_BASE}/tutor/code-quality`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      problem_id: problemId,
      code,
    }),
  });
  if (!res.ok) throw new Error('Failed to analyze code quality');
  return res.json();
}

export async function requestEdgeCases(
  problemId: string,
  code: string
): Promise<EdgeCaseResponse> {
  const res = await fetch(`${API_BASE}/tutor/edge-cases`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      problem_id: problemId,
      code,
    }),
  });
  if (!res.ok) throw new Error('Failed to generate edge cases');
  return res.json();
}

export async function recordAttempt(
  problemId: string,
  code: string,
  result: ExecutionResult,
  bugCategory?: string,
  hintsUsed: number = 0
): Promise<{ status: string; attempt_id: number; is_solved: boolean }> {
  const res = await fetch(`${API_BASE}/progress/attempt`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      problem_id: problemId,
      code,
      status: result.status,
      error_type: result.error_type,
      error_message: result.error_message,
      error_line: result.error_line,
      bug_category: bugCategory,
      passed_tests: result.passed_tests,
      total_tests: result.total_tests,
      execution_time_ms: result.execution_time_ms,
      hints_used: hintsUsed,
    }),
  });
  if (!res.ok) throw new Error('Failed to record attempt');
  return res.json();
}

export async function fetchProgressSummary(): Promise<ProgressSummary> {
  const res = await fetch(`${API_BASE}/progress/summary`);
  if (!res.ok) throw new Error('Failed to fetch progress summary');
  return res.json();
}

export async function resetProgress(): Promise<{ status: string }> {
  const res = await fetch(`${API_BASE}/progress/reset`, {
    method: 'POST',
  });
  if (!res.ok) throw new Error('Failed to reset progress');
  return res.json();
}
