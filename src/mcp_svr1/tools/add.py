from mcp.server.fastmcp import FastMCP


def register_add_tool(mcp: FastMCP):
    @mcp.tool()
    def add(a: int, b: int) -> int:
        """Adds two numbers.""" 
        return a + b