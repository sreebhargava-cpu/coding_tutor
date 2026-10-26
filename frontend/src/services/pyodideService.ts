import { ExecutionResult, TestCase, TestResultDetail } from '../types';

declare global {
  interface Window {
    loadPyodide?: any;
    pyodideInstance?: any;
  }
}

let pyodidePromise: Promise<any> | null = null;

export async function getPyodide(): Promise<any> {
  if (window.pyodideInstance) {
    return window.pyodideInstance;
  }

  if (pyodidePromise) {
    return pyodidePromise;
  }

  pyodidePromise = new Promise(async (resolve, reject) => {
    try {
      // Ensure pyodide.js script is loaded
      if (!window.loadPyodide) {
        const script = document.createElement('script');
        script.src = 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/pyodide.js';
        script.async = true;
        await new Promise((res, rej) => {
          script.onload = res;
          script.onerror = () => rej(new Error('Failed to load Pyodide WebAssembly runtime script'));
          document.head.appendChild(script);
        });
      }

      const pyodide = await window.loadPyodide({
        indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.26.4/full/',
      });

      window.pyodideInstance = pyodide;
      resolve(pyodide);
    } catch (err) {
      pyodidePromise = null;
      reject(err);
    }
  });

  return pyodidePromise;
}

/**
 * Runs student Python code against predefined test cases directly in the browser via Pyodide.
 */
export async function executeAndTestCode(
  userCode: string,
  functionName: string,
  testCases: TestCase[]
): Promise<ExecutionResult> {
  const startTime = performance.now();
  const pyodide = await getPyodide();

  // Test runner wrapper Python script
  // We execute the student's code and capture stdout/stderr safely
  const runnerScript = `
import sys
import io
import json
import traceback

stdout_buf = io.StringIO()
stderr_buf = io.StringIO()
old_stdout = sys.stdout
old_stderr = sys.stderr

sys.stdout = stdout_buf
sys.stderr = stderr_buf

exec_error = None
error_type = None
error_msg = None
error_line = None

# Step 1: Execute student code in clean dictionary scope
student_scope = {}
try:
    exec(compile(${JSON.stringify(userCode)}, '<student_code>', 'exec'), student_scope)
except SyntaxError as se:
    error_type = "SyntaxError"
    error_msg = str(se.msg)
    error_line = se.lineno
    exec_error = "SyntaxError"
except Exception as e:
    error_type = type(e).__name__
    error_msg = str(e)
    # Extract line number from traceback
    tb = traceback.extract_tb(sys.exc_info()[2])
    for frame in tb:
        if frame.filename == '<student_code>':
            error_line = frame.lineno
            break
    exec_error = error_type

# Restore streams
sys.stdout = old_stdout
sys.stderr = old_stderr

run_stdout = stdout_buf.getvalue()
run_stderr = stderr_buf.getvalue()

output_data = {
    "syntax_or_compile_error": exec_error,
    "error_type": error_type,
    "error_message": error_msg,
    "error_line": error_line,
    "stdout": run_stdout,
    "stderr": run_stderr
}
json.dumps(output_data)
`;

  try {
    const compileResultRaw = await pyodide.runPythonAsync(runnerScript);
    const compileResult = JSON.parse(compileResultRaw);

    // If student code failed during compilation / execution
    if (compileResult.syntax_or_compile_error) {
      const isSyntax = compileResult.error_type === 'SyntaxError';
      return {
        status: isSyntax ? 'syntax_error' : 'runtime_error',
        error_type: compileResult.error_type,
        error_message: compileResult.error_message,
        error_line: compileResult.error_line,
        stdout: compileResult.stdout,
        stderr: compileResult.stderr,
        passed_tests: 0,
        total_tests: testCases.length,
        test_results: [],
        execution_time_ms: Math.round(performance.now() - startTime),
      };
    }

    // Now test against each test case
    const testResults: TestResultDetail[] = [];
    let passedCount = 0;
    let firstRuntimeError: { type: string; msg: string; line?: number } | null = null;

    // Run test cases inside pyodide using a test harness
    for (let i = 0; i < testCases.length; i++) {
      const tc = testCases[i];
      const tcInputJson = JSON.stringify(tc.input);
      const tcExpectedJson = JSON.stringify(tc.expected);
      const isHidden = !!tc.is_hidden;

      const singleTestScript = `
import json
import sys
import traceback

func = student_scope.get(${JSON.stringify(functionName)})
test_input = json.loads(${JSON.stringify(tcInputJson)})
expected_val = json.loads(${JSON.stringify(tcExpectedJson)})

res = {
    "passed": False,
    "actual": None,
    "error": None,
    "error_type": None,
    "error_line": None
}

if func is None:
    res["error"] = f"Function '{${JSON.stringify(functionName)}}' is not defined in your code."
    res["error_type"] = "NameError"
else:
    try:
        actual = func(*test_input)
        res["actual"] = actual
        
        # Check expected exception vs normal return
        if isinstance(expected_val, str) and expected_val.startswith("EXCEPTION:"):
            res["passed"] = False
            res["error"] = f"Expected exception {expected_val.split(':')[1]}, but function returned normally."
        else:
            # Handle float approximate equality
            if isinstance(expected_val, float) and isinstance(actual, (int, float)):
                res["passed"] = abs(actual - expected_val) < 1e-4
            else:
                res["passed"] = (actual == expected_val)
    except Exception as e:
        exc_type = type(e).__name__
        res["error_type"] = exc_type
        res["error"] = str(e)
        
        # Check if exception was expected
        if isinstance(expected_val, str) and expected_val == f"EXCEPTION:{exc_type}":
            res["passed"] = True
        else:
            res["passed"] = False
            # Find traceback line
            tb = traceback.extract_tb(sys.exc_info()[2])
            for frame in tb:
                if frame.filename == '<student_code>':
                    res["error_line"] = frame.lineno
                    break

def serialize_res(obj):
    try:
        return json.dumps(obj)
    except Exception:
        return json.dumps({"passed": obj.get("passed", False), "actual": str(obj.get("actual")), "error": obj.get("error")})

serialize_res(res)
`;

      const testResRaw = await pyodide.runPythonAsync(singleTestScript);
      const testRes = JSON.parse(testResRaw);

      if (testRes.passed) {
        passedCount++;
      } else if (!firstRuntimeError && testRes.error_type) {
        firstRuntimeError = {
          type: testRes.error_type,
          msg: testRes.error,
          line: testRes.error_line,
        };
      }

      testResults.push({
        test_index: i + 1,
        input_str: tc.input.map((arg) => (typeof arg === 'string' ? `"${arg}"` : JSON.stringify(arg))).join(', '),
        expected_str: typeof tc.expected === 'string' ? tc.expected : JSON.stringify(tc.expected),
        actual_str: testRes.actual !== undefined ? (typeof testRes.actual === 'string' ? `"${testRes.actual}"` : JSON.stringify(testRes.actual)) : undefined,
        passed: testRes.passed,
        is_hidden: isHidden,
        error: testRes.error,
      });
    }

    const allPassed = passedCount === testCases.length;
    let finalStatus: 'passed' | 'wrong_answer' | 'runtime_error' = 'wrong_answer';
    if (allPassed) {
      finalStatus = 'passed';
    } else if (firstRuntimeError) {
      finalStatus = 'runtime_error';
    }

    return {
      status: finalStatus,
      error_type: firstRuntimeError ? firstRuntimeError.type : undefined,
      error_message: firstRuntimeError ? firstRuntimeError.msg : (finalStatus === 'wrong_answer' ? 'Output does not match expected result on test cases.' : undefined),
      error_line: firstRuntimeError?.line,
      stdout: compileResult.stdout || '',
      stderr: compileResult.stderr || '',
      passed_tests: passedCount,
      total_tests: testCases.length,
      test_results: testResults,
      execution_time_ms: Math.round(performance.now() - startTime),
    };
  } catch (globalErr: any) {
    return {
      status: 'runtime_error',
      error_type: 'ExecutionError',
      error_message: globalErr.message || String(globalErr),
      stdout: '',
      stderr: String(globalErr),
      passed_tests: 0,
      total_tests: testCases.length,
      test_results: [],
      execution_time_ms: Math.round(performance.now() - startTime),
    };
  }
}
