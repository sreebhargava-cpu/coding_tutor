import React from 'react';
import { ProblemSummary } from '../types';
import { 
  Sparkles, 
  Terminal, 
  BarChart3, 
  CheckCircle2, 
  Layers, 
  Bot, 
  Cpu
} from 'lucide-react';

interface NavbarProps {
  problems: ProblemSummary[];
  currentProblemId: string;
  onSelectProblem: (id: string) => void;
  activeView: 'workspace' | 'dashboard';
  setActiveView: (view: 'workspace' | 'dashboard') => void;
  isPyodideReady: boolean;
}

export const Navbar: React.FC<NavbarProps> = ({
  problems,
  currentProblemId,
  onSelectProblem,
  activeView,
  setActiveView,
  isPyodideReady,
}) => {
  const currentProblem = problems.find((p) => p.id === currentProblemId);

  return (
    <header className="bg-slate-900/90 backdrop-blur border-b border-slate-800 px-4 py-2.5 flex items-center justify-between z-20">
      {/* Brand & Title */}
      <div className="flex items-center space-x-3">
        <div className="h-9 w-9 rounded-lg bg-gradient-to-tr from-indigo-600 to-violet-500 flex items-center justify-center shadow-lg shadow-indigo-500/20">
          <Sparkles className="h-5 w-5 text-white" />
        </div>
        <div>
          <div className="flex items-center space-x-2">
            <h1 className="text-base font-bold text-white tracking-tight">Adaptive Coding Tutor</h1>
            <span className="text-xs px-2 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 font-medium border border-indigo-500/20">
              Socratic AI
            </span>
          </div>
          <p className="text-[11px] text-slate-400">Contextual mentorship for Python programmers</p>
        </div>
      </div>

      {/* Problem Selector Dropdown */}
      <div className="flex items-center space-x-2">
        <label className="text-xs text-slate-400 flex items-center gap-1.5 font-medium">
          <Layers className="h-3.5 w-3.5 text-slate-500" /> Problem:
        </label>
        <select
          value={currentProblemId}
          onChange={(e) => onSelectProblem(e.target.value)}
          className="bg-slate-800 hover:bg-slate-750 text-slate-200 text-xs rounded-lg border border-slate-700 px-3 py-1.5 font-medium focus:ring-2 focus:ring-indigo-500 outline-none transition"
        >
          {problems.map((p) => (
            <option key={p.id} value={p.id}>
              {p.is_solved ? '✓ ' : ''}{p.title} ({p.difficulty})
            </option>
          ))}
        </select>
        {currentProblem?.is_solved && (
          <span className="flex items-center gap-1 text-[11px] text-emerald-400 bg-emerald-500/10 border border-emerald-500/20 px-2 py-0.5 rounded-full font-medium">
            <CheckCircle2 className="h-3 w-3" /> Solved
          </span>
        )}
      </div>

      {/* Navigation Tabs & Statuses */}
      <div className="flex items-center space-x-3">
        {/* Pyodide status */}
        <div className="flex items-center space-x-1.5 px-2.5 py-1 rounded-md bg-slate-800/80 border border-slate-700/60 text-[11px]">
          <Cpu className={`h-3.5 w-3.5 ${isPyodideReady ? 'text-emerald-400' : 'text-amber-400 animate-pulse'}`} />
          <span className="text-slate-300 font-mono">
            {isPyodideReady ? 'Pyodide Wasm' : 'Loading Python...'}
          </span>
        </div>

        {/* AI Tutor status */}
        <div className="flex items-center space-x-1.5 px-2.5 py-1 rounded-md bg-indigo-950/60 border border-indigo-800/40 text-[11px]">
          <Bot className="h-3.5 w-3.5 text-indigo-400" />
          <span className="text-indigo-200 font-medium">AI Socratic Mentor</span>
        </div>

        {/* View Switcher Tabs */}
        <div className="flex items-center bg-slate-800 p-0.5 rounded-lg border border-slate-700">
          <button
            onClick={() => setActiveView('workspace')}
            className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-md text-xs font-medium transition ${
              activeView === 'workspace'
                ? 'bg-indigo-600 text-white shadow-sm'
                : 'text-slate-300 hover:text-white'
            }`}
          >
            <Terminal className="h-3.5 w-3.5" />
            <span>Workspace</span>
          </button>
          <button
            onClick={() => setActiveView('dashboard')}
            className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-md text-xs font-medium transition ${
              activeView === 'dashboard'
                ? 'bg-indigo-600 text-white shadow-sm'
                : 'text-slate-300 hover:text-white'
            }`}
          >
            <BarChart3 className="h-3.5 w-3.5" />
            <span>Progress</span>
          </button>
        </div>
      </div>
    </header>
  );
};
