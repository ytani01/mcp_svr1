from mcp.server.fastmcp import FastMCP
from ..utils.my_logger import get_logger
from ..core import get_debug_flag

from mcp_svr1 import __version__


def register_version_resource(mcp: FastMCP):
    log = get_logger(__name__, debug=get_debug_flag())
    # @mcp.resource() デコレータは、関数をFastMCPリソースとして登録します。
    # 第一引数はパス（例: "server://version"）、第二引数は説明です。
    # リソースは読み取り専用データを提供します。
    @mcp.resource(
        "server://version",
        description="""Returns the MCP server version number.
        Use when user asks for server version."""
        )
    def version() -> str:
        """Returns the MCP server version (read-only resource)."""
        log.debug(f"version: __package__={__package__}, __version__={__version__}")
        return f"{__package__} {__version__}"
