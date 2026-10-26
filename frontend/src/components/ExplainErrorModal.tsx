import React from 'react';
import { ExplainErrorResponse } from '../types';
import { X, AlertTriangle, HelpCircle, Sparkles } from 'lucide-react';

interface ExplainErrorModalProps {
  isOpen: boolean;
  onClose: () => void;
  data: ExplainErrorResponse | null;
  loading: boolean;
}

export const ExplainErrorModal: React.FC<ExplainErrorModalProps> = ({
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
          <div className="flex items-center space-x-2 text-rose-400 font-semibold text-sm">
            <AlertTriangle className="h-4 w-4" />
            <span>Python Error Explanation</span>
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
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-rose-500"></div>
              <p className="font-mono">Translating stack trace into plain English...</p>
            </div>
          ) : data ? (
            <div className="space-y-4">
              {/* Error type & Category */}
              <div className="flex items-center justify-between">
                <span className="text-base font-bold text-white font-mono">{data.error_type}</span>
                <span className="text-[10px] uppercase font-bold tracking-wider px-2 py-0.5 rounded bg-rose-500/10 text-rose-400 border border-rose-500/20 font-mono">
                  {data.bug_category}
                </span>
              </div>

              {/* Friendly summary */}
              <div className="p-3.5 rounded-xl bg-rose-950/30 border border-rose-800/40 text-rose-200">
                <div className="font-semibold text-rose-300 mb-0.5">Summary</div>
                <p>{data.friendly_summary}</p>
              </div>

              {/* What happened */}
              <div className="p-3.5 rounded-xl bg-slate-850 border border-slate-800 space-y-1 text-slate-200">
                <div className="font-semibold text-slate-300">What Python Attempted</div>
                <p>{data.what_happened}</p>
              </div>

              {/* Why it happened */}
              <div className="p-3.5 rounded-xl bg-slate-850 border border-slate-800 space-y-1 text-slate-200">
                <div className="font-semibold text-slate-300">Why It Happened</div>
                <p>{data.why_it_happened}</p>
              </div>

              {/* Guiding Socratic Question */}
              <div className="p-4 rounded-xl bg-gradient-to-br from-indigo-950/60 to-slate-900 border border-indigo-800/50 space-y-1.5">
                <div className="text-[11px] font-semibold text-indigo-300 flex items-center gap-1.5">
                  <HelpCircle className="h-3.5 w-3.5 text-indigo-400" />
                  <span>Next Step for You</span>
                </div>
                <blockquote className="text-sm font-medium text-white italic border-l-2 border-indigo-500 pl-3">
                  "{data.guiding_question}"
                </blockquote>
              </div>
            </div>
          ) : null}
        </div>
      </div>
    </div>
  );
};
