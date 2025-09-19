# `uv run mcp_svr1 client call add a=1 b=2` コマンドを
# `--debug` オプションなしで実行し、標準エラー出力をキャプチャ。
# `FASTMCP_LOG_LEVEL=CRITICAL` 環境変数を設定し、デバッグ出力を無効化し、
# 特定のデバッグメッセージが含まれないことをアサートする。
import os
import subprocess


def test_debug_option_disabled():
    command = ["uv", "run", "mcp_svr1", "client", "call", "add",
               "a=1", "b=2"]

    # FASTMCP_LOG_LEVEL を CRITICAL に設定
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        env=dict(os.environ, FASTMCP_LOG_LEVEL='CRITICAL')
    )

    assert result.returncode == 0
    # デバッグメッセージが含まれないことをアサート
    assert "add: a=1, b=2" not in result.stderr
