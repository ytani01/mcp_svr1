# Suggested Commands

Here are some important commands for developing in this project:

- **Run the MCP server:**
  ```bash
  uv run mcp_svr1
  ```

- **Run the MCP client:**
  ```bash
  uv run mcp_client
  ```

- **Run tests:**
  ```bash
  uv run python -m pytest -v
  ```

- **Run linting and type checking:**
  ```bash
  uv run ruff check .
  uv run mypy .
  uv run pyright
  ```

- **Install new dependencies:**
  ```bash
  uv add <library-name>
  ```
