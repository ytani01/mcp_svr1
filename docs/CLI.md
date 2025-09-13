# CLI クライアントの使用方法

このドキュメントでは、`mcp_client` CLI ツールを使用する方法について説明します。

## インストール

`mcp_client` CLI ツールをインストールするには、`uv` がインストールされていることを確認し、次のコマンドを実行します。

```bash
uv install
```

## 基本的な使用方法

`mcp_client` ツールは、MCP サーバーと対話するためのいくつかのサブコマンドを提供します。

### `call` サブコマンド

MCP サーバー上のツールを呼び出すために使用します。

```bash
uv run mcp_client call <TOOL_NAME> [ARGS...]
```

ツールの引数は `key=value` 形式で指定する必要があります。

**例:**

`add` ツールを引数 `a=1` および `b=2` で呼び出します。

```bash
uv run mcp_client call add a=1 b=2
```

`subtract` ツールを引数 `a=5` および `b=2` で呼び出します。

```bash
uv run mcp_client call subtract a=5 b=2
```

### `read` サブコマンド

MCP サーバーからリソースを読み取るために使用します。

```bash
uv run mcp_client read <RESOURCE_URI>
```

**例:**

サーバーバージョンリソースを読み取ります。

```bash
uv run mcp_client read server://version
```

### `list` サブコマンド

利用可能なツールまたはリソースを一覧表示するためのサブコマンドを提供します。

#### `list tools`

MCP サーバー上の利用可能なすべてのツールを一覧表示します。

```bash
uv run mcp_client list tools
```

#### `list resources`

MCP サーバー上の利用可能なすべてのリソースを一覧表示します。

```bash
uv run mcp_client list resources
```

## シェルモード

`mcp_client` はインタラクティブなシェルモードも提供します。

```bash
uv run mcp_client shell
```

シェル内では、`mcp_client` プレフィックスなしで `call`、`read`、`list` コマンドを直接使用できます。

**例 (シェル内):**

```
mcp > call add a=1 b=2
mcp > read server://version
mcp > list tools
```