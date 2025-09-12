from mcp.server.fastmcp import FastMCP


def register_subtract_tool(mcp: FastMCP):
    @mcp.tool()
    def subtract(a: int, b: int) -> int:
        """Subtracts two numbers.""" 
        return a - b