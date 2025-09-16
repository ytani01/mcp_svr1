from typing import Optional
from mcp.server.fastmcp import FastMCP

_mcp_instance: Optional[FastMCP] = None

def get_mcp_instance() -> FastMCP:
    if _mcp_instance is None:
        raise RuntimeError("MCP instance not initialized.")
    return _mcp_instance

def set_mcp_instance(instance: FastMCP):
    global _mcp_instance
    _mcp_instance = instance
