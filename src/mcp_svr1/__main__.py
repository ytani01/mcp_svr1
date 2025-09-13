#
# (c) 2025 Yoichi Tanibayashi
#
from mcp.server.fastmcp import FastMCP

from .tools.add import register_add_tool
from .tools.echo import register_echo_tool
from .tools.subtract import register_subtract_tool
from .tools.version import register_version_resource

mcp = FastMCP("mcp_svr1")

register_add_tool(mcp)
register_subtract_tool(mcp)
register_version_resource(mcp)
register_echo_tool(mcp)


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()