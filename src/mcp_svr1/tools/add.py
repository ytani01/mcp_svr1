from mcp.server.fastmcp import FastMCP


def register_add_tool(mcp: FastMCP):
    # @mcp.tool() デコレータは、関数をFastMCPツールとして登録します。
    # 関数名がツール名、型ヒントがインターフェースを定義します。
    @mcp.tool()
    def add(a: int, b: int) -> int:
        """Adds two numbers.

        Args:
            a: 最初の数値。
            b: 2番目の数値。
        """
        return a + b