#
# (c) 2025 Yoichi Tanibayashi
#
"""
FastMCPサーバーのメインエントリーポイント。

このファイルは、FastMCPサーバーを初期化し、
ツールとリソースを登録してサーバーを実行します。
テンプレートとして、新しいツールやリソースを追加する際の参考にしてください。
"""
from mcp.server.fastmcp import FastMCP

from .tools.add import register_add_tool
from .tools.echo import register_echo_tool
from .tools.subtract import register_subtract_tool
from .tools.version import register_version_resource

# FastMCPサーバーインスタンスを初期化します。
# サーバー名はプロジェクト名と一致させるのが一般的です。
mcp = FastMCP("mcp_svr1")

# 各ツールとリソースをFastMCPサーバーに登録します。
# 新しいツールやリソースを作成した場合は、ここに登録関数を追加してください。
register_add_tool(mcp)
register_subtract_tool(mcp)
register_version_resource(mcp)
register_echo_tool(mcp)


def main():
    """
    MCPサーバーを起動します。
    transport="stdio" は標準入出力を使用することを示します。
    """
    # transport="stdio" は標準入出力を使用することを示します。
    # 他のトランスポートオプション（例: "tcp"）も利用可能です。
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()