import asyncio
import os
import tempfile

import pytest


@pytest.mark.asyncio
async def test_debug_diagnostic():
    with tempfile.NamedTemporaryFile(
        mode='w+', encoding='utf-8', delete=False) as stderr_file:
        log_file_path = stderr_file.name
        command = ["uv", "run", "mcp_svr1", "--debug", "client", "call",
                   "add", "a=1", "b=2"]
        process = await asyncio.create_subprocess_exec(
            *command,
            stdout=asyncio.subprocess.PIPE,
            stderr=stderr_file.fileno(),
            env=dict(os.environ, FASTMCP_LOG_LEVEL='DEBUG')
        )
        await process.wait()

    with open(log_file_path, 'r', encoding='utf-8') as f:
        stderr_output = f.read()
    os.remove(log_file_path)

    print(f"Captured stderr:\n{stderr_output}")  # Manual inspection
    assert "add: a=1, b=2" in stderr_output
