from mcp.server.fastmcp import FastMCP
from ..utils.my_logger import get_logger
from ..core import get_debug_flag

def register_echo_tool(mcp: FastMCP):
    log = get_logger(__name__, debug=get_debug_flag())
    # @mcp.tool() デコレータは、関数をFastMCPツールとして登録します。
    # 関数名がツール名、型ヒントがインターフェースを定義します。
    @mcp.tool()
    def echo(text: str) -> str:
        """Echoes the input text.

        Args:
            text: エコーするテキスト。
        """
        log.debug(f"echo: text='{text}'")
        return text