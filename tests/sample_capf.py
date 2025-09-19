# `pytest` の `capfd` フィクスチャ使用例。関数が標準出力と標準エラー出力に
# 書き込む内容をキャプチャし、それらの出力が期待通りかをアサートするテスト。
import sys


def function_outputting_stderr():
    """標準エラー出力に文字列を出力する関数"""
    sys.stderr.write("これは標準エラー出力です。")
    print("これは標準出力です。")  # 標準出力にも出力する例


def test_stderr_output(capfd):
    """標準エラー出力をテストする関数"""
    function_outputting_stderr()
    out, err = capfd.readouterr()

    # 標準エラー出力の内容が期待通りかアサートする
    assert "これは標準エラー出力です。" in err
    # 標準出力の内容も一緒に確認できる
    assert "これは標準出力です。" in out
