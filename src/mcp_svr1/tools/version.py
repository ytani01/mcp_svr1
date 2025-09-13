from mcp.server.fastmcp import FastMCP

from mcp_svr1 import __version__


def register_version_resource(mcp: FastMCP):
    @mcp.resource(
        "server://version",
        description="""Returns the MCP server version number.
        Use when user asks for server version."""
        )
    def version() -> str:
        """Returns the MCP server version (read-only resource)."""
        return f"{__package__} {__version__}"
