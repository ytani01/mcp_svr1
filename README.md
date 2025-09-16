# mcp_svr1

**FastMCP**を使用した **MCPサーバー** の Pythonプロジェクトです。
テンプレートやサンプルとして使うことを目的としてます。

## == インストール

### === ``uv``のインストール

``uv``は、Pythonのプロジェクト管理やバージョン管理のツールです。
MCPサーバーの実行にも使います。

参考: [uv 公式ドキュメント](https://docs.astral.sh/uv/getting-started/installation/)

``` bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### === MCPサーバーのインストール

適切なディレクトリに ``git clone`` してください。

ここでは、ホームディレクト下の`work`ディレクトリ (`$HOME/work`)を想定してます。

``` bash
cd ~
mkdir work
cd work
git clone https://github.com/ytani01/mcp_svr1
cd mcp_svr1
uv venv
# venv の activate は不要です！
uv pip install -e .   # 一応
```


## == Gemini CLIでの利用

### === Gemini CLIの設定例

* ~/.gemini/settings.json
``` ini
{
  "mcpServers": {
    "mcp_svr1": {
      "command": "uv",
      "args": [
        "run",
        "mcp_svr1",
        "server"
      ],
      "cwd": "$HOME/work/mcp_svr1"
    }
  },
  "selectedAuthType": "oauth-personal",
  "theme": "Ayu"
}
```


### === MCPサーバーがGemini CLIに認識されていることの確認


``` text
> /mcp list


Configured MCP servers:

  🟢 mcp_svr1 - Ready (4 tools)
    Tools:
    - add
    - echo
    - subtract
    - version
```


### === **Gemini CLI** での呼び出し方法

**注意**

- このツールが呼び出されるかどうかは、Gemini CLI の判断に依存します。
- モデルの種類や他のMCPサーバなど、様々な条件で、呼び出されないことがあります。


👉 `Gemini CLI`のバージョンではなく、`mcp_svr1`のバージョンを答えるようになります。
``` text
> バージョンは？

 ╭─
 │ ?  version (mcp_svr1 MCP Server) {} ←
 │
 │   MCP Server: mcp_svr1
 │   Tool: version
 │
 │ Allow execution of MCP tool "version" from server "mcp_svr1"?
 │
 │ ● 1. Yes, allow once
 │   2. Yes, always allow tool "version" from server "mcp_svr1"
 │   3. Yes, always allow all tools from server "mcp_svr1"
 │   4. No, suggest changes (esc)
 ╰
 ✦ mcp_svr1 0.0.4
```


👉 Gemini CLI が、プロンプトの内容を解釈して、ツールを選んで実行します。
``` text
> add 8 + 2

:

 ✦ 10
```

``` text
> ８と２を足して

:

 ✦ 10
```

``` text
> 8に2を加えるとどうなるかな？

:

✦ 10になります。
```


## == サーバーテスト用 CLI

[CLIの使用方法](docs/CLI.md)


## == 参考情報

- [github: FastMCP](https://github.com/jlowin/fastmcp)
- [github: Gemini CLI](https://github.com/google-gemini/gemini-cli)
