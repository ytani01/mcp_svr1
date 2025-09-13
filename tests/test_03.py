import json

import pytest
from asyncclick.testing import CliRunner

from mcp_client.cli import mcp_client


@pytest.fixture
def runner():
    return CliRunner()


@pytest.mark.asyncio
async def test_call_add(runner):
    result = await runner.invoke(mcp_client, ["call", "add", "a=1", "b=2"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data["result"] == 3


@pytest.mark.asyncio
async def test_call_subtract(runner):
    result = await runner.invoke(
        mcp_client, ["call", "subtract", "a=5", "b=2"]
    )
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data["result"] == 3


@pytest.mark.asyncio
async def test_read_version(runner):
    result = await runner.invoke(mcp_client, ["read", "server://version"])
    assert result.exit_code == 0
    assert "mcp_svr1" in result.output


@pytest.mark.asyncio
async def test_list_tools(runner):
    result = await runner.invoke(mcp_client, ["list", "tools"])
    assert result.exit_code == 0
    assert "add" in result.output
    assert "subtract" in result.output
    assert "echo" in result.output


@pytest.mark.asyncio
async def test_list_resources(runner):
    result = await runner.invoke(mcp_client, ["list", "resources"])
    assert result.exit_code == 0
    assert "server://version" in result.output
