# Project Overview

This project implements an MCP (Multi-Agent Communication Protocol) server and a client.

## Purpose
The primary purpose of this project is to provide an MCP server that exposes various tools, and a client to interact with these tools. It also serves as a demonstration and development environment for interacting with GeminiCLI, with a strong emphasis on the importance of Japanese docstrings for effective tool selection by GeminiCLI.

## Tech Stack
- **Language:** Python
- **Framework:** serena MCP
- **Dependency Management/Runner:** uv
- **Testing:** pytest
- **Linting:** ruff

## Codebase Structure
- `.serena/`: GeminiCLI memory files and project configuration.
- `archives/`: Historical task-related markdown files.
- `src/`: Main application source code.
    - `src/mcp_client/`: MCP client implementation.
        - `cli.py`: Command-line interface for the client.
        - `utils.py`: Client utility functions.
    - `src/mcp_svr1/`: MCP server implementation.
        - `__main__.py`: Server entry point.
        - `tools/`: Directory containing individual MCP tools (e.g., `add`, `subtract`, `echo`, `version`).
        - `utils/`: Server utility functions (e.g., `my_logger.py`).
- `docs/`: Project documentation (e.g., `CLI.md`).
- `tests/`: Unit and integration tests for the project.
- `pyproject.toml`: Project configuration for `uv`, `pytest`, `ruff`.
- `uv.lock`: Dependency lock file.
- `.python-version`: Specifies the Python version used.
- `GEMINI.md`: Guidelines for GeminiCLI interaction, emphasizing docstring importance.
