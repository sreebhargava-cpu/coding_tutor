import React, { useEffect, useState, useCallback } from 'react';
import { 
  ProblemSummary, 
  ProblemDetail, 
  ExecutionResult, 
  HintResponse,
  ExplainConceptResponse,
  CodeQualityResponse,
  EdgeCaseResponse,
  ExplainErrorResponse
} from './types';
import { 
  fetchProblems, 
  fetchProblemDetail, 
  requestSocraticHint, 
  requestExplainError,
  requestExplainConcept,
  requestCodeQuality,
  requestEdgeCases,
  recordAttempt,
  fetchProgressSummary
} from './services/apiService';
import { getPyodide, executeAndTestCode } from './services/pyodideService';
import { Navbar } from './components/Navbar';
import { ProblemDescription } from './components/ProblemDescription';
import { CodeEditor } from './components/CodeEditor';
import { ConsoleOutput } from './components/ConsoleOutput';
import { TutorPanel } from './components/TutorPanel';
import { ConceptModal } from './components/ConceptModal';
import { QualityFeedbackModal } from './components/QualityFeedbackModal';
import { EdgeCaseModal } from './components/EdgeCaseModal';
import { ExplainErrorModal } from './components/ExplainErrorModal';
import { Dashboard } from './components/Dashboard';

export function App() {
  const [problems, setProblems] = useState<ProblemSummary[]>([]);
  const [currentProblemId, setCurrentProblemId] = useState<string>('');
  const [currentProblem, setCurrentProblem] = useState<ProblemDetail | null>(null);
  const [loadingProblem, setLoadingProblem] = useState<boolean>(true);

  const [studentCode, setStudentCode] = useState<string>('');
  const [executionResult, setExecutionResult] = useState<ExecutionResult | null>(null);
  const [isRunning, setIsRunning] = useState<boolean>(false);
  const [isPyodideReady, setIsPyodideReady] = useState<boolean>(false);

  // Socratic Hint State
  const [hint, setHint] = useState<HintResponse | null>(null);
  const [hintLevel, setHintLevel] = useState<number>(1);
  const [previousHints, setPreviousHints] = useState<string[]>([]);
  const [hintsUsedCount, setHintsUsedCount] = useState<number>(0);
  const [loadingHint, setLoadingHint] = useState<boolean>(false);
  const [recurringWeaknesses, setRecurringWeaknesses] = useState<string[]>([]);

  // Navigation View
  const [activeView, setActiveView] = useState<'workspace' | 'dashboard'>('workspace');

  // Modals state
  const [conceptModalOpen, setConceptModalOpen] = useState<boolean>(false);
  const [conceptData, setConceptData] = useState<ExplainConceptResponse | null>(null);
  const [conceptLoading, setConceptLoading] = useState<boolean>(false);
  const [selectedConceptText, setSelectedConceptText] = useState<string>('');

  const [qualityModalOpen, setQualityModalOpen] = useState<boolean>(false);
  const [qualityData, setQualityData] = useState<CodeQualityResponse | null>(null);
  const [qualityLoading, setQualityLoading] = useState<boolean>(false);

  const [edgeCaseModalOpen, setEdgeCaseModalOpen] = useState<boolean>(false);
  const [edgeCaseData, setEdgeCaseData] = useState<EdgeCaseResponse | null>(null);
  const [edgeCaseLoading, setEdgeCaseLoading] = useState<boolean>(false);

  const [errorModalOpen, setErrorModalOpen] = useState<boolean>(false);
  const [errorData, setErrorData] = useState<ExplainErrorResponse | null>(null);
  const [errorLoading, setErrorLoading] = useState<boolean>(false);

  // Preload Pyodide
  useEffect(() => {
    getPyodide()
      .then(() => setIsPyodideReady(true))
      .catch((err) => console.error('Failed to preload Pyodide', err));
  }, []);

  // Fetch problem list on start
  const loadProblemList = useCallback(async () => {
    try {
      const list = await fetchProblems();
      setProblems(list);
      if (list.length > 0 && !currentProblemId) {
        setCurrentProblemId(list[0].id);
      }
    } catch (err) {
      console.error('Failed to load problem list', err);
    }
  }, [currentProblemId]);

  useEffect(() => {
    loadProblemList();
  }, [loadProblemList]);

  // Load selected problem detail
  useEffect(() => {
    if (!currentProblemId) return;

    let isMounted = true;
    setLoadingProblem(true);
    fetchProblemDetail(currentProblemId)
      .then((detail) => {
        if (!isMounted) return;
        setCurrentProblem(detail);
        setStudentCode(detail.starter_code);
        setExecutionResult(null);
        setHint(null);
        setHintLevel(1);
        setPreviousHints([]);
        setHintsUsedCount(0);
      })
      .catch((err) => console.error('Failed to load problem detail', err))
      .finally(() => {
        if (isMounted) setLoadingProblem(false);
      });

    return () => {
      isMounted = false;
    };
  }, [currentProblemId]);

  // Refresh weakness tracking on mount
  useEffect(() => {
    fetchProgressSummary()
      .then((summary) => setRecurringWeaknesses(summary.recurring_weaknesses))
      .catch((err) => console.error('Failed to fetch summary', err));
  }, []);

  // Run Code with Pyodide
  const handleRunCode = async () => {
    if (!currentProblem) return;
    setIsRunning(true);

    try {
      const res = await executeAndTestCode(
        studentCode,
        currentProblem.function_name,
        currentProblem.test_cases
      );
      setExecutionResult(res);

      // Record Attempt to Database
      const bugCategory = hint?.bug_category || (res.error_type ? 'runtime_error' : (res.status === 'wrong_answer' ? 'logical_error' : undefined));
      await recordAttempt(
        currentProblem.id,
        studentCode,
        res,
        bugCategory,
        hintsUsedCount
      );

      // Refresh problem list to show solved checkmark
      if (res.status === 'passed') {
        loadProblemList();
      }

      // Refresh weakness indicators
      fetchProgressSummary().then((s) => setRecurringWeaknesses(s.recurring_weaknesses));
    } catch (err) {
      console.error('Execution failed', err);
    } finally {
      setIsRunning(false);
    }
  };

  // Socratic Hint Progression
  const handleRequestHint = async (nextLevel: boolean = false) => {
    if (!currentProblem) return;

    const targetLevel = nextLevel ? Math.min(3, hintLevel + 1) : hintLevel;
    setLoadingHint(true);

    try {
      const hintRes = await requestSocraticHint(
        currentProblem.id,
        studentCode,
        executionResult,
        targetLevel,
        previousHints,
        1
      );

      setHint(hintRes);
      setHintLevel(targetLevel);
      setPreviousHints((prev) => [...prev, hintRes.socratic_question]);
      setHintsUsedCount((prev) => prev + 1);
    } catch (err) {
      console.error('Failed to request hint', err);
    } finally {
      setLoadingHint(false);
    }
  };

  // Explain Error Action
  const handleAskExplainError = async () => {
    if (!currentProblem || !executionResult?.error_type) return;
    setErrorLoading(true);
    setErrorModalOpen(true);

    try {
      const exp = await requestExplainError(
        currentProblem.id,
        studentCode,
        executionResult.error_type,
        executionResult.error_message || '',
        executionResult.error_line
      );
      setErrorData(exp);
    } catch (err) {
      console.error('Failed to explain error', err);
    } finally {
      setErrorLoading(false);
    }
  };

  // Explain Concept Action
  const handleExplainSelection = (text: string) => {
    setSelectedConceptText(text);
    setConceptModalOpen(true);
    handleSearchConcept(text);
  };

  const handleSearchConcept = async (conceptName: string) => {
    if (!currentProblem) return;
    setConceptLoading(true);
    try {
      const data = await requestExplainConcept(
        currentProblem.id,
        studentCode,
        conceptName,
        conceptName
      );
      setConceptData(data);
    } catch (err) {
      console.error('Failed to explain concept', err);
    } finally {
      setConceptLoading(false);
    }
  };

  // Code Quality Coach Action
  const handleOpenQualityModal = async () => {
    if (!currentProblem) return;
    setQualityModalOpen(true);
    setQualityLoading(true);
    try {
      const q = await requestCodeQuality(currentProblem.id, studentCode);
      setQualityData(q);
    } catch (err) {
      console.error('Failed to get quality feedback', err);
    } finally {
      setQualityLoading(false);
    }
  };

  // Edge-Case Coach Action
  const handleOpenEdgeCaseModal = async () => {
    if (!currentProblem) return;
    setEdgeCaseModalOpen(true);
    setEdgeCaseLoading(true);
    try {
      const ec = await requestEdgeCases(currentProblem.id, studentCode);
      setEdgeCaseData(ec);
    } catch (err) {
      console.error('Failed to get edge cases', err);
    } finally {
      setEdgeCaseLoading(false);
    }
  };

  const handleResetCode = () => {
    if (currentProblem && window.confirm('Reset editor to original starter code?')) {
      setStudentCode(currentProblem.starter_code);
      setExecutionResult(null);
    }
  };

  return (
    <div className="h-screen w-screen flex flex-col bg-slate-950 overflow-hidden font-sans select-none">
      {/* Top Navbar */}
      <Navbar
        problems={problems}
        currentProblemId={currentProblemId}
        onSelectProblem={(id) => setCurrentProblemId(id)}
        activeView={activeView}
        setActiveView={setActiveView}
        isPyodideReady={isPyodideReady}
      />

      {/* Main View Area */}
      <main className="flex-1 overflow-hidden relative">
        {activeView === 'dashboard' ? (
          <Dashboard
            onSelectProblem={(id) => {
              setCurrentProblemId(id);
              setActiveView('workspace');
            }}
            onReturnToWorkspace={() => setActiveView('workspace')}
          />
        ) : (
          <div className="h-full grid grid-cols-12 divide-x divide-slate-800">
            {/* Left Column: Problem Statement & Objectives (3 cols) */}
            <div className="col-span-3 h-full overflow-hidden bg-slate-900/60">
              <ProblemDescription problem={currentProblem} loading={loadingProblem} />
            </div>

            {/* Middle Column: Monaco Code Editor & Console Output (6 cols) */}
            <div className="col-span-6 h-full flex flex-col overflow-hidden">
              {/* Code Editor (60% height) */}
              <div className="h-[62%]">
                <CodeEditor
                  code={studentCode}
                  onChange={(val) => setStudentCode(val)}
                  onRun={handleRunCode}
                  onReset={handleResetCode}
                  isRunning={isRunning}
                  onExplainSelection={handleExplainSelection}
                />
              </div>

              {/* Console & Test Case Output (38% height) */}
              <div className="h-[38%] border-t border-slate-800">
                <ConsoleOutput
                  result={executionResult}
                  isRunning={isRunning}
                  onAskExplainError={handleAskExplainError}
                />
              </div>
            </div>

            {/* Right Column: AI Socratic Tutor Mentor Panel (3 cols) */}
            <div className="col-span-3 h-full overflow-hidden">
              <TutorPanel
                hint={hint}
                loadingHint={loadingHint}
                onRequestHint={handleRequestHint}
                onRequestExplainError={handleAskExplainError}
                onOpenConceptModal={() => setConceptModalOpen(true)}
                onOpenQualityModal={handleOpenQualityModal}
                onOpenEdgeCaseModal={handleOpenEdgeCaseModal}
                executionResult={executionResult}
                recurringWeaknesses={recurringWeaknesses}
              />
            </div>
          </div>
        )}
      </main>

      {/* Interactive Modals */}
      <ConceptModal
        isOpen={conceptModalOpen}
        onClose={() => setConceptModalOpen(false)}
        conceptData={conceptData}
        loading={conceptLoading}
        onSearchConcept={handleSearchConcept}
        initialSelection={selectedConceptText}
      />

      <QualityFeedbackModal
        isOpen={qualityModalOpen}
        onClose={() => setQualityModalOpen(false)}
        data={qualityData}
        loading={qualityLoading}
      />

      <EdgeCaseModal
        isOpen={edgeCaseModalOpen}
        onClose={() => setEdgeCaseModalOpen(false)}
        data={edgeCaseData}
        loading={edgeCaseLoading}
      />

      <ExplainErrorModal
        isOpen={errorModalOpen}
        onClose={() => setErrorModalOpen(false)}
        data={errorData}
        loading={errorLoading}
      />
    </div>
  );
}

export default App;
