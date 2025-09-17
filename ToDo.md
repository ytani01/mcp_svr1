# ToDo.md

## 2025-09-17a

  - [x] @Plan_1_Logging.md に基づいて、やるべきタスクのチェックリストを作り、 @Tasks.mdを作成する。まだ実行してはならない。
  - [x] @Tasks2.md を修正して、@Tasks.mdにリネームした。'Tasks.md'を再確認して事項する。
  - [x] 'uv run mcp_svr1 client ...'の動作を確認して、バグを修正する。
  - [x] '--debug'の他に、短縮形の'-d'も使えるようにする。
  - [x] デバッグオプションは、サブコマンドでも使えるようにする。

## 2025-09-17b
  - [x] Plan.mdを元に、デバッグオプションをdisableにしたときの出力がただし事をテストするプログラム'tests/test_04_debug_option_disabled.py'を作成し、テストを通す.
  - [x] Plan.mdと、'tests/test_sample_of_05_debug_option_enable.py'を参考に、デバッグオプションをONにしたときの出力がただし事をテストするプログラム'tests/test_05_debug_option_enable.py'を作成し、テストを通す.
  - [x] リンティングを実行し、再テスト.

  - [x] すべてのサブコマンドでデバッグオプションを指定できるようにする。
  - [x] 'src/mcp_svr1/utils/utils/click_utils.py'を利用して、オプションの処理を整理する。
  - [ ] 'src/mcp_svr1/utils/utils/click_utils.py'を上手に利用して、すべてのレベルのすべてのサブコマンドでデバッグオプションを指定できるようにする。
  - [ ] 今後のデバッグや、動作確認のため、デバッグメッセージを埋め込むべき場所を特定して埋め込む。
  - [ ] 'tests/test_05...'を修正して、追加したデバッグメッセージをテストできるようにする。






