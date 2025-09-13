# Task Completion

When you have completed a task, you should always perform the following steps:

1.  **Run linting and type checking** to ensure the code is clean and correct:
    ```bash
    uv run ruff check .
    uv run mypy .
    uv run pyright
    ```

2.  **Run tests** to ensure that your changes have not broken anything:
    ```bash
    uv run python -m pytest -v
    ```

3.  If all checks and tests pass, **propose a commit message** to the user. The user is responsible for the final commit.
