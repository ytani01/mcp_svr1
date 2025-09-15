# Task Completion Checklist

When a task is completed, the following steps should generally be performed:

1.  **Coding:** Ensure all code changes are implemented according to the task requirements and project conventions.
2.  **Testing:** Run relevant unit and integration tests (`uv run pytest tests/`) to ensure no regressions were introduced and new features work as expected. Write new tests if necessary to cover new functionality.
3.  **Debugging:** Address any bugs or issues identified during testing or code review.
4.  **Linting:** Run linting checks (`ruff check src/`) to ensure code adheres to style guidelines.
5.  **Documentation:** Update any relevant documentation (e.g., `docs/`, docstrings) to reflect changes.
6.  **Review:** (If applicable) Prepare changes for code review.
7.  **Commit:** Commit changes with a clear and concise commit message.
