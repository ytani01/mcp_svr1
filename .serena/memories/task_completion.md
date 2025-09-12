# Task Completion Guidelines

When a task is completed, the following steps should be performed:
1.  Run linting: `uv run ruff check src/ tests/`
2.  Run type checking: `uv run mypy src/ tests/` and `uv run pyright src/ tests/`
3.  Run tests: `uv run python -m pytest -v`
4.  Update `Tasks.md` to mark the completed task.
