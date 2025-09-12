# Task Completion Guidelines

When a task item in `Tasks.md` is completed:

1.  **Mark as complete**: Mark the task item in `Tasks.md` as complete.
2.  **Code Modification Follow-up**: If source code was modified, always perform the following:
    - Run linting (`uv run ruff check ...`, `uv run mypy ...`, `uv run pyright ...`).
    - Create, update, and run test programs (`uv run python -m pytest -v ...`).
3.  **Commit**: Prompt the user to commit the changes with a short, one-line English commit message.
4.  **`Tasks.md` Completion**: If all tasks in `Tasks.md` are completed:
    - Report completion to the user.
    - Prompt the user to update `ToDo.md`.
    - Run `uv run rename_task.py` to rename `Tasks.md` to `yyyymmdd-HHMM-Tasks-done.md` and move it to the `archives` directory.
