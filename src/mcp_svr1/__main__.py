#
# (c) 2025 Yoichi Tanibayashi
#
from importlib.metadata import version as get_version_from_metadata

from mcp.server.fastmcp import FastMCP

if __package__:
    __version__ = get_version_from_metadata(__package__)
else:
    __version__ = "_._._"


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
