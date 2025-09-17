from typing import Optional

from mcp.server.fastmcp import FastMCP

_mcp_instance: Optional[FastMCP] = None
_debug_flag: bool = False

def get_mcp_instance() -> FastMCP:
    if _mcp_instance is None:
        raise RuntimeError("MCP instance not initialized.")
    return _mcp_instance

def set_mcp_instance(instance: FastMCP, debug: bool = False):
    global _mcp_instance, _debug_flag
    _mcp_instance = instance
    _debug_flag = debug

def get_debug_flag() -> bool:
    return _debug_flag
