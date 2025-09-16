# Project Overview

This is a Python project for an MCP (Model Context Protocol) server using FastMCP. It is intended to be used as a template or sample.

## Tech Stack

- Python 3.13+
- `uv` for project and dependency management.
- `FastMCP` for the MCP server implementation.
- `click` and `asyncclick` for the CLI.
- `pytest` for testing.
- `ruff`, `mypy`, `pyright` for linting and type checking.

## Codebase Structure

- `src/mcp_svr1/`: Main package directory.
    - `__main__.py`: Main entry point for the CLI.
    - `core.py`: Core logic of the MCP server.
    - `cli/`: CLI implementation using Click.
    - `tools/`: Implementation of the tools exposed by the MCP server.
    - `utils/`: Utility modules.
