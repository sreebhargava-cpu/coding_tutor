import React from 'react';
import { ProblemDetail } from '../types';
import { Target, Lightbulb, CheckCircle2 } from 'lucide-react';

interface ProblemDescriptionProps {
  problem: ProblemDetail | null;
  loading: boolean;
}

export const ProblemDescription: React.FC<ProblemDescriptionProps> = ({ problem, loading }) => {
  if (loading) {
    return (
      <div className="h-full flex items-center justify-center p-6 text-slate-500">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-500"></div>
      </div>
    );
  }

  if (!problem) {
    return (
      <div className="h-full flex items-center justify-center p-6 text-slate-500">
        Select a problem to begin coding.
      </div>
    );
  }

  const difficultyColors = {
    Beginner: 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20',
    Intermediate: 'bg-amber-500/10 text-amber-400 border-amber-500/20',
    Advanced: 'bg-rose-500/10 text-rose-400 border-rose-500/20',
  };

  return (
    <div className="h-full overflow-y-auto p-5 text-slate-200 space-y-4">
      {/* Header Info */}
      <div className="space-y-2">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-2">
            <span
              className={`text-xs px-2.5 py-0.5 rounded-full border font-medium ${
                difficultyColors[problem.difficulty] || difficultyColors.Beginner
              }`}
            >
              {problem.difficulty}
            </span>
            <span className="text-xs px-2.5 py-0.5 rounded-full bg-slate-800 text-slate-300 border border-slate-700 font-mono">
              {problem.category}
            </span>
          </div>

          {problem.is_solved && (
            <span className="flex items-center gap-1 text-xs text-emerald-400 bg-emerald-500/10 border border-emerald-500/30 px-2.5 py-0.5 rounded-full font-medium">
              <CheckCircle2 className="h-3.5 w-3.5" /> Solved
            </span>
          )}
        </div>

        <h2 className="text-xl font-bold text-white tracking-tight">{problem.title}</h2>
      </div>

      {/* Learning Objective Callout */}
      <div className="p-3.5 rounded-xl bg-indigo-950/40 border border-indigo-800/40 text-indigo-200 text-xs flex items-start gap-2.5 leading-relaxed">
        <Target className="h-4 w-4 text-indigo-400 mt-0.5 shrink-0" />
        <div>
          <span className="font-semibold text-indigo-300">Learning Objective: </span>
          {problem.learning_objective}
        </div>
      </div>

      {/* Description Content */}
      <div className="prose prose-invert prose-sm max-w-none space-y-3 text-slate-300 text-xs leading-relaxed font-sans">
        {problem.description.split('\n\n').map((paragraph, idx) => {
          if (paragraph.startsWith('###')) {
            return (
              <h3 key={idx} className="text-sm font-semibold text-slate-100 mt-4 mb-2 flex items-center gap-1.5 border-b border-slate-800 pb-1">
                {paragraph.replace(/^###\s*/, '')}
              </h3>
            );
          }
          if (paragraph.startsWith('```')) {
            const cleanCode = paragraph.replace(/```[a-z]*\n?/g, '').trim();
            return (
              <pre key={idx} className="bg-slate-900 border border-slate-800 rounded-lg p-3 font-mono text-xs text-indigo-300 overflow-x-auto">
                <code>{cleanCode}</code>
              </pre>
            );
          }
          return (
            <p key={idx} className="text-slate-300">
              {paragraph}
            </p>
          );
        })}
      </div>

      {/* Public Test Cases Preview */}
      <div className="mt-4 pt-3 border-t border-slate-800 space-y-2">
        <h4 className="text-xs font-semibold text-slate-300 flex items-center gap-1.5 uppercase tracking-wider">
          <Lightbulb className="h-3.5 w-3.5 text-amber-400" />
          Example Test Cases
        </h4>
        <div className="space-y-2 font-mono text-xs">
          {problem.test_cases
            .filter((tc) => !tc.is_hidden)
            .map((tc, index) => (
              <div
                key={index}
                className="p-2.5 rounded-lg bg-slate-900/80 border border-slate-800 flex flex-col space-y-1"
              >
                <div className="text-slate-400">
                  <span className="text-slate-500">Input: </span>
                  <span className="text-emerald-400 font-medium">
                    {tc.input.map((arg) => (typeof arg === 'string' ? `"${arg}"` : JSON.stringify(arg))).join(', ')}
                  </span>
                </div>
                <div className="text-slate-400">
                  <span className="text-slate-500">Expected: </span>
                  <span className="text-indigo-400 font-medium">{JSON.stringify(tc.expected)}</span>
                </div>
                {tc.explanation && (
                  <div className="text-[11px] text-slate-500 font-sans italic">
                    Note: {tc.explanation}
                  </div>
                )}
              </div>
            ))}
        </div>
      </div>

      {/* 3 Progressive Hints Section */}
      {problem.hints && problem.hints.length > 0 && (
        <HintsAccordion hints={problem.hints} />
      )}

    </div>
  );
};

interface HintsAccordionProps {
  hints: string[];
}

const HintsAccordion: React.FC<HintsAccordionProps> = ({ hints }) => {
  const [revealedCount, setRevealedCount] = React.useState<number>(0);

  const titles = ["Hint 1: Conceptual Nudge", "Hint 2: Directional Clue", "Hint 3: Concrete Direction"];

  return (
    <div className="mt-4 pt-3 border-t border-slate-800 space-y-2">
      <div className="flex items-center justify-between">
        <h4 className="text-xs font-semibold text-slate-300 flex items-center gap-1.5 uppercase tracking-wider">
          <Lightbulb className="h-3.5 w-3.5 text-amber-400" />
          Curated Hints ({revealedCount}/{hints.length})
        </h4>
        {revealedCount < hints.length && (
          <button
            onClick={() => setRevealedCount((prev) => Math.min(hints.length, prev + 1))}
            className="text-[11px] px-2 py-0.5 rounded bg-indigo-600/30 text-indigo-300 hover:bg-indigo-600/50 border border-indigo-500/40 transition font-medium"
          >
            {revealedCount === 0 ? "Show Hint 1" : "Show Next Hint"}
          </button>
        )}
      </div>

      <div className="space-y-2">
        {hints.slice(0, revealedCount).map((hintText, idx) => (
          <div key={idx} className="p-2.5 rounded-lg bg-indigo-950/20 border border-indigo-900/40 text-xs space-y-1">
            <span className="text-[11px] font-semibold text-indigo-400 block">{titles[idx] || `Hint ${idx + 1}`}</span>
            <p className="text-slate-300 leading-relaxed">{hintText}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

