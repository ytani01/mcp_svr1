# Plan for CLI Client Tool

## 1. CLIフレームワークの選択
- **Click**: 既存のプロジェクト依存関係と人気度からClickを選択。

## 2. CLIコマンドの設計
- **MCPサーバーへの接続方法**:
  - `--server`オプションでURL（リモートサーバー）またはファイルパス（ローカルインメモリサーバー）を指定可能にする。
  - `--server`が指定されない場合、デフォルトでローカルインメモリサーバーに接続する。
- **ツールの呼び出し方法**:
  - `call`サブコマンドを使用。
  - ツール名は必須引数とする。
  - ツールの引数は`--key value`形式で渡す。
- **リソースの読み取り方法**:
  - `read`サブコマンドを使用。
  - リソースURIは必須引数とする。
- **ツール/リソースの一覧表示方法**:
  - `list`サブコマンドを使用。
  - `list`の下に`tools`と`resources`サブコマンドを設ける。

## 3. クライアントコードの構造化
- **メインCLIエントリーポイント**:
  - `src/mcp_client/cli.py`をメインエントリーポイントとする。
  - `click.group()`でメインコマンドを、`main.command()`で`call`, `read`, `list`などのサブコマンドを定義する。
- **FastMCPサーバーへの接続処理**:
  - `src/mcp_client/utils.py`にヘルパー関数を作成し、`--server`オプションに基づいて`fastmcp.client.Client`インスタンスを生成・返却する。
  - この関数は、ローカルインメモリサーバーまたはリモートサーバーへの接続を処理する。
- **コマンド実装**:
  - 各サブコマンド（`call`, `read`, `list tools`, `list resources`）は、`src/mcp_client/cli.py`内の独自の関数として実装する。
  - これらの関数は、ヘルパー関数を使用してクライアントインスタンスを取得し、適切な`client`メソッド（`call_tool`, `read_resource`, `list_tools`, `list_resources`）を呼び出す。
- **エラーハンドリング**:
  - `try...except`ブロックを使用して`fastmcp.exceptions.ToolError`やその他の潜在的な例外を捕捉する。
  - ユーザーフレンドリーなエラーメッセージを出力する。

## 4. 既存コードとの統合

### 4.1. プロジェクト構造
- クライアントコードは`src/mcp_client/`ディレクトリに配置する。

### 4.2. 依存関係
- `click`と`fastmcp`は`pyproject.toml`に既に存在するため、追加の依存関係は不要。

### 4.3. エントリーポイント
- `pyproject.toml`に`mcp_client = "mcp_client.cli:main"`というエントリーポイントを追加し、CLIクライアントを`mcp_client`コマンドで呼び出せるようにする。

### 4.4. `pyproject.toml`の更新
- `[project.scripts]`セクションに`mcp_client`のエントリーポイントを追加する。
- `[tool.hatch.build.targets.sdist.exclude]`に`src/mcp_client`を追加しないように注意する。
