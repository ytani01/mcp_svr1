import pytest
import subprocess
import asyncio
import tempfile
import os

@pytest.mark.asyncio
async def test_debug_option_enabled():
    # --debug オプションありで実行し、デバッグログが出力されることを確認
    with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8', delete=False) as stderr_file_with_debug:
        log_file_with_debug_path = stderr_file_with_debug.name
        command_with_debug = ["uv", "run", "mcp_svr1", "--debug", "client", "call", "add", "a=1", "b=2"]
        process_with_debug = await asyncio.create_subprocess_exec(
            *command_with_debug,
            stdout=asyncio.subprocess.PIPE,
            stderr=stderr_file_with_debug.fileno(),
            env=dict(os.environ, FASTMCP_LOG_LEVEL='DEBUG') # Enable FastMCP DEBUG logs
        )
        await process_with_debug.wait()

    with open(log_file_with_debug_path, 'r', encoding='utf-8') as f:
        stderr_with_debug_str = f.read()
    os.remove(log_file_with_debug_path)
    assert "add: a=1, b=2" in stderr_with_debug_str

    # -d オプションありで実行し、デバッグログが出力されることを確認
    with tempfile.NamedTemporaryFile(mode='w+', encoding='utf-8', delete=False) as stderr_file_with_short_debug:
        log_file_with_short_debug_path = stderr_file_with_short_debug.name
        command_with_short_debug = ["uv", "run", "mcp_svr1", "-d", "client", "call", "add", "a=1", "b=2"]
        process_with_short_debug = await asyncio.create_subprocess_exec(
            *command_with_short_debug,
            stdout=asyncio.subprocess.PIPE,
            stderr=stderr_file_with_short_debug.fileno(),
            env=dict(os.environ, FASTMCP_LOG_LEVEL='DEBUG') # Enable FastMCP DEBUG logs
        )
        await process_with_short_debug.wait()

    with open(log_file_with_short_debug_path, 'r', encoding='utf-8') as f:
        stderr_with_short_debug_str = f.read()
    os.remove(log_file_with_short_debug_path)
    assert "add: a=1, b=2" in stderr_with_short_debug_str
