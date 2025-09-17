# デバッグ方針検討プラン

## 1. 目的

*   `--debug` および `-d` オプションが `mcp_svr1` のツールでデバッグロギングを正しく有効にすることを自動テストで検証する。
*   `my_logger.py` は変更しない。
*   `FastMCP` の `INFO` ログは無視する。

## 2. 問題の再確認

*   手動実行では `DEBUG` ログが `stderr` に出力されるが、`pytest` 環境でのサブプロセスからの `stderr` キャプチャが不安定。

## 3. テスト戦略

*   **コアアプローチ:** `tempfile.NamedTemporaryFile` を使用してサブプロセスの `stderr` をファイルにリダイレクトし、そのファイルの内容を読み取ってアサーションを行う。
*   **`FastMCP` ログの制御:** `FASTMCP_LOG_LEVEL` 環境変数を使用して `FastMCP` のログレベルを調整し、`DEBUG` ログの分離を容易にする。
*   **テストの焦点:** `mcp_svr1` のツールからの特定のデバッグメッセージ（「add: a=1, b=2」）の有無のみをアサートする。ツールの機能的な出力は `tests/test_03.py` でカバーされているため、重複は避ける。

## 4. アクションプラン

*   **テストファイルの作成と修正:**
    *   `tests/test_04_debug_option_disabled.py` を作成し、デバッグオプションなしのシナリオをテストする。
    *   `tests/test_05_debug_option_enabled.py` を作成し、デバッグオプションありのシナリオ（`--debug` と `-d`）をテストする。
    *   各テストファイル内で、`tempfile.NamedTemporaryFile` を使用して一時ファイルを作成し、その `fileno()` を `asyncio.create_subprocess_exec` の `stderr` 引数に渡す。
    *   `asyncio.create_subprocess_exec` の `env` 引数で `FASTMCP_LOG_LEVEL` 環境変数を適切に設定する（`CRITICAL` または `DEBUG`）。
    *   サブプロセス終了後、一時ファイルを読み込み、その内容に対してデバッグメッセージの有無をアサートする。

*   **`tests/test_03.py` との重複について:**
    *   `tests/test_04_debug_option_disabled.py` および `tests/test_05_debug_option_enabled.py` は、デバッグオプションのロギング動作に特化するため、`tests/test_03.py` で既にカバーされているツールの機能的な出力に関するアサーションは削除します。

## 5. 厳格な制約

*   このプランがうまくいかなくても、「正常な実行のみをチェックする」プランに変更することは禁止します。デバッグログの存在をアサートするテストを成功させることにコミットします。
