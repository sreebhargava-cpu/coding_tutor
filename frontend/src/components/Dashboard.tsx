import React, { useEffect, useState } from 'react';
import { ProgressSummary } from '../types';
import { fetchProgressSummary, resetProgress } from '../services/apiService';
import { 
  BarChart, 
  Bar, 
  XAxis, 
  YAxis, 
  Tooltip, 
  ResponsiveContainer, 
  Cell 
} from 'recharts';
import { 
  Trophy, 
  Target, 
  RotateCcw, 
  CheckCircle2, 
  XCircle, 
  AlertTriangle, 
  Sparkles,
  TrendingUp,
  BrainCircuit,
  History
} from 'lucide-react';

interface DashboardProps {
  onSelectProblem: (id: string) => void;
  onReturnToWorkspace: () => void;
}

export const Dashboard: React.FC<DashboardProps> = ({ onSelectProblem, onReturnToWorkspace }) => {
  const [summary, setSummary] = useState<ProgressSummary | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  const loadSummary = async () => {
    try {
      setLoading(true);
      const data = await fetchProgressSummary();
      setSummary(data);
    } catch (err) {
      console.error('Failed to load progress summary', err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadSummary();
  }, []);

  const handleReset = async () => {
    if (window.confirm('Are you sure you want to reset your learning history?')) {
      await resetProgress();
      await loadSummary();
    }
  };

  if (loading) {
    return (
      <div className="h-full flex items-center justify-center p-8 text-slate-400">
        <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-indigo-500 mb-2"></div>
      </div>
    );
  }

  if (!summary) {
    return (
      <div className="h-full flex items-center justify-center p-8 text-slate-500">
        No progress data available.
      </div>
    );
  }

  const chartColors = ['#6366f1', '#8b5cf6', '#ec4899', '#f43f5e', '#f97316', '#eab308'];

  return (
    <div className="h-full overflow-y-auto p-6 space-y-6 max-w-6xl mx-auto">
      {/* Top Banner */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-4 border-b border-slate-800">
        <div>
          <h2 className="text-xl font-bold text-white flex items-center gap-2">
            <TrendingUp className="h-5 w-5 text-indigo-400" />
            Learning & Progress Dashboard
          </h2>
          <p className="text-xs text-slate-400 mt-1">
            Tracking problem completion, common bugs, and personal growth over time.
          </p>
        </div>

        <div className="flex items-center space-x-2">
          <button
            onClick={onReturnToWorkspace}
            className="px-3.5 py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold shadow transition"
          >
            Continue Coding
          </button>
          <button
            onClick={handleReset}
            className="p-1.5 rounded-lg text-slate-400 hover:text-rose-400 hover:bg-slate-800 border border-slate-700/60 transition"
            title="Reset Learning History"
          >
            <RotateCcw className="h-4 w-4" />
          </button>
        </div>
      </div>

      {/* KPI Metric Cards */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
        {/* Solved Problems */}
        <div className="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-sm flex items-center space-x-3.5">
          <div className="h-10 w-10 rounded-xl bg-emerald-500/10 border border-emerald-500/20 flex items-center justify-center text-emerald-400">
            <Trophy className="h-5 w-5" />
          </div>
          <div>
            <div className="text-[11px] font-medium text-slate-400">Problems Solved</div>
            <div className="text-xl font-bold text-white">
              {summary.problems_solved}{' '}
              <span className="text-xs text-slate-500 font-normal">/ {summary.total_problems}</span>
            </div>
          </div>
        </div>

        {/* Success Rate */}
        <div className="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-sm flex items-center space-x-3.5">
          <div className="h-10 w-10 rounded-xl bg-indigo-500/10 border border-indigo-500/20 flex items-center justify-center text-indigo-400">
            <Target className="h-5 w-5" />
          </div>
          <div>
            <div className="text-[11px] font-medium text-slate-400">Curriculum Rate</div>
            <div className="text-xl font-bold text-white">{summary.success_rate_percent}%</div>
          </div>
        </div>

        {/* Total Coding Attempts */}
        <div className="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-sm flex items-center space-x-3.5">
          <div className="h-10 w-10 rounded-xl bg-violet-500/10 border border-violet-500/20 flex items-center justify-center text-violet-400">
            <History className="h-5 w-5" />
          </div>
          <div>
            <div className="text-[11px] font-medium text-slate-400">Total Attempts</div>
            <div className="text-xl font-bold text-white">{summary.total_attempts}</div>
          </div>
        </div>

        {/* Problems Attempted */}
        <div className="p-4 rounded-2xl bg-slate-900 border border-slate-800 shadow-sm flex items-center space-x-3.5">
          <div className="h-10 w-10 rounded-xl bg-amber-500/10 border border-amber-500/20 flex items-center justify-center text-amber-400">
            <BrainCircuit className="h-5 w-5" />
          </div>
          <div>
            <div className="text-[11px] font-medium text-slate-400">Problems Explored</div>
            <div className="text-xl font-bold text-white">{summary.problems_attempted}</div>
          </div>
        </div>
      </div>

      {/* Suggested Focus Recommendation Banner */}
      <div className="p-4 rounded-2xl bg-gradient-to-r from-indigo-950/70 via-indigo-900/30 to-slate-900 border border-indigo-800/50 flex items-start gap-3 shadow-md">
        <Sparkles className="h-5 w-5 text-indigo-400 shrink-0 mt-0.5" />
        <div className="space-y-1">
          <h4 className="text-xs font-bold text-indigo-300 uppercase tracking-wide">
            Personalized Tutor Recommendation
          </h4>
          <p className="text-sm font-medium text-slate-200">{summary.suggested_focus}</p>
        </div>
      </div>

      {/* Charts & Weakness Analytics Grid */}
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Recharts Bar Chart: Common Difficulties */}
        <div className="lg:col-span-2 p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="text-sm font-bold text-white">Error Categories & Common Pitfalls</h3>
            <span className="text-[11px] text-slate-500">Frequency of mistakes recorded</span>
          </div>

          <div className="h-64 w-full">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart
                data={summary.common_difficulties}
                margin={{ top: 10, right: 10, left: -20, bottom: 25 }}
              >
                <XAxis
                  dataKey="display_name"
                  tick={{ fill: '#94a3b8', fontSize: 10 }}
                  interval={0}
                  angle={-25}
                  textAnchor="end"
                />
                <YAxis
                  tick={{ fill: '#94a3b8', fontSize: 11 }}
                  allowDecimals={false}
                />
                <Tooltip
                  contentStyle={{
                    backgroundColor: '#0f172a',
                    borderColor: '#334155',
                    borderRadius: '8px',
                    fontSize: '12px',
                    color: '#f8fafc',
                  }}
                />
                <Bar dataKey="count" radius={[4, 4, 0, 0]}>
                  {summary.common_difficulties.map((_, index) => (
                    <Cell key={`cell-${index}`} fill={chartColors[index % chartColors.length]} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Identified Recurring Weaknesses */}
        <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-4 flex flex-col justify-between">
          <div className="space-y-3">
            <h3 className="text-sm font-bold text-white">Identified Weaknesses</h3>
            <p className="text-xs text-slate-400">
              The AI tutor incorporates these historical weaknesses into future Socratic prompts for tailored questions.
            </p>

            <div className="space-y-2 pt-2">
              {summary.recurring_weaknesses && summary.recurring_weaknesses.length > 0 ? (
                summary.recurring_weaknesses.map((w, idx) => (
                  <div
                    key={idx}
                    className="p-3 rounded-xl bg-slate-850 border border-slate-800 flex items-center justify-between"
                  >
                    <span className="text-xs font-semibold text-slate-200">{w}</span>
                    <span className="text-[10px] px-2 py-0.5 rounded-full bg-rose-500/10 text-rose-400 border border-rose-500/20 font-medium">
                      Needs Practice
                    </span>
                  </div>
                ))
              ) : (
                <div className="p-6 rounded-xl bg-slate-850/50 border border-dashed border-slate-800 text-center text-xs text-slate-500">
                  No recurring weaknesses recorded yet. Keep practicing!
                </div>
              )}
            </div>
          </div>

          <div className="p-3 rounded-xl bg-indigo-950/20 border border-indigo-900/40 text-[11px] text-indigo-300">
            Tip: Solve problems in your weakest area to reinforce core mechanics.
          </div>
        </div>
      </div>

      {/* Attempt History Table */}
      <div className="p-5 rounded-2xl bg-slate-900 border border-slate-800 space-y-3">
        <h3 className="text-sm font-bold text-white">Recent Attempt History</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-left text-xs text-slate-300">
            <thead className="bg-slate-850 text-slate-400 font-semibold border-b border-slate-800">
              <tr>
                <th className="p-2.5">Problem</th>
                <th className="p-2.5">Status</th>
                <th className="p-2.5">Bug Category</th>
                <th className="p-2.5">Tests</th>
                <th className="p-2.5">Hints</th>
                <th className="p-2.5">Time</th>
                <th className="p-2.5 text-right">Action</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800 font-mono">
              {summary.recent_attempts.map((attempt) => (
                <tr key={attempt.id} className="hover:bg-slate-850/60 transition">
                  <td className="p-2.5 font-sans font-medium text-white">
                    {attempt.problem_title}
                  </td>
                  <td className="p-2.5">
                    {attempt.status === 'passed' ? (
                      <span className="inline-flex items-center gap-1 text-emerald-400 font-semibold">
                        <CheckCircle2 className="h-3.5 w-3.5" /> Passed
                      </span>
                    ) : attempt.status === 'wrong_answer' ? (
                      <span className="inline-flex items-center gap-1 text-amber-400 font-semibold">
                        <XCircle className="h-3.5 w-3.5" /> Wrong
                      </span>
                    ) : (
                      <span className="inline-flex items-center gap-1 text-rose-400 font-semibold">
                        <AlertTriangle className="h-3.5 w-3.5" /> Error
                      </span>
                    )}
                  </td>
                  <td className="p-2.5 text-slate-400">{attempt.bug_category || '-'}</td>
                  <td className="p-2.5 text-slate-400">
                    {attempt.passed_tests} / {attempt.total_tests}
                  </td>
                  <td className="p-2.5 text-slate-400">{attempt.hints_used}</td>
                  <td className="p-2.5 text-slate-500 font-sans">{attempt.timestamp}</td>
                  <td className="p-2.5 text-right">
                    <button
                      onClick={() => {
                        onSelectProblem(attempt.problem_id);
                        onReturnToWorkspace();
                      }}
                      className="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-indigo-300 font-sans text-xs transition"
                    >
                      Open
                    </button>
                  </td>
                </tr>
              ))}
              {summary.recent_attempts.length === 0 && (
                <tr>
                  <td colSpan={7} className="text-center py-6 text-slate-500 font-sans">
                    No attempts recorded yet. Start solving problems in the workspace!
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
};
