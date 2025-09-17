import pytest
import asyncio
import asyncio.subprocess as asp

@pytest.mark.asyncio
async def test_capture_async_subprocess_stderr():
    # 意図的に存在しないコマンドを実行して、stderrにエラーを出力させる
    proc = await asp.create_subprocess_exec(
        'nonexistent-command',  # 存在しないコマンド
        stdout=asp.PIPE,
        stderr=asp.PIPE
    )

    # communicate()を使って、サブプロセスとの通信と終了を待つ
    # これにより、stdoutとstderrの出力をまとめて取得できる
    stdout_bytes, stderr_bytes = await proc.communicate()
    
    # 出力はバイト列なので、デコードして文字列に変換する
    stderr_output = stderr_bytes.decode()
    
    # 意図したエラーメッセージがstderrに含まれていることを確認
    # OSによってメッセージが異なるため、両方をチェック
    assert "command not found" in stderr_output or "No such file or directory" in stderr_output
    
    # プロセスが正常終了していないことを確認
    assert proc.returncode != 0
