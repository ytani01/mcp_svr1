# Suggested Commands

## Project Management
- `uv install`: Install dependencies.
- `uv run <command>`: Run a command in the project's virtual environment.
- `uv add`: add python packages

## Linting
- `ruff check src/`: Run linting checks on the `src` directory.

## Testing
- `uv run pytest tests/`: Run all unit and integration tests.

## Running Entrypoints
- **MCP Server:** `uv run python src/mcp_svr1`
- **MCP Client CLI:** `uv run python src/mcp_client/cli.py`

## General Utilities
- `git status`: Check the status of the Git repository.
- `git add .`: Stage all changes.
- `git commit -m "<message>"`: Commit staged changes.
- `ls -F`: List files and directories.
- `cd <directory>`: Change directory.
- `grep <pattern> <files>`: Search for patterns in files.
- `find . -name "<pattern>"`: Find files by name.
