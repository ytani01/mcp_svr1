import sys

def function_outputting_stderr():
    """標準エラー出力に文字列を出力する関数"""
    sys.stderr.write("これは標準エラー出力です。\n")
    print("これは標準出力です。") # 標準出力にも出力する例

def test_stderr_output(capfd):
    """標準エラー出力をテストする関数"""
    function_outputting_stderr()
    out, err = capfd.readouterr()

    # 標準エラー出力の内容が期待通りかアサートする
    assert err == "これは標準エラー出力です。\n"
    # 標準出力の内容も一緒に確認できる
    assert out == "これは標準出力です。\n"
