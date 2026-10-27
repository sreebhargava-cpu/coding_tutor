import React, { useState } from 'react';
import { ExecutionResult } from '../types';
import { 
  CheckCircle, 
  XCircle, 
  AlertTriangle, 
  Clock, 
  Terminal, 
  Sparkles,
  ChevronRight
} from 'lucide-react';

interface ConsoleOutputProps {
  result: ExecutionResult | null;
  isRunning: boolean;
  onAskExplainError: () => void;
}

export const ConsoleOutput: React.FC<ConsoleOutputProps> = ({
  result,
  isRunning,
  onAskExplainError,
}) => {
  const [activeTab, setActiveTab] = useState<'tests' | 'terminal'>('tests');
  const [selectedTestIndex, setSelectedTestIndex] = useState<number>(0);

  if (isRunning) {
    return (
      <div className="h-full flex flex-col items-center justify-center p-6 bg-slate-950 text-slate-400">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-500 mb-2"></div>
        <p className="text-xs font-mono">Executing in Pyodide WebAssembly runtime...</p>
      </div>
    );
  }

  if (!result) {
    return (
      <div className="h-full flex flex-col items-center justify-center p-6 bg-slate-950 text-slate-500">
        <Terminal className="h-7 w-7 text-slate-600 mb-2" />
        <p className="text-xs">Click <span className="text-indigo-400 font-semibold">Run Code</span> to test your solution</p>
      </div>
    );
  }

  const isPassed = result.status === 'passed';
  const isRuntimeError = result.status === 'runtime_error';
  const isSyntaxError = result.status === 'syntax_error';
  const isWrongAnswer = result.status === 'wrong_answer';

  return (
    <div className="h-full flex flex-col bg-slate-950 text-slate-200">
      {/* Result Status Header Bar */}
      <div className="px-4 py-2 bg-slate-900 border-b border-slate-800 flex items-center justify-between">
        <div className="flex items-center space-x-2">
          {isPassed && result.test_results && result.test_results.length > 0 && (
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
          )}
          {isWrongAnswer && (
            <div className="flex items-center space-x-1.5 text-amber-400 text-xs font-semibold">
              <XCircle className="h-4 w-4" />
              <span>Wrong Answer ({result.passed_tests}/{result.total_tests} passed)</span>
            </div>
          )}
          {isRuntimeError && (
            <div className="flex items-center space-x-1.5 text-rose-400 text-xs font-semibold">
              <AlertTriangle className="h-4 w-4" />
              <span>Runtime Error: {result.error_type}</span>
            </div>
          )}
          {isSyntaxError && (
            <div className="flex items-center space-x-1.5 text-rose-400 text-xs font-semibold">
              <AlertTriangle className="h-4 w-4" />
              <span>Syntax Error</span>
            </div>
          )}

          <span className="text-[11px] text-slate-500 font-mono flex items-center gap-1">
            <Clock className="h-3 w-3" /> {result.execution_time_ms} ms
          </span>
        </div>

        {/* View mode toggle */}
        <div className="flex items-center space-x-1 bg-slate-850 p-0.5 rounded border border-slate-800 text-[11px]">
          <button
            onClick={() => setActiveTab('tests')}
            className={`px-2 py-0.5 rounded font-medium transition ${
              activeTab === 'tests' ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            Test Cases
          </button>
          <button
            onClick={() => setActiveTab('terminal')}
            className={`px-2 py-0.5 rounded font-medium transition ${
              activeTab === 'terminal' ? 'bg-indigo-600 text-white' : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            Terminal Output
          </button>
        </div>
      </div>

      {/* Error Callout Banner if error occurred */}
      {(isRuntimeError || isSyntaxError) && (
        <div className="p-3 bg-rose-950/40 border-b border-rose-800/40 flex items-start justify-between gap-3">
          <div className="space-y-0.5">
            <div className="text-xs font-semibold text-rose-300 flex items-center gap-1.5">
              <span>{result.error_type || 'Error'}</span>
              {result.error_line && (
                <span className="text-[11px] px-1.5 py-0.2 rounded bg-rose-900/60 text-rose-200 border border-rose-700/50">
                  Line {result.error_line}
                </span>
              )}
            </div>
            <p className="text-xs text-rose-200 font-mono">{result.error_message}</p>
          </div>

          <button
            onClick={onAskExplainError}
            className="shrink-0 flex items-center space-x-1.5 px-3 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-500 text-white text-xs font-semibold shadow-md shadow-rose-900/30 transition"
          >
            <Sparkles className="h-3.5 w-3.5" />
            <span>Explain Error</span>
          </button>
        </div>
      )}

      {/* Tab 1: Test Cases Viewer */}
      {activeTab === 'tests' && (
        <div className="flex-1 flex overflow-hidden">
          {/* Test Tabs Sidebar */}
          <div className="w-36 bg-slate-900/60 border-r border-slate-800 overflow-y-auto p-2 space-y-1 text-xs">
            {result.test_results.map((tr, idx) => (
              <button
                key={idx}
                onClick={() => setSelectedTestIndex(idx)}
                className={`w-full flex items-center justify-between px-2.5 py-1.5 rounded-md font-mono text-xs transition ${
                  selectedTestIndex === idx
                    ? 'bg-indigo-600/20 text-indigo-300 border border-indigo-500/40 font-semibold'
                    : 'text-slate-400 hover:bg-slate-800/80 hover:text-slate-200'
                }`}
              >
                <span>Test {tr.test_index}</span>
                {tr.passed ? (
                  <CheckCircle className="h-3.5 w-3.5 text-emerald-400 shrink-0" />
                ) : (
                  <XCircle className="h-3.5 w-3.5 text-rose-400 shrink-0" />
                )}
              </button>
            ))}
          </div>

          {/* Test Case Detail Content */}
          <div className="flex-1 p-4 overflow-y-auto space-y-3 font-mono text-xs">
            {result.test_results[selectedTestIndex] ? (
              (() => {
                const tr = result.test_results[selectedTestIndex];
                return (
                  <div className="space-y-3">
                    <div className="flex items-center justify-between">
                      <span className="font-semibold text-slate-300">
                        Case {tr.test_index} {tr.is_hidden ? '(Hidden Test)' : ''}
                      </span>
                      <span
                        className={`px-2 py-0.5 rounded text-[11px] font-semibold ${
                          tr.passed
                            ? 'bg-emerald-500/10 text-emerald-400 border border-emerald-500/30'
                            : 'bg-rose-500/10 text-rose-400 border border-rose-500/30'
                        }`}
                      >
                        {tr.passed ? 'PASSED' : 'FAILED'}
                      </span>
                    </div>

                    <div className="space-y-1">
                      <div className="text-slate-500 text-[11px]">Input:</div>
                      <div className="p-2 rounded bg-slate-900 border border-slate-800 text-slate-200">
                        {tr.input_str}
                      </div>
                    </div>

                    <div className="space-y-1">
                      <div className="text-slate-500 text-[11px]">Expected:</div>
                      <div className="p-2 rounded bg-slate-900 border border-slate-800 text-indigo-300">
                        {tr.expected_str}
                      </div>
                    </div>

                    <div className="space-y-1">
                      <div className="text-slate-500 text-[11px]">Your Output:</div>
                      <div
                        className={`p-2 rounded border ${
                          tr.passed
                            ? 'bg-slate-900 border-slate-800 text-emerald-300'
                            : 'bg-rose-950/20 border-rose-900/50 text-rose-300'
                        }`}
                      >
                        {tr.actual_str !== undefined ? tr.actual_str : (tr.error ? `Error: ${tr.error}` : 'None')}
                      </div>
                    </div>
                  </div>
                );
              })()
            ) : (
              <div className="text-slate-500">No test case details available for this run.</div>
            )}
          </div>
        </div>
      )}

      {/* Tab 2: Terminal Output Viewer */}
      {activeTab === 'terminal' && (
        <div className="flex-1 p-3 overflow-y-auto font-mono text-xs text-slate-300 bg-slate-950">
          {result.stdout ? (
            <pre className="whitespace-pre-wrap">{result.stdout}</pre>
          ) : (
            <span className="text-slate-600 italic">No standard output printed during execution.</span>
          )}
          {result.stderr && (
            <pre className="mt-2 text-rose-400 whitespace-pre-wrap">{result.stderr}</pre>
          )}
        </div>
      )}
    </div>
  );
};
