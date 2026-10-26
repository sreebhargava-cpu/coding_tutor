import React from 'react';
import { CodeQualityResponse } from '../types';
import { X, CheckCircle2, HelpCircle, Sparkles, Award } from 'lucide-react';

interface QualityFeedbackModalProps {
  isOpen: boolean;
  onClose: () => void;
  data: CodeQualityResponse | null;
  loading: boolean;
}

export const QualityFeedbackModal: React.FC<QualityFeedbackModalProps> = ({
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
          <div className="flex items-center space-x-2 text-emerald-400 font-semibold text-sm">
            <Award className="h-4 w-4" />
            <span>Code Quality Coaching</span>
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
              <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-emerald-500"></div>
              <p className="font-mono">Reviewing readability, nesting, and Python conventions...</p>
            </div>
          ) : data ? (
            <div className="space-y-4">
              {/* Score card */}
              <div className="p-4 rounded-xl bg-slate-850 border border-slate-800 flex items-center justify-between">
                <div>
                  <div className="text-xs text-slate-400 font-medium">Readability & Style Score</div>
                  <div className="text-2xl font-bold text-white mt-0.5">{data.score} / 100</div>
                </div>
                <div className="h-12 w-12 rounded-full border-4 border-emerald-500 flex items-center justify-center font-bold text-emerald-400 text-sm">
                  {data.score}%
                </div>
              </div>

              {/* Readability Assessment */}
              <div className="p-3.5 rounded-xl bg-slate-850 border border-slate-800 space-y-1 text-slate-200">
                <div className="font-semibold text-slate-300">Overview</div>
                <p>{data.readability_feedback}</p>
              </div>

              {/* Strengths */}
              {data.strengths && data.strengths.length > 0 && (
                <div className="space-y-1.5">
                  <div className="font-semibold text-emerald-400 flex items-center gap-1.5">
                    <CheckCircle2 className="h-3.5 w-3.5" />
                    <span>What You Did Well</span>
                  </div>
                  <ul className="space-y-1 pl-4 list-disc text-slate-300">
                    {data.strengths.map((s, idx) => (
                      <li key={idx}>{s}</li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Socratic Improvement Questions */}
              {data.improvement_questions && data.improvement_questions.length > 0 && (
                <div className="p-3.5 rounded-xl bg-indigo-950/30 border border-indigo-800/40 space-y-2">
                  <div className="font-semibold text-indigo-300 flex items-center gap-1.5">
                    <HelpCircle className="h-3.5 w-3.5 text-indigo-400" />
                    <span>Questions to Consider for Improvement</span>
                  </div>
                  <ul className="space-y-1.5 pl-4 list-disc text-indigo-200">
                    {data.improvement_questions.map((q, idx) => (
                      <li key={idx}>{q}</li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Pythonic Tips */}
              {data.pythonic_tips && data.pythonic_tips.length > 0 && (
                <div className="p-3.5 rounded-xl bg-amber-500/10 border border-amber-500/20 space-y-1.5 text-amber-200">
                  <div className="font-semibold text-amber-300 flex items-center gap-1.5">
                    <Sparkles className="h-3.5 w-3.5 text-amber-400" />
                    <span>Idiomatic Python Tips</span>
                  </div>
                  <ul className="space-y-1 pl-4 list-disc text-amber-300/90">
                    {data.pythonic_tips.map((t, idx) => (
                      <li key={idx}>{t}</li>
                    ))}
                  </ul>
                </div>
              )}
            </div>
          ) : null}
        </div>
      </div>
    </div>
  );
};
