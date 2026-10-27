with open("frontend/src/components/ConsoleOutput.tsx", "r", encoding="utf-8") as f:
    text = f.read()

target = """          {isPassed && (
            <div className="flex items-center space-x-1.5 text-emerald-400 text-xs font-semibold">
              <CheckCircle className="h-4 w-4" />
              <span>All Test Cases Passed ({result.passed_tests}/{result.total_tests})</span>
            </div>
          )}"""

replacement = """          {isPassed && result.test_results && result.test_results.length > 0 && (
            <div className="flex items-center space-x-1.5 text-emerald-400 text-xs font-semibold">
              <CheckCircle className="h-4 w-4" />
              <span>All Test Cases Passed ({result.passed_tests}/{result.total_tests})</span>
            </div>
          )}
          {isPassed && (!result.test_results || result.test_results.length === 0) && (
            <div className="flex items-center space-x-1.5 text-emerald-400 text-xs font-semibold">
              <CheckCircle className="h-4 w-4" />
              <span>Script Executed Successfully</span>
            </div>
          )}
          {result.status === 'timeout' && (
            <div className="flex items-center space-x-1.5 text-amber-400 text-xs font-semibold">
              <Clock className="h-4 w-4" />
              <span>Execution Timed Out (Infinite loop protection)</span>
            </div>
          )}"""

if target in text:
    text = text.replace(target, replacement)
    with open("frontend/src/components/ConsoleOutput.tsx", "w", encoding="utf-8") as f:
        f.write(text)
    print("ConsoleOutput.tsx updated!")
else:
    print("Warning: target not found in ConsoleOutput.tsx")
