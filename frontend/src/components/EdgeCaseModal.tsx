import React from 'react';
import { EdgeCaseResponse } from '../types';
import { X, Sparkles, Shield, AlertCircle, HelpCircle } from 'lucide-react';

interface EdgeCaseModalProps {
  isOpen: boolean;
  onClose: () => void;
  data: EdgeCaseResponse | null;
  loading: boolean;
}

export const EdgeCaseModal: React.FC<EdgeCaseModalProps> = ({
  isOpen,
  onClose,
  data,
  loading,
}) => {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
      <div className="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-xl overflow-hidden shadow-2xl flex flex-col max-h-[85vh]">
        {/* Header */}
        <div className="px-5 py-3.5 bg-slate-850 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center space-x-2 text-indigo-400 font-semibold text-sm">
            <Sparkles className="h-4 w-4" />
            <span>Edge-Case Coaching & Robustness</span>
          </div>
          <button
            onClick={onClose}
            className="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition"
          >
            <X className="h-4 w-4" />
          </button>
        </div>

        {/* Body */}
        <div className="flex-1 overflow-y-auto p-5 space-y-4 text-xs leading-relaxed">
          {loading ? (
            <div className="py-12 flex flex-col items-center justify-center text-slate-400 space-y-2">
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-500"></div>
              <p className="font-mono">Analyzing boundary conditions and unusual inputs...</p>
            </div>
          ) : data ? (
            <div className="space-y-4">
              {/* Intro Callout */}
              <div className="p-3.5 rounded-xl bg-indigo-950/40 border border-indigo-800/40 text-indigo-200">
                <h4 className="font-bold text-white text-sm mb-1">{data.challenge_title}</h4>
                <p>{data.intro_message}</p>
              </div>

              {/* Edge Cases List */}
              <div className="space-y-3">
                <div className="font-semibold text-slate-200 flex items-center gap-1.5">
                  <Shield className="h-4 w-4 text-indigo-400" />
                  <span>Boundary Scenarios to Test</span>
                </div>

                <div className="space-y-2.5">
                  {data.edge_cases.map((ec, idx) => (
                    <div
                      key={idx}
                      className="p-3 rounded-xl bg-slate-850 border border-slate-800 space-y-1.5"
                    >
                      <div className="flex items-center justify-between">
                        <span className="font-semibold text-white">{ec.name}</span>
                        <code className="text-[11px] px-2 py-0.5 rounded bg-slate-800 text-indigo-300 font-mono border border-slate-700">
                          {ec.input_example}
                        </code>
                      </div>
                      <p className="text-slate-300">
                        <span className="text-slate-400 font-medium">Why it matters: </span>
                        {ec.why_important}
                      </p>
                      <div className="flex items-start gap-1.5 text-rose-300/90 text-[11px]">
                        <AlertCircle className="h-3.5 w-3.5 shrink-0 text-rose-400 mt-0.5" />
                        <span>Potential Pitfall: {ec.what_could_go_wrong}</span>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              {/* Socratic Challenge Question */}
              <div className="p-4 rounded-xl bg-gradient-to-br from-indigo-950/60 to-slate-900 border border-indigo-800/50 space-y-1.5">
                <div className="text-[11px] font-semibold text-indigo-300 flex items-center gap-1.5">
                  <HelpCircle className="h-3.5 w-3.5 text-indigo-400" />
                  <span>Think About This:</span>
                </div>
                <blockquote className="text-sm font-medium text-white italic border-l-2 border-indigo-500 pl-3">
                  "{data.socratic_challenge_question}"
                </blockquote>
              </div>
            </div>
          ) : null}
        </div>
      </div>
    </div>
  );
};
