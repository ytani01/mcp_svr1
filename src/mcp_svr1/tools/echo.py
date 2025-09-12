from mcp.server.fastmcp import FastMCP


def register_echo_tool(mcp: FastMCP):
    @mcp.tool()
    def echo(text: str) -> str:
        """Echoes the input text."""
        return text