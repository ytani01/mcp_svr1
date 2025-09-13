# Project Overview

This is a Python project for an MCP (Model Context Protocol) server using the FastMCP library. It is intended to be used as a template or sample project.

## Tech Stack

- Python 3.13+
- FastMCP: For creating the MCP server.
- `uv`: For project and dependency management.
- `hatch`: For building and versioning.
- `pytest`: For testing.
- `ruff`, `mypy`, `pyright`: For linting and type checking.

## Codebase Structure

- `src/mcp_svr1`: The main MCP server implementation.
  - `__main__.py`: The entry point for the server.
  - `tools/`: Contains the tools that the MCP server exposes (e.g., `add`, `echo`, `subtract`, `version`).
- `src/mcp_client`: A command-line client for the MCP server.
- `tests/`: Contains tests for the project.
