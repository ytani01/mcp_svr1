# Suggested Commands

This document outlines essential commands for developing and interacting with the `mcp_svr1` project.

## Project Setup and Dependencies
- **Install `uv` (if not already installed):**
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **Create/Update Virtual Environment:**
  ```bash
  uv venv
  ```
- **Install Project in Editable Mode:**
  ```bash
  uv pip install -e .
  ```
- **Add a new dependency:**
  ```bash
  uv add <package-name>
  ```

## Running the MCP Server
- **Start the MCP Server (for Gemini CLI integration):**
  ```bash
  uv run mcp_svr1 server
  ```

## Development and Quality Assurance
- **Run Ruff Linter:**
  ```bash
  uv run ruff check src/
  ```
- **Run MyPy Type Checker:**
  ```bash
  uv run mypy src/
  ```
- **Run Pyright Type Checker:**
  ```bash
  uv run pyright src/
  ```
- **Run Pytest (all tests):**
  ```bash
  uv run python -m pytest -v tests/
  ```
- **Run a specific test file (e.g., `test_01.py`):**
  ```bash
  uv run python -m pytest -v tests/test_01.py
  ```

## Task Management
- **Rename and Archive `Tasks.md` (after completion):**
  ```bash
  uv run rename_task.py
  ```

## Git Commands
- **Check Git Status:**
  ```bash
  git status
  ```
- **Review Changes:**
  ```bash
  git diff HEAD
  ```
- **Review Staged Changes:**
  ```bash
  git diff --staged
  ```
- **View Recent Commits:**
  ```bash
  git log -n 3
  ```

## General Linux Utility Commands
- `ls`: List directory contents.
- `cd`: Change directory.
- `grep`: Search for patterns in files.
- `find`: Search for files in a directory hierarchy.
- `cat`, `less`, `more`: View file contents.
- `head`, `tail`: View beginning/end of files.
- `cp`, `mv`, `rm`: Copy, move, remove files/directories.
