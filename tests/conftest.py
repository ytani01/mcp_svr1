# `pytest` フィクスチャを定義し、テストセッション全体で `FastMCP`
# インスタンスをセットアップ。`add`、`subtract`、`version`、`echo` ツールを
# 登録し、テスト実行時に MCP サーバーの環境を準備する役割を担う。
import pytest
from mcp.server.fastmcp import FastMCP

from mcp_svr1.core import set_mcp_instance
from mcp_svr1.tools.add import register_add_tool
from mcp_svr1.tools.echo import register_echo_tool
from mcp_svr1.tools.subtract import register_subtract_tool
from mcp_svr1.tools.version import register_version_resource


@pytest.fixture(scope="session", autouse=True)
async def setup_mcp_instance():
    mcp = FastMCP("mcp_svr1")
    set_mcp_instance(mcp, debug=False)  # Set debug to False for tests

    register_add_tool(mcp)
    register_subtract_tool(mcp)
    register_version_resource(mcp)
    register_echo_tool(mcp)

    yield
