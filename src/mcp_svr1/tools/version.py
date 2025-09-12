from mcp.server.fastmcp import FastMCP

from mcp_svr1 import __version__


def register_version_tool(mcp: FastMCP):
    @mcp.tool()
    def version() -> str:
        """Returns the server version."""
        return f"{__package__} {__version__}"