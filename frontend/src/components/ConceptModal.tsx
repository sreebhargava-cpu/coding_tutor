import React, { useState } from 'react';
import { ExplainConceptResponse } from '../types';
import { X, HelpCircle, Code, Lightbulb, Sparkles } from 'lucide-react';

interface ConceptModalProps {
  isOpen: boolean;
  onClose: () => void;
  conceptData: ExplainConceptResponse | null;
  loading: boolean;
  onSearchConcept: (conceptName: string) => void;
  initialSelection?: string;
}

export const ConceptModal: React.FC<ConceptModalProps> = ({
  isOpen,
  onClose,
  conceptData,
  loading,
  onSearchConcept,
  initialSelection,
}) => {
  const [inputVal, setInputVal] = useState(initialSelection || '');

  if (!isOpen) return null;

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (inputVal.trim()) {
      onSearchConcept(inputVal.trim());
    }
  };

  const quickConcepts = ['range()', 'dict.get()', 'list slicing [::-1]', 'set()', 'isinstance()'];

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
      <div className="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-xl overflow-hidden shadow-2xl flex flex-col max-h-[85vh]">
        {/* Modal Header */}
        <div className="px-5 py-3.5 bg-slate-850 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center space-x-2 text-indigo-400 font-semibold text-sm">
            <HelpCircle className="h-4 w-4" />
            <span>Python Concept Explanation</span>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition"
          >
            <X className="h-4 w-4" />
          </button>
        </div>

        {/* Search Bar / Quick Suggestions */}
        <div className="p-4 bg-slate-900 border-b border-slate-800 space-y-2">
          <form onSubmit={handleSubmit} className="flex gap-2">
            <input
              type="text"
              value={inputVal}
              onChange={(e) => setInputVal(e.target.value)}
              placeholder="Ask about a concept (e.g. range, dict.get, slicing)..."
              className="flex-1 bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 font-mono"
            />
            <button
              type="submit"
              disabled={loading || !inputVal.trim()}
              className="px-4 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow transition disabled:opacity-50 flex items-center gap-1.5"
            >
              <Sparkles className="h-3.5 w-3.5" />
              <span>Explain</span>
            </button>
          </form>

          {/* Quick concept pills */}
          <div className="flex flex-wrap items-center gap-1.5 text-[11px] text-slate-400">
            <span>Suggestions:</span>
            {quickConcepts.map((q) => (
              <button
                key={q}
                onClick={() => {
                  setInputVal(q);
                  onSearchConcept(q);
                }}
                className="px-2 py-0.5 rounded-full bg-slate-800 hover:bg-slate-700 text-slate-300 font-mono border border-slate-700 transition"
              >
                {q}
              </button>
            ))}
          </div>
        </div>

        {/* Modal Body */}
        <div className="flex-1 overflow-y-auto p-5 space-y-4 text-xs leading-relaxed">
          {loading ? (
            <div className="py-12 flex flex-col items-center justify-center text-slate-400 space-y-2">
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-500"></div>
              <p className="font-mono">Analyzing concept in relation to your code...</p>
            </div>
          ) : conceptData ? (
            <div className="space-y-4">
              <div>
                <span className="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 font-mono">
                  Concept
                </span>
                <h3 className="text-base font-bold text-white mt-1">{conceptData.concept_name}</h3>
              </div>

              {/* General Explanation */}
              <div className="p-3.5 rounded-xl bg-slate-850 border border-slate-800 text-slate-200 space-y-1">
                <div className="font-semibold text-slate-300">How It Works</div>
                <p>{conceptData.explanation}</p>
              </div>

              {/* Context in Your Code */}
              {conceptData.context_in_your_code && (
                <div className="p-3.5 rounded-xl bg-indigo-950/30 border border-indigo-800/40 text-indigo-200 space-y-1">
                  <div className="font-semibold text-indigo-300">In Your Current Problem</div>
                  <p>{conceptData.context_in_your_code}</p>
                </div>
              )}

              {/* Mini Example */}
              {conceptData.mini_example && (
                <div className="space-y-1">
                  <div className="font-semibold text-slate-300 flex items-center gap-1.5">
                    <Code className="h-3.5 w-3.5 text-indigo-400" />
                    <span>Python Example</span>
                  </div>
                  <pre className="p-3 rounded-xl bg-slate-950 border border-slate-800 font-mono text-indigo-300 overflow-x-auto text-xs">
                    <code>{conceptData.mini_example}</code>
                  </pre>
                </div>
              )}

              {/* Pro Tip */}
              {conceptData.pro_tip && (
                <div className="p-3 rounded-xl bg-amber-500/10 border border-amber-500/20 text-amber-300 flex items-start gap-2">
                  <Lightbulb className="h-4 w-4 shrink-0 text-amber-400 mt-0.5" />
                  <div>
                    <span className="font-semibold text-amber-200">Pro-Tip: </span>
                    {conceptData.pro_tip}
                  </div>
                </div>
              )}
            </div>
          ) : (
            <div className="text-center py-10 text-slate-500">
              Select any code or enter a concept name to get a contextual explanation.
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
