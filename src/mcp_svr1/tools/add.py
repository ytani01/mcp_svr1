from mcp.server.fastmcp import FastMCP

from ..core import get_debug_flag
from ..utils.my_logger import get_logger


def register_add_tool(mcp: FastMCP):
    log = get_logger(__name__, debug=get_debug_flag())

    # @mcp.tool() デコレータは、関数をFastMCPツールとして登録します。
    # 関数名がツール名、型ヒントがインターフェースを定義します。
    @mcp.tool()
    def add(a: int, b: int) -> int:
        """Adds two numbers.

        Args:
            a: first number
            b: second number
        """
        log.debug(f"add: a={a}, b={b}")
        return a + b
