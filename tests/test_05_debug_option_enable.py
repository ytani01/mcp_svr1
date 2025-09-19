# `uv run mcp_svr1 --debug client call add a=1 b=2` コマンドを
# 非同期で実行し、標準エラー出力を一時ファイルにリダイレクトして、
# デバッグログに特定のメッセージ（`add: a=1, b=2`）が含まれることをテスト。
import subprocess

import pytest


@pytest.mark.asyncio
async def test_debug_diagnostic():
    """debug option test."""

    cmdline = "uv run mcp_svr1 --debug client call add a=1 b=2"
    print()
    print()
    print(f"* cmdline = {cmdline}")

    result = subprocess.run(cmdline.split(), capture_output=True, text=True)

    print()
    print(f"* stdout\n{result.stdout}")
    print(f"* stderr\n{result.stderr}")
    print(f"* returncode = {result.returncode}")
    print()

    assert result.returncode == 0
    assert "add: a=1, b=2" in result.stderr
