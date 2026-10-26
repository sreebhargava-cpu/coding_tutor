import React from 'react';
import { HintResponse, ExecutionResult } from '../types';
import { 
  Bot, 
  Sparkles, 
  HelpCircle, 
  ArrowRight, 
  CheckCircle2, 
  ShieldAlert, 
  Code2, 
  FileQuestion,
  Lightbulb
} from 'lucide-react';

interface TutorPanelProps {
  hint: HintResponse | null;
  loadingHint: boolean;
  onRequestHint: (nextLevel?: boolean) => void;
  onRequestExplainError: () => void;
  onOpenConceptModal: () => void;
  onOpenQualityModal: () => void;
  onOpenEdgeCaseModal: () => void;
  executionResult: ExecutionResult | null;
  recurringWeaknesses: string[];
}

export const TutorPanel: React.FC<TutorPanelProps> = ({
  hint,
  loadingHint,
  onRequestHint,
  onRequestExplainError,
  onOpenConceptModal,
  onOpenQualityModal,
  onOpenEdgeCaseModal,
  executionResult,
  recurringWeaknesses,
}) => {
  const isPassed = executionResult?.status === 'passed';
  const hasError = executionResult && executionResult.status !== 'passed';

  const hintLevelLabels: Record<number, { name: string; desc: string }> = {
    1: { name: 'Conceptual Question', desc: 'Encourages reasoning about the core principle' },
    2: { name: 'Directional Clue', desc: 'Focuses in on where the discrepancy happens' },
    3: { name: 'Specific Guidance', desc: 'Targeted insight close to the root cause' },
  };

  return (
    <div className="h-full flex flex-col bg-slate-900 border-l border-slate-800 text-slate-200">
      {/* Tutor Header */}
      <div className="p-3.5 bg-slate-850 border-b border-slate-800 flex items-center justify-between">
        <div className="flex items-center space-x-2.5">
          <div className="h-8 w-8 rounded-lg bg-indigo-600/20 border border-indigo-500/30 flex items-center justify-center text-indigo-400">
            <Bot className="h-4.5 w-4.5" />
          </div>
          <div>
            <h3 className="text-xs font-bold text-white tracking-wide uppercase">AI Socratic Tutor</h3>
            <p className="text-[11px] text-slate-400">Adaptive Mentor & Guided Debugging</p>
          </div>
        </div>

        {hint && (
          <div className="flex items-center space-x-1">
            {[1, 2, 3].map((lvl) => (
              <div
                key={lvl}
                className={`h-2 rounded-full transition-all duration-300 ${
                  lvl <= hint.hint_level
                    ? 'w-5 bg-indigo-500'
                    : 'w-2 bg-slate-700'
                }`}
                title={`Hint Level ${lvl}`}
              />
            ))}
          </div>
        )}
      </div>

      {/* Action Buttons Toolbar */}
      <div className="p-3 bg-slate-900/90 border-b border-slate-800 grid grid-cols-2 gap-2 text-xs">
        <button
          onClick={() => onRequestHint(false)}
          disabled={loadingHint}
          className="flex items-center justify-center space-x-1.5 px-3 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-semibold shadow transition disabled:opacity-50"
        >
          <Lightbulb className="h-3.5 w-3.5 fill-current" />
          <span>{hint ? 'Refresh Hint' : 'Get Socratic Hint'}</span>
        </button>

        <button
          onClick={onRequestExplainError}
          disabled={!hasError}
          className={`flex items-center justify-center space-x-1.5 px-3 py-2 rounded-lg font-semibold border transition ${
            hasError
              ? 'bg-rose-500/10 text-rose-300 border-rose-500/30 hover:bg-rose-500/20'
              : 'bg-slate-800/40 text-slate-500 border-slate-800 cursor-not-allowed'
          }`}
        >
          <FileQuestion className="h-3.5 w-3.5" />
          <span>Explain Error</span>
        </button>

        <button
          onClick={onOpenConceptModal}
          className="flex items-center justify-center space-x-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-750 text-slate-200 border border-slate-700 font-medium transition"
        >
          <HelpCircle className="h-3.5 w-3.5 text-indigo-400" />
          <span>Explain Concept</span>
        </button>

        <button
          onClick={onOpenQualityModal}
          className="flex items-center justify-center space-x-1.5 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-750 text-slate-200 border border-slate-700 font-medium transition"
        >
          <Code2 className="h-3.5 w-3.5 text-emerald-400" />
          <span>Code Quality</span>
        </button>
      </div>

      {/* Main Mentor Body */}
      <div className="flex-1 p-4 overflow-y-auto space-y-4 text-xs">
        {/* Recurring Weakness Alert if relevant */}
        {recurringWeaknesses && recurringWeaknesses.length > 0 && (
          <div className="p-3 rounded-lg bg-amber-500/10 border border-amber-500/20 text-amber-300 flex items-start gap-2">
            <ShieldAlert className="h-4 w-4 shrink-0 text-amber-400 mt-0.5" />
            <div className="space-y-0.5">
              <span className="font-semibold text-amber-200">Historical Weakness Detected:</span>
              <p className="text-[11px] text-amber-300/90 leading-tight">
                You frequently encounter hurdles in <span className="underline font-medium">{recurringWeaknesses[0]}</span>. Check boundaries and assumptions carefully!
              </p>
            </div>
          </div>
        )}

        {/* All tests passed banner -> Suggest Edge Cases! */}
        {isPassed && (
          <div className="p-4 rounded-xl bg-emerald-950/40 border border-emerald-800/40 space-y-3">
            <div className="flex items-center space-x-2 text-emerald-400 font-semibold text-sm">
              <CheckCircle2 className="h-5 w-5" />
              <span>Great Job! Core Solution Passes</span>
            </div>
            <p className="text-slate-300 leading-relaxed">
              Your solution works for all basic test cases. Real-world programming requires thinking about boundary conditions and edge cases.
            </p>
            <button
              onClick={onOpenEdgeCaseModal}
              className="w-full py-2 px-3 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-semibold flex items-center justify-center space-x-1.5 shadow transition"
            >
              <Sparkles className="h-3.5 w-3.5" />
              <span>Take Edge-Case Challenge</span>
            </button>
          </div>
        )}

        {/* Socratic Hint Card */}
        {loadingHint ? (
          <div className="p-6 flex flex-col items-center justify-center text-slate-400 space-y-2">
            <div className="animate-spin rounded-full h-7 w-7 border-b-2 border-indigo-500"></div>
            <p className="text-xs font-mono">Analyzing code and formulating Socratic question...</p>
          </div>
        ) : hint ? (
          <div className="space-y-3.5">
            {/* Level indicator pill */}
            <div className="flex items-center justify-between">
              <div className="flex items-center space-x-1.5">
                <span className="px-2 py-0.5 rounded text-[10px] font-bold tracking-wider uppercase bg-indigo-500/20 text-indigo-300 border border-indigo-500/30">
                  Hint Level {hint.hint_level} of 3
                </span>
                <span className="text-slate-400 font-medium">
                  {hintLevelLabels[hint.hint_level]?.name}
                </span>
              </div>
              <span className="text-[11px] text-slate-500 font-mono">
                {hint.bug_category}
              </span>
            </div>

            {/* Socratic Question Bubble */}
            <div className="p-4 rounded-xl bg-gradient-to-br from-indigo-950/60 to-slate-900 border border-indigo-800/50 space-y-2 shadow-inner">
              <div className="text-[11px] font-semibold text-indigo-300 flex items-center gap-1.5">
                <Bot className="h-3.5 w-3.5 text-indigo-400" />
                <span>Mentor Asks:</span>
              </div>
              <blockquote className="text-sm font-medium text-white italic border-l-2 border-indigo-500 pl-3 leading-snug">
                "{hint.socratic_question}"
              </blockquote>
            </div>

            {/* Hint Body */}
            <div className="p-3.5 rounded-xl bg-slate-850 border border-slate-800 space-y-2 text-slate-300 leading-relaxed">
              <div className="font-semibold text-slate-200">{hint.hint_title}</div>
              <p>{hint.hint_body}</p>

              {hint.targeted_line && (
                <div className="pt-2 text-[11px] text-indigo-300 font-mono">
                  Focus investigation around <span className="font-semibold">line {hint.targeted_line}</span>.
                </div>
              )}
            </div>

            {/* Next Progressive Hint Button */}
            {hint.next_hint_available && (
              <button
                onClick={() => onRequestHint(true)}
                className="w-full flex items-center justify-center space-x-1.5 py-2 px-3 rounded-lg bg-slate-800 hover:bg-slate-750 text-indigo-300 hover:text-white border border-slate-700 font-medium transition"
              >
                <span>Still stuck? Get Level {hint.hint_level + 1} Hint</span>
                <ArrowRight className="h-3.5 w-3.5" />
              </button>
            )}
          </div>
        ) : (
          !isPassed && (
            <div className="p-6 rounded-xl bg-slate-850/60 border border-dashed border-slate-800 text-center space-y-3">
              <div className="h-10 w-10 mx-auto rounded-full bg-indigo-500/10 flex items-center justify-center text-indigo-400">
                <Lightbulb className="h-5 w-5" />
              </div>
              <div className="space-y-1">
                <h4 className="text-sm font-semibold text-slate-200">Need Guidance?</h4>
                <p className="text-slate-400 text-xs">
                  Run your code or click <span className="text-indigo-400 font-medium">Get Socratic Hint</span> to receive progressive questions that help you solve the problem yourself.
                </p>
              </div>
            </div>
          )
        )}
      </div>
    </div>
  );
};
