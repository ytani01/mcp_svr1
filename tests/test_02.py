
from typing import Any, cast

import pytest
from fastmcp.client import Client

from mcp_svr1.core import get_mcp_instance


@pytest.mark.asyncio
async def test_add():
    async with Client(get_mcp_instance()) as client:
        result = await client.call_tool("add", {"a": 1, "b": 2})
        assert result.data.result == 3

@pytest.mark.asyncio
async def test_subtract():
    async with Client(get_mcp_instance()) as client:
        result = await client.call_tool("subtract", {"a": 5, "b": 3})
        assert result.data.result == 2

@pytest.mark.asyncio
async def test_ping():
    async with Client(get_mcp_instance()) as client:
        result = await client.ping()
        assert result is True

@pytest.mark.asyncio
async def test_version():
    async with Client(get_mcp_instance()) as client:
        result = await client.read_resource("server://version")
        assert cast(Any, result[0]).text.startswith("mcp_svr")

@pytest.mark.asyncio
async def test_echo():
    async with Client(get_mcp_instance()) as client:
        test_string = "Hello, MCP!"
        result = await client.call_tool("echo", {"text": test_string})
        assert result.data.result == test_string
