import subprocess

# テストしたいコマンド
command = ["your_command", "arg1", "arg2"]  # 実際のコマンドに置き換え

# サブプロセスの stderr をキャプチャする
result = subprocess.run(
    command,
    capture_output=True,  # 標準出力と標準エラー出力をキャプチャする
    text=True,            # 出力を文字列として扱う
    check=True            # エラー終了時に例外を発生させる
)

# キャプチャされた stderr を確認する
stderr_output = result.stderr
print(f"stderr出力: {stderr_output}")

# pytest のテスト内でアサーションを使用する
# stderr に特定のエラーメッセージが含まれているか確認するなど
assert "エラーメッセージ" in stderr_output
