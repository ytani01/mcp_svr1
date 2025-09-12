# Coding Style and Conventions

## General Rules
- Comments in source code are generally in Japanese.
- Each line should be within 78 characters.
- Use `get_logger()` from `my_logger.py` for debug logs.
- Do not modify `my_logger.py`.

## Project-wide Rules (from GEMINI.md)
- Conduct thorough research before experimenting.
- `git commit` is performed only by the user. The AI should prompt the user to commit with a short, one-line English commit message.
- Project configuration and management are done via `uv` and `pyproject.toml`, adhering to the latest `uv` specifications.
- Always use `uv run ...` for command execution; do not explicitly activate `venv`.
- Install/add libraries using `uv add ...`; do not use `pip install ...`.
- File updates should be reliable, preferably by creating new files and replacing old ones.

## Learning and Debugging Principles
- Prioritize official documentation for core features, configuration, and authentication.
- Validate all assumptions (naming, implicit behavior, default values).
- Systematically isolate problems by testing each component.
- Utilize detailed logging and debugging options.
- Respect user feedback for continuous learning and problem diagnosis.
