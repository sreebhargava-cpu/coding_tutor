import React, { useState } from 'react';
import { ProblemSummary } from '../types';
import { generateCustomProblem, saveCustomProblem, deleteCustomProblem } from '../services/apiService';
import {
  Search,
  BarChart3,
  ArrowRight,
  CheckCircle2,
  Sparkles,
  Play,
  PlusCircle,
  Trash2,
  AlertCircle,
  RefreshCw,
  X
} from 'lucide-react';

interface HomePageProps {
  problems: ProblemSummary[];
  onStartProblem: (id: string) => void;
  onGoToAnalytics: () => void;
  onRefreshProblems?: () => void;
  lastProblemId: string | null;
  lastProblemCode: string | null;
}

const difficultyLabel = (d: string) => {
  if (d === 'Beginner') return 'Easy';
  if (d === 'Intermediate') return 'Medium';
  if (d === 'Advanced') return 'Hard';
  return d;
};

const difficultyColor = (d: string) => {
  const label = difficultyLabel(d);
  if (label === 'Easy') return 'text-emerald-400 bg-emerald-500/10 border-emerald-500/20';
  if (label === 'Medium') return 'text-amber-400 bg-amber-500/10 border-amber-500/20';
  if (label === 'Hard') return 'text-rose-400 bg-rose-500/10 border-rose-500/20';
  return 'text-indigo-400 bg-indigo-500/10 border-indigo-500/20';
};

type DifficultyFilter = 'All' | 'Easy' | 'Medium' | 'Hard' | 'Custom';

export const HomePage: React.FC<HomePageProps> = ({
  problems,
  onStartProblem,
  onGoToAnalytics,
  onRefreshProblems,
  lastProblemId,
}) => {
  const [search, setSearch] = useState('');
  const [difficultyFilter, setDifficultyFilter] = useState<DifficultyFilter>('All');

  // Custom problem modal & preview state
  const [customModalOpen, setCustomModalOpen] = useState(false);
  const [customPrompt, setCustomPrompt] = useState('');
  const [customLoading, setCustomLoading] = useState(false);
  const [customError, setCustomError] = useState<string | null>(null);
  const [previewProblem, setPreviewProblem] = useState<any | null>(null);
  const [savingCustom, setSavingCustom] = useState(false);

  const lastProblem = lastProblemId ? problems.find((p) => p.id === lastProblemId) : null;

  const filteredProblems = problems.filter((p) => {
    const matchesSearch = p.title.toLowerCase().includes(search.toLowerCase());
    const label = difficultyLabel(p.difficulty);
    const isCustom = !p.is_preset;

    let matchesDifficulty = true;
    if (difficultyFilter === 'Custom') {
      matchesDifficulty = isCustom;
    } else if (difficultyFilter !== 'All') {
      matchesDifficulty = label === difficultyFilter;
    }

    return matchesSearch && matchesDifficulty;
  });

  const filterTabs: DifficultyFilter[] = ['All', 'Easy', 'Medium', 'Hard', 'Custom'];

  const handleGenerateCustom = async () => {
    if (!customPrompt.trim()) return;
    setCustomLoading(true);
    setCustomError(null);
    setPreviewProblem(null);
    try {
      const generated = await generateCustomProblem(customPrompt);
      setPreviewProblem(generated);
    } catch (err: any) {
      setCustomError(err.message || 'Custom problem generation failed. Please ensure Gemini API is configured.');
    } finally {
      setCustomLoading(false);
    }
  };

  const handleSaveCustom = async () => {
    if (!previewProblem) return;
    setSavingCustom(true);
    try {
      const res = await saveCustomProblem(previewProblem);
      if (onRefreshProblems) onRefreshProblems();
      setCustomModalOpen(false);
      setPreviewProblem(null);
      setCustomPrompt('');
      onStartProblem(res.id);
    } catch (err: any) {
      setCustomError(err.message || 'Failed to save problem.');
    } finally {
      setSavingCustom(false);
    }
  };

  const handleDeleteProblem = async (e: React.MouseEvent, problem: ProblemSummary) => {
    e.stopPropagation();
    if (problem.is_preset) {
      alert('Preset curriculum problems cannot be deleted.');
      return;
    }

    const confirmed = window.confirm(
      `Delete custom problem "${problem.title}"?\n\nWarning: This will permanently delete the problem definition and all ${problem.attempt_count} associated coding attempt records.`
    );
    if (!confirmed) return;

    try {
      await deleteCustomProblem(problem.id);
      if (onRefreshProblems) onRefreshProblems();
    } catch (err: any) {
      alert(`Error deleting problem: ${err.message}`);
    }
  };

  return (
    <div className="h-full overflow-y-auto bg-slate-950 text-slate-200">
      <div className="max-w-6xl mx-auto px-6 py-8 space-y-10">

        {/* ── Hero Section ── */}
        <section className="text-center space-y-4 pt-4">
          <div className="flex items-center justify-center gap-3 mb-2">
            <div className="h-12 w-12 rounded-2xl bg-gradient-to-tr from-indigo-600 to-violet-500 flex items-center justify-center shadow-lg shadow-indigo-500/30">
              <Sparkles className="h-6 w-6 text-white" />
            </div>
          </div>
          <h1 className="text-4xl font-extrabold text-white tracking-tight">
            AI-Powered Adaptive Coding Tutor
          </h1>
          <p className="text-slate-400 text-lg max-w-2xl mx-auto leading-relaxed">
            Learn Python through Socratic questioning. Get personalized hints, concept explanations,
            and real-time feedback — without being handed the answer.
          </p>

          <div className="flex items-center justify-center gap-4 pt-2 flex-wrap">
            <div className="px-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-sm">
              <span className="text-indigo-400 font-bold">{problems.length}</span>{' '}
              <span className="text-slate-400">Curated &amp; Custom Problems</span>
            </div>
            <div className="px-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-sm">
              <span className="text-emerald-400 font-bold">Pyodide Wasm</span>{' '}
              <span className="text-slate-400">Browser Execution</span>
            </div>
            <div className="px-4 py-2 rounded-xl bg-slate-900 border border-slate-800 text-sm">
              <span className="text-violet-400 font-bold">3-Tier Hints</span>{' '}
              <span className="text-slate-400">Socratic Mentoring</span>
            </div>
          </div>
        </section>

        {/* ── Continue Last Problem ── */}
        <section>
          {lastProblem ? (
            <div className="p-6 rounded-2xl bg-gradient-to-r from-indigo-950/60 via-slate-900 to-slate-900 border border-indigo-800/40 shadow-xl flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
              <div className="space-y-1.5">
                <div className="flex items-center gap-2">
                  <span className="text-xs font-semibold uppercase tracking-wider text-indigo-400">
                    Continue Last Problem
                  </span>
                  {lastProblem.is_solved && (
                    <span className="flex items-center gap-1 text-[11px] text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-2 py-0.5 rounded-full font-medium">
                      <CheckCircle2 className="h-3 w-3" /> Solved
                    </span>
                  )}
                </div>
                <h2 className="text-xl font-bold text-white">{lastProblem.title}</h2>
                <div className="flex items-center gap-2 text-xs text-slate-400 flex-wrap">
                  <span
                    className={`px-2 py-0.5 rounded-full border font-medium ${difficultyColor(lastProblem.difficulty)}`}
                  >
                    {difficultyLabel(lastProblem.difficulty)}
                  </span>
                  <span>•</span>
                  <span>{lastProblem.category}</span>
                  {lastProblem.attempt_count > 0 && (
                    <>
                      <span>•</span>
                      <span>{lastProblem.attempt_count} attempts</span>
                    </>
                  )}
                </div>
              </div>
              <button
                onClick={() => onStartProblem(lastProblem.id)}
                className="shrink-0 flex items-center gap-2 px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm shadow-lg shadow-indigo-600/30 transition"
              >
                <Play className="h-4 w-4 fill-white" />
                Resume Coding
                <ArrowRight className="h-4 w-4" />
              </button>
            </div>
          ) : (
            <div className="p-6 rounded-2xl bg-slate-900 border border-slate-800 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
              <div className="space-y-1">
                <span className="text-xs font-semibold uppercase tracking-wider text-indigo-400">
                  Ready to Start?
                </span>
                <h2 className="text-xl font-bold text-white">Start your first Python challenge</h2>
                <p className="text-xs text-slate-400">
                  Select any problem from the library below or generate a custom AI challenge.
                </p>
              </div>
              {problems.length > 0 && (
                <button
                  onClick={() => onStartProblem(problems[0].id)}
                  className="shrink-0 flex items-center gap-2 px-5 py-2.5 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-semibold text-sm shadow-lg shadow-indigo-600/30 transition"
                >
                  <Play className="h-4 w-4 fill-white" />
                  Start Problem 1
                  <ArrowRight className="h-4 w-4" />
                </button>
              )}
            </div>
          )}
        </section>

        {/* ── Problem Library ── */}
        <section className="space-y-5">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h2 className="text-2xl font-bold text-white tracking-tight">Problem Library</h2>
              <p className="text-xs text-slate-400 mt-0.5">
                30 curated curriculum challenges and your custom generated problems
              </p>
            </div>

            {/* Generate Custom Challenge Button */}
            <button
              onClick={() => setCustomModalOpen(true)}
              className="flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-indigo-600/20 hover:bg-indigo-600/30 text-indigo-300 border border-indigo-500/40 text-xs font-semibold transition"
            >
              <PlusCircle className="h-4 w-4 text-indigo-400" />
              <span>Create Custom Challenge</span>
            </button>
          </div>

          {/* Search & Difficulty Filter Toolbar */}
          <div className="flex flex-col sm:flex-row gap-3 items-stretch sm:items-center justify-between">
            <div className="relative flex-1 max-w-sm">
              <Search className="absolute left-3 top-2.5 h-4 w-4 text-slate-500" />
              <input
                type="text"
                placeholder="Search problems by title..."
                value={search}
                onChange={(e) => setSearch(e.target.value)}
                className="w-full pl-9 pr-4 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 transition"
              />
            </div>

            <div className="flex items-center gap-1.5 bg-slate-900 p-1 rounded-xl border border-slate-800 self-start sm:self-auto flex-wrap">
              {filterTabs.map((tab) => (
                <button
                  key={tab}
                  onClick={() => setDifficultyFilter(tab)}
                  className={`px-3 py-1.5 rounded-lg text-xs font-medium transition ${
                    difficultyFilter === tab
                      ? 'bg-indigo-600 text-white shadow-sm'
                      : 'text-slate-400 hover:text-slate-200'
                  }`}
                >
                  {tab}
                </button>
              ))}
            </div>
          </div>

          {/* Problem Cards Grid */}
          {filteredProblems.length === 0 ? (
            <div className="text-center py-16 text-slate-500">
              No problems match your current search and filters.
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
              {filteredProblems.map((problem) => (
                <div
                  key={problem.id}
                  onClick={() => onStartProblem(problem.id)}
                  className="group relative cursor-pointer text-left rounded-xl bg-slate-900/70 border border-slate-800 hover:border-indigo-500/50 hover:bg-slate-900 p-4 space-y-3 transition-all duration-150 hover:shadow-lg hover:shadow-indigo-500/5"
                >
                  <div className="flex items-start justify-between gap-2">
                    <h3 className="font-semibold text-slate-100 group-hover:text-white text-sm leading-snug">
                      {problem.title}
                    </h3>
                    <div className="flex items-center gap-1.5 shrink-0 mt-0.5">
                      {problem.is_solved && (
                        <CheckCircle2 className="h-4 w-4 text-emerald-400" />
                      )}
                      {!problem.is_preset && (
                        <button
                          onClick={(e) => handleDeleteProblem(e, problem)}
                          className="opacity-0 group-hover:opacity-100 p-1 text-slate-400 hover:text-rose-400 hover:bg-slate-800 rounded transition"
                          title="Delete custom problem"
                        >
                          <Trash2 className="h-3.5 w-3.5" />
                        </button>
                      )}
                    </div>
                  </div>

                  <div className="flex items-center gap-2 flex-wrap">
                    <span
                      className={`text-xs px-2 py-0.5 rounded-full border font-medium ${difficultyColor(problem.difficulty)}`}
                    >
                      {difficultyLabel(problem.difficulty)}
                    </span>
                    <span className="text-xs px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 border border-slate-700 font-mono">
                      {problem.category}
                    </span>
                    {!problem.is_preset && (
                      <span className="text-[10px] px-2 py-0.5 rounded-full bg-violet-500/10 text-violet-400 border border-violet-500/20 font-medium">
                        Custom AI
                      </span>
                    )}
                  </div>

                  <div className="flex items-center justify-between text-[11px] text-slate-500 pt-1">
                    <span>
                      {problem.attempt_count > 0
                        ? `${problem.attempt_count} attempt${problem.attempt_count !== 1 ? 's' : ''}`
                        : 'Unattempted'}
                    </span>
                    <span className="text-indigo-400 font-medium opacity-0 group-hover:opacity-100 transition flex items-center gap-0.5">
                      Open <ArrowRight className="h-3 w-3" />
                    </span>
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>

        {/* Footer analytics CTA */}
        <section className="pb-4">
          <button
            onClick={onGoToAnalytics}
            className="w-full flex items-center justify-center gap-2 py-3 rounded-xl border border-slate-800 text-slate-400 hover:text-white hover:border-slate-700 hover:bg-slate-900/40 transition text-sm font-medium"
          >
            <BarChart3 className="h-4 w-4" />
            View your full progress analytics
            <ArrowRight className="h-4 w-4" />
          </button>
        </section>
      </div>

      {/* ── Custom Problem Generator Modal ── */}
      {customModalOpen && (
        <div className="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-2xl max-h-[90vh] flex flex-col shadow-2xl overflow-hidden animate-fadeIn">
            <div className="p-4 border-b border-slate-800 flex items-center justify-between">
              <div className="flex items-center gap-2">
                <Sparkles className="h-5 w-5 text-indigo-400" />
                <h3 className="text-base font-bold text-white">Create Custom Python Challenge</h3>
              </div>
              <button
                onClick={() => setCustomModalOpen(false)}
                className="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition"
              >
                <X className="h-5 w-5" />
              </button>
            </div>

            <div className="p-6 overflow-y-auto space-y-4 flex-1">
              {!previewProblem ? (
                <>
                  <p className="text-xs text-slate-400">
                    Describe any algorithm, problem, or topic you'd like to practice in Python.
                    Gemini will generate starter code, valid test cases, and progressive hints.
                  </p>
                  <textarea
                    rows={4}
                    value={customPrompt}
                    onChange={(e) => setCustomPrompt(e.target.value)}
                    placeholder="e.g. Write a function that checks if two strings are isomorphic, with boundary test cases..."
                    className="w-full p-3 rounded-xl bg-slate-950 border border-slate-800 text-xs text-slate-200 placeholder-slate-600 focus:outline-none focus:ring-2 focus:ring-indigo-500 font-sans resize-none"
                  />

                  {customError && (
                    <div className="p-3 rounded-xl bg-rose-950/40 border border-rose-800/50 flex items-start gap-2.5 text-xs text-rose-300">
                      <AlertCircle className="h-4 w-4 shrink-0 mt-0.5 text-rose-400" />
                      <span>{customError}</span>
                    </div>
                  )}

                  <div className="flex justify-end pt-2">
                    <button
                      onClick={handleGenerateCustom}
                      disabled={customLoading || !customPrompt.trim()}
                      className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-semibold shadow transition ${
                        customLoading || !customPrompt.trim()
                          ? 'bg-slate-800 text-slate-500 cursor-not-allowed'
                          : 'bg-indigo-600 hover:bg-indigo-500 text-white shadow-indigo-600/30'
                      }`}
                    >
                      {customLoading ? (
                        <>
                          <RefreshCw className="h-4 w-4 animate-spin" />
                          <span>Generating Challenge...</span>
                        </>
                      ) : (
                        <>
                          <Sparkles className="h-4 w-4" />
                          <span>Generate Challenge</span>
                        </>
                      )}
                    </button>
                  </div>
                </>
              ) : (
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <span className="text-xs font-semibold text-emerald-400">Preview Challenge</span>
                    <button
                      onClick={handleGenerateCustom}
                      disabled={customLoading}
                      className="text-xs text-slate-400 hover:text-white flex items-center gap-1"
                    >
                      <RefreshCw className={`h-3 w-3 ${customLoading ? 'animate-spin' : ''}`} />
                      Regenerate
                    </button>
                  </div>

                  <div className="p-4 rounded-xl bg-slate-950 border border-slate-800 space-y-2">
                    <h4 className="text-base font-bold text-white">{previewProblem.title}</h4>
                    <div className="flex gap-2">
                      <span className="text-xs px-2 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 font-medium">
                        {previewProblem.difficulty}
                      </span>
                      <span className="text-xs px-2 py-0.5 rounded-full bg-slate-800 text-slate-300 border border-slate-700 font-mono">
                        {previewProblem.category}
                      </span>
                    </div>
                    <p className="text-xs text-slate-300 whitespace-pre-line pt-2">
                      {previewProblem.description}
                    </p>
                    <div className="pt-2">
                      <span className="text-[11px] font-semibold text-slate-500 uppercase tracking-wide block mb-1">
                        Starter Code
                      </span>
                      <pre className="p-2.5 rounded bg-slate-900 border border-slate-800 font-mono text-xs text-indigo-300 overflow-x-auto">
                        {previewProblem.starter_code}
                      </pre>
                    </div>
                  </div>

                  <div className="flex justify-end gap-2 pt-2">
                    <button
                      onClick={() => setPreviewProblem(null)}
                      className="px-3.5 py-2 rounded-xl text-xs font-medium text-slate-400 hover:text-white hover:bg-slate-800 transition"
                    >
                      Back to Prompt
                    </button>
                    <button
                      onClick={handleSaveCustom}
                      disabled={savingCustom}
                      className="flex items-center gap-1.5 px-4 py-2 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold shadow transition"
                    >
                      {savingCustom ? 'Saving...' : 'Save & Open Challenge'}
                    </button>
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default HomePage;
