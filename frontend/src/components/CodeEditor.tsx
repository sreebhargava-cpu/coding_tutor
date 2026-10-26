import React, { useRef, useState } from 'react';
import Editor, { OnMount } from '@monaco-editor/react';
import { Play, RotateCcw, Copy, Check, HelpCircle } from 'lucide-react';

interface CodeEditorProps {
  code: string;
  onChange: (value: string) => void;
  onRun: () => void;
  onReset: () => void;
  isRunning: boolean;
  onExplainSelection: (selectedText: string) => void;
}

export const CodeEditor: React.FC<CodeEditorProps> = ({
  code,
  onChange,
  onRun,
  onReset,
  isRunning,
  onExplainSelection,
}) => {
  const editorRef = useRef<any>(null);
  const [selectedText, setSelectedText] = useState<string>('');
  const [copied, setCopied] = useState<boolean>(false);

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

    // Add Ctrl+Enter shortcut to run code
    editor.addCommand(monaco.KeyMod.CtrlCmd | monaco.KeyCode.Enter, () => {
      onRun();
    });
  };

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

          {/* Run & Grade Button */}
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
        </div>
      </div>

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
    </div>
  );
};
