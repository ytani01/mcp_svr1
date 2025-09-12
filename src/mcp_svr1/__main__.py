#
# (c) 2025 Yoichi Tanibayashi
#
from mcp.server.fastmcp import FastMCP

from . import __version__

mcp = FastMCP("mcp_svr1")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Adds two numbers.""" 
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtracts two numbers."""
    return a - b

@mcp.tool()
def version() -> str:
    """Returns the server version."""
    return f"{__package__} {__version__}"

@mcp.tool()
def echo(text: str) -> str:
    """Echoes back the parameters it received."""
    return text


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
