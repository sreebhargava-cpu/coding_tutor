import React, { useRef, useState } from 'react';
import Editor, { OnMount } from '@monaco-editor/react';
import { Play, RotateCcw, Copy, Check, HelpCircle, Terminal, FlaskConical } from 'lucide-react';

interface CodeEditorProps {
  code: string;
  onChange: (value: string) => void;
  onRun: () => void;
  onRunWithInput: (input: string) => void;
  onReset: () => void;
  isRunning: boolean;
  onExplainSelection: (selectedText: string) => void;
}

export const CodeEditor: React.FC<CodeEditorProps> = ({
  code,
  onChange,
  onRun,
  onRunWithInput,
  onReset,
  isRunning,
  onExplainSelection,
}) => {
  const editorRef = useRef<any>(null);
  const [selectedText, setSelectedText] = useState<string>('');
  const [copied, setCopied] = useState<boolean>(false);
  const [isScriptMode, setIsScriptMode] = useState<boolean>(false);
  const [programInput, setProgramInput] = useState<string>('');

  const handleEditorDidMount: OnMount = (editor, monaco) => {
    editorRef.current = editor;

    // Listen to selection changes
    editor.onDidChangeCursorSelection((e) => {
      const selection = editor.getModel()?.getValueInRange(e.selection);
      if (selection && selection.trim().length > 1) {
        setSelectedText(selection.trim());
      } else {
        setSelectedText('');
      }
    });

    // Add Ctrl+Enter shortcut to run code (mode-aware)
    editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, () => {
      if (isScriptMode) {
        onRunWithInput(programInput);
      } else {
        onRun();
      }
    });
  };

  // Keep the Ctrl+Enter handler up-to-date when mode/input changes
  // by storing the latest values in a ref used by the Monaco command
  const isScriptModeRef = useRef(isScriptMode);
  const programInputRef = useRef(programInput);
  isScriptModeRef.current = isScriptMode;
  programInputRef.current = programInput;

  const handleCopy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="h-full flex flex-col bg-slate-900 border-l border-r border-slate-800">
      {/* Editor Header Toolbar */}
      <div className="bg-slate-850 px-4 py-2 border-b border-slate-800 flex items-center justify-between text-xs">
        <div className="flex items-center space-x-2">
          <span className="font-mono text-slate-300 font-medium">solution.py</span>
          <span className="text-[11px] text-slate-500 font-mono">Python 3.14 (Pyodide)</span>
        </div>

        <div className="flex items-center space-x-2">
          {/* Explain selected code action */}
          {selectedText && (
            <button
              onClick={() => onExplainSelection(selectedText)}
              className="flex items-center space-x-1.5 px-2.5 py-1 rounded-md bg-indigo-500/20 text-indigo-300 hover:bg-indigo-500/30 border border-indigo-500/40 font-medium transition animate-fadeIn"
              title="Ask AI Tutor to explain selected code concept"
            >
              <HelpCircle className="h-3.5 w-3.5" />
              <span>Explain "{selectedText.length > 16 ? selectedText.slice(0, 14) + '...' : selectedText}"</span>
            </button>
          )}

          {/* Copy Button */}
          <button
            onClick={handleCopy}
            className="p-1.5 text-slate-400 hover:text-slate-200 hover:bg-slate-800 rounded transition"
            title="Copy code to clipboard"
          >
            {copied ? <Check className="h-3.5 w-3.5 text-emerald-400" /> : <Copy className="h-3.5 w-3.5" />}
          </button>

          {/* Reset Button */}
          <button
            onClick={onReset}
            className="p-1.5 text-slate-400 hover:text-slate-200 hover:bg-slate-800 rounded transition"
            title="Reset to starter template"
          >
            <RotateCcw className="h-3.5 w-3.5" />
          </button>

          {/* Mode toggle: Run & Test vs Run Script */}
          <div className="flex items-center bg-slate-800/80 border border-slate-700 rounded-lg overflow-hidden">
            <button
              onClick={() => setIsScriptMode(false)}
              className={`flex items-center space-x-1 px-2.5 py-1.5 text-xs font-semibold transition ${
                !isScriptMode
                  ? 'bg-indigo-600 text-white'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
              title="Run & Test mode: tests against predefined test cases"
            >
              <FlaskConical className="h-3 w-3" />
              <span>Run &amp; Test</span>
            </button>
            <button
              onClick={() => setIsScriptMode(true)}
              className={`flex items-center space-x-1 px-2.5 py-1.5 text-xs font-semibold transition ${
                isScriptMode
                  ? 'bg-emerald-600 text-white'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
              title="Run Script mode: execute as a script with custom input()"
            >
              <Terminal className="h-3 w-3" />
              <span>Run Script</span>
            </button>
          </div>

          {/* Run Button — adapts to mode */}
          {!isScriptMode ? (
            <button
              onClick={onRun}
              disabled={isRunning}
              className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg font-semibold shadow transition ${
                isRunning
                  ? 'bg-indigo-700/60 text-indigo-200 cursor-not-allowed'
                  : 'bg-indigo-600 hover:bg-indigo-500 text-white shadow-indigo-600/30'
              }`}
            >
              <Play className={`h-3.5 w-3.5 ${isRunning ? 'animate-spin' : 'fill-white'}`} />
              <span>{isRunning ? 'Executing...' : 'Run Code'}</span>
              <kbd className="hidden sm:inline-block ml-1 text-[10px] bg-indigo-800/80 px-1.5 py-0.5 rounded text-indigo-200">
                Ctrl+Enter
              </kbd>
            </button>
          ) : (
            <button
              onClick={() => onRunWithInput(programInput)}
              disabled={isRunning}
              className={`flex items-center space-x-1.5 px-3 py-1.5 rounded-lg font-semibold shadow transition ${
                isRunning
                  ? 'bg-emerald-700/60 text-emerald-200 cursor-not-allowed'
                  : 'bg-emerald-600 hover:bg-emerald-500 text-white shadow-emerald-600/30'
              }`}
            >
              <Play className={`h-3.5 w-3.5 ${isRunning ? 'animate-spin' : 'fill-white'}`} />
              <span>{isRunning ? 'Executing...' : '▶ Run Script'}</span>
              <kbd className="hidden sm:inline-block ml-1 text-[10px] bg-emerald-800/80 px-1.5 py-0.5 rounded text-emerald-200">
                Ctrl+Enter
              </kbd>
            </button>
          )}
        </div>
      </div>

      {/* Script Mode Banner */}
      {isScriptMode && (
        <div className="px-4 py-1.5 bg-emerald-950/40 border-b border-emerald-800/40 flex items-center gap-2 text-[11px] text-emerald-300">
          <Terminal className="h-3.5 w-3.5 shrink-0" />
          <span className="font-semibold">Script Mode:</span>
          <span className="text-emerald-400/80">Input lines below feed to <code className="font-mono bg-emerald-900/40 px-1 rounded">input()</code> calls in order.</span>
        </div>
      )}

      {/* Monaco Editor Container */}
      <div className="flex-1 overflow-hidden relative">
        <Editor
          height="100%"
          defaultLanguage="python"
          language="python"
          theme="vs-dark"
          value={code}
          onChange={(val) => onChange(val || '')}
          onMount={handleEditorDidMount}
          options={{
            minimap: { enabled: false },
            fontSize: 13,
            lineNumbers: 'on',
            scrollBeyondLastLine: false,
            automaticLayout: true,
            tabSize: 4,
            insertSpaces: true,
            fontFamily: "'Fira Code', 'Courier New', monospace",
            formatOnType: true,
            padding: { top: 12, bottom: 12 },
          }}
        />
      </div>

      {/* Program Input Textarea — only shown in script mode */}
      {isScriptMode && (
        <div className="border-t border-slate-800 bg-slate-900/80 px-4 py-3 flex flex-col gap-1.5">
          <label className="text-[11px] font-semibold text-slate-400 font-mono">
            Program Input <span className="text-slate-500 font-normal">(one line per <code className="bg-slate-800 px-1 rounded">input()</code> call)</span>
          </label>
          <textarea
            value={programInput}
            onChange={(e) => setProgramInput(e.target.value)}
            rows={3}
            placeholder={"e.g.\nAlice\n25"}
            spellCheck={false}
            className="w-full resize-none rounded-md bg-slate-950 border border-slate-700 text-slate-200 font-mono text-xs px-3 py-2 focus:outline-none focus:ring-1 focus:ring-emerald-500/60 focus:border-emerald-600/60 placeholder-slate-600"
          />
        </div>
      )}
    </div>
  );
};
