# Task Completion Guidelines

## When a Task is Completed
- After modifying source code, always run linting and testing.
  - Linting: `uv run ruff check ...`, `uv run mypy ...`, `uv run pyright ...`
  - Testing: `uv run python -m pytest -v ...`
- If all tasks in `Tasks.md` are completed:
  1. Report completion to the user.
  2. Prompt the user to update `ToDo.md`.
  3. Run `uv run rename_task.py` to rename `Tasks.md` and move it to the `archives` directory.
