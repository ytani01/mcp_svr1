import json

import pytest
from asyncclick.testing import CliRunner

from mcp_svr1.__main__ import cli


@pytest.fixture
def runner():
    return CliRunner()


@pytest.mark.asyncio
async def test_call_add(runner):
    result = await runner.invoke(cli, ["client", "call", "add", "a=1", "b=2"])
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data["result"] == 3


@pytest.mark.asyncio
async def test_call_subtract(runner):
    result = await runner.invoke(
        cli, ["client", "call", "subtract", "a=5", "b=2"]
    )
    assert result.exit_code == 0
    data = json.loads(result.output)
    assert data["result"] == 3


@pytest.mark.asyncio
async def test_read_version(runner):
    result = await runner.invoke(cli, ["client", "read", "server://version"])
    assert result.exit_code == 0
    assert "mcp_svr1" in result.output


@pytest.mark.asyncio
async def test_list_tools(runner):
    # verboseなしのテスト
    result = await runner.invoke(cli, ["client", "list", "tools"])
    assert result.exit_code == 0
    assert "利用可能なツール:" in result.output
    assert "  - add: Adds two numbers." in result.output
    assert "  - echo: Echoes the input text." in result.output
    assert "  - subtract: Subtracts two numbers." in result.output

    # verboseありのテスト
    result = await runner.invoke(cli, ["client", "list", "tools", "--verbose"])
    assert result.exit_code == 0
    assert "利用可能なツール:" in result.output
    assert "  - add: Adds two numbers." in result.output
    assert "    引数:" in result.output
    assert "      - a (integer): 最初の数値。" in result.output
    assert "      - b (integer): 2番目の数値。" in result.output
    assert "  - echo: Echoes the input text." in result.output
    assert "    引数:" in result.output
    assert "      - text (string): エコーするテキスト。" in result.output
    assert "  - subtract: Subtracts two numbers." in result.output
    assert "    引数:" in result.output
    assert "      - a (integer): 最初の数値。" in result.output
    assert "      - b (integer): 2番目の数値。" in result.output


@pytest.mark.asyncio
async def test_list_resources(runner):
    result = await runner.invoke(cli, ["client", "list", "resources"])
    assert result.exit_code == 0
    assert "server://version" in result.output