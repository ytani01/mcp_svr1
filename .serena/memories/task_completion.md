# Task Completion Workflow

When a task is completed, the following steps should be performed:

1.  **Linting:**
    -   `uv run ruff check .`
    -   `uv run mypy .`
    -   `uv run pyright .`
2.  **Testing:**
    -   `uv run python -m pytest -v ...` (run all relevant tests)
3.  **Update `Tasks.md`:**
    -   Mark the completed task as `[x]` in `Tasks.md`.
4.  **Archive `Tasks.md` (if all tasks are complete):**
    -   Report completion to the user.
    -   Prompt the user to update `ToDo.md`.
    -   Run `uv run rename_task.py` to rename and archive `Tasks.md`.