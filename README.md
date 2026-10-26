# AI-Powered Adaptive Coding Tutor

An intelligent, interactive coding tutor designed to help students learn programming through guided Socratic discovery rather than direct answers.

## Architecture & Features

* **In-Browser Python Execution**: Powered by Pyodide (WebAssembly) capturing stdout, stderr, exception types, and execution time.
* **Monaco Editor Workspace**: Professional code editing with syntax highlighting, line numbers, and keyboard shortcuts (`Ctrl+Enter` to run).
* **Curriculum System**: Predefined Python problems spanning Variables, Conditions, Loops, Strings, Lists & Indexing, Dictionaries, Functions, and Data Structures.
* **Socratic Debugging & 3-Level Hints**:
  * **Level 1 (Conceptual)**: Broad question provoking thoughts about the underlying principle.
  * **Level 2 (Directional)**: Focused clue pointing toward where the discrepancy originates.
  * **Level 3 (Specific)**: Targeted insight comparing expected vs actual state without giving away the direct code.
* **Plain-English Error Explanations**: Contextual translations of technical tracebacks (`IndexError`, `TypeError`, `KeyError`, `ZeroDivisionError`).
* **Concept Explanations in Context**: Highlight any code snippet in the editor and click "Explain" for an instant contextual breakdown and mini-example.
* **Code Quality Coaching**: Evaluates working code for readability, nesting, variable naming, and idiomatic Python practices with a score out of 100.
* **Edge-Case Challenges**: Once basic tests pass, students are challenged with boundary inputs (empty lists, duplicates, negative numbers).
* **Progress Dashboard**: Interactive Recharts analytics tracking problem completion, recurring weaknesses, and personal recommendations.

---

## Quick Start Guide

### 1. Unified Full-Stack Launch (Recommended)
You can run the entire application (Backend API + Built React UI) with a single command:

```powershell
python backend/run.py
```
Open your browser and navigate to:
**http://localhost:8000**

---

### 2. Dual-Server Development Mode

#### Start Backend:
```powershell
cd backend
python run.py
```
*(Backend runs on `http://localhost:8000`)*

#### Start Frontend Dev Server:
```powershell
cd frontend
npm run dev
```
*(Frontend runs on `http://localhost:3000` with hot-module reloading and proxying to `/api`)*

---

### Configuration (Optional Gemini API Key)
The tutor includes an intelligent contextual fallback engine that works offline. To enable live Gemini API generation, create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
GEMINI_MODEL=gemini-2.5-flash
```

---

### Running Automated Test Suite
To verify all backend endpoints, Socratic hint progressions, error explanations, and progress metrics:

```powershell
python backend/tests/test_api.py
```
