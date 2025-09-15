from mcp.server.fastmcp import FastMCP


def register_echo_tool(mcp: FastMCP):
    # @mcp.tool() デコレータは、関数をFastMCPツールとして登録します。
    # 関数名がツール名、型ヒントがインターフェースを定義します。
    @mcp.tool()
    def echo(text: str) -> str:
        """Echoes the input text.

        Args:
            text: エコーするテキスト。
        """
        return text