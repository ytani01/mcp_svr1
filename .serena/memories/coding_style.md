# Coding Style and Conventions

## General Rules
- Chat in Japanese.
- Research thoroughly before experimenting.
- `git commit` is user-only. Propose short, single-line English commit messages.
- `uv` and `pyproject.toml` for project configuration and management, adhering to the latest `uv` specifications.
- Use `uv run ...` for command execution.
- Do not explicitly activate `venv`.
- Use `uv add ...` for library installation/addition, not `pip install ...`.
- Reliable file updates: create new files and replace old ones.

## Code Specifics
- Source code comments in Japanese.
- Each line within 78 characters.
- Use `my_logger.py`'s `get_logger()` for debug logs.
- Do not modify `my_logger.py`.

## Learning and Debugging Principles
- Prioritize official documentation.
- Verify all assumptions.
- Systematic problem isolation.
- Utilize detailed logging.
- Respect user feedback.
