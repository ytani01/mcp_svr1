# CLIの使用方法

このドキュメントでは、`mcp_svr1` CLI ツールを使用する方法について説明します。

## 基本的な使用方法

`mcp_svr1` ツールは、MCP サーバーの起動と、サーバーと対話するためのクライアント機能を提供します。

### `server` サブコマンド

MCP サーバーを起動します。

```bash
uv run mcp_svr1 server
```

### `client` サブコマンド

MCP サーバーと対話するためのクライアント機能を提供します。

#### `call` サブコマンド

MCP サーバー上のツールを呼び出すために使用します。

```bash
uv run mcp_svr1 client call <TOOL_NAME> [ARGS...]
```

ツールの引数は `key=value` 形式で指定する必要があります。

**例:**

`add` ツールを引数 `a=1` および `b=2` で呼び出します。

```bash
uv run mcp_svr1 client call add a=1 b=2
```

`subtract` ツールを引数 `a=5` および `b=2` で呼び出します。

```bash
uv run mcp_svr1 client call subtract a=5 b=2
```

#### `read` サブコマンド

MCP サーバーからリソースを読み取るために使用します。

```bash
uv run mcp_svr1 client read <RESOURCE_URI>
```

**例:**

サーバーバージョンリソースを読み取ります。

```bash
uv run mcp_svr1 client read server://version
```

#### `list` サブコマンド

利用可能なツールまたはリソースを一覧表示するためのサブコマンドを提供します。

##### `list tools`

MCP サーバー上の利用可能なすべてのツールを一覧表示します。

```bash
uv run mcp_svr1 client list tools
```

##### `list resources`

MCP サーバー上の利用可能なすべてのリソースを一覧表示します。

```bash
uv run mcp_svr1 client list resources
```
