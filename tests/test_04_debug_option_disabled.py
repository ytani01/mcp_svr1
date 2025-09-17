import pytest
import subprocess
import asyncio
import tempfile
import os

@pytest.mark.asyncio
async def test_debug_option_disabled():
    # --debug オプションなしで実行し、デバッグログが出力されないことを確認
    with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8', delete=False) as stderr_file_no_debug:
        log_file_no_debug_path = stderr_file_no_debug.name
        command_no_debug = ["uv", "run", "mcp_svr1", "client", "call", "add", "a=1", "b=2"]
        process_no_debug = await asyncio.create_subprocess_exec(
            *command_no_debug,
            stdout=asyncio.subprocess.PIPE,
            stderr=stderr_file_no_debug.fileno(),
            env=dict(os.environ, FASTMCP_LOG_LEVEL='CRITICAL') # Suppress FastMCP INFO logs
        )
        await process_no_debug.wait()

    with open(log_file_no_debug_path, 'r', encoding='utf-8') as f:
        stderr_no_debug_str = f.read()
    os.remove(log_file_no_debug_path)
    assert "add: a=1, b=2" not in stderr_no_debug_str
