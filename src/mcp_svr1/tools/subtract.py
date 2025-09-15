from mcp.server.fastmcp import FastMCP


def register_subtract_tool(mcp: FastMCP):
    # @mcp.tool() デコレータは、関数をFastMCPツールとして登録します。
    # 関数名がツール名、型ヒントがインターフェースを定義します。
    @mcp.tool()
    def subtract(a: int, b: int) -> int:
        """Subtracts two numbers.

        Args:
            a: 最初の数値。
            b: 2番目の数値。
        """
        return a - b