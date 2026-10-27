export interface TestCase {
  input: any[];
  expected: any;
  is_hidden?: boolean;
  explanation?: string;
}

export interface ProblemSummary {
  id: string;
  title: string;
  difficulty: 'Beginner' | 'Intermediate' | 'Advanced';
  category: string;
  learning_objective: string;
  order_index: number;
  is_solved: boolean;
  attempt_count: number;
  is_preset?: boolean;
}

export interface EdgeCasePredefined {
  name: string;
  input_example: string;
  why_important: string;
  what_could_go_wrong: string;
}

export interface ProblemDetail extends ProblemSummary {
  description: string;
  starter_code: string;
  function_name: string;
  test_cases: TestCase[];
  edge_cases?: EdgeCasePredefined[];
  hints?: string[];
  is_preset?: boolean;
}

export interface TestResultDetail {
  test_index: number;
  input_str: string;
  expected_str: string;
  actual_str?: string;
  passed: boolean;
  is_hidden: boolean;
  error?: string;
}

export interface ExecutionResult {
  status: 'passed' | 'wrong_answer' | 'runtime_error' | 'syntax_error' | 'timeout';
  error_type?: string;
  error_message?: string;
  error_line?: number;
  stdout: string;
  stderr: string;
  passed_tests: number;
  total_tests: number;
  test_results: TestResultDetail[];
  execution_time_ms: number;
}

export interface HintResponse {
  bug_category: string;
  hint_level: number; // 1, 2, or 3
  hint_title: string;
  socratic_question: string;
  hint_body: string;
  targeted_line?: number;
  should_reveal_solution: boolean;
  next_hint_available: boolean;
}

export interface ExplainErrorResponse {
  error_type: string;
  friendly_summary: string;
  what_happened: string;
  why_it_happened: string;
  guiding_question: string;
  bug_category: string;
}

export interface ExplainConceptResponse {
  concept_name: string;
  explanation: string;
  context_in_your_code: string;
  mini_example: string;
  pro_tip: string;
}

export interface CodeQualityResponse {
  score: number;
  readability_feedback: string;
  strengths: string[];
  improvement_questions: string[];
  pythonic_tips: string[];
}

export interface EdgeCaseItem {
  name: string;
  input_example: string;
  why_important: string;
  what_could_go_wrong: string;
}

export interface EdgeCaseResponse {
  challenge_title: string;
  intro_message: string;
  edge_cases: EdgeCaseItem[];
  socratic_challenge_question: string;
}

export interface DifficultyStat {
  category: string;
  display_name: string;
  count: number;
}

export interface RecentAttemptItem {
  id: number;
  problem_id: string;
  problem_title: string;
  status: string;
  bug_category: string;
  passed_tests: number;
  total_tests: number;
  hints_used: number;
  is_solved: boolean;
  timestamp: string;
}

export interface ProgressSummary {
  problems_attempted: number;
  problems_solved: number;
  total_problems: number;
  completion_rate_percent?: number;
  attempt_success_rate_percent?: number;
  success_rate_percent: number;
  total_attempts: number;
  common_difficulties: DifficultyStat[];
  recurring_weaknesses: string[];
  suggested_focus: string;
  recent_attempts: RecentAttemptItem[];
}
