#
# (c) 2025 Yoichi Tanibayashi
#
"""
FastMCPサーバーのメインエントリーポイント。

このファイルは、FastMCPサーバーを初期化し、
ツールとリソースを登録してサーバーを実行します。
テンプレートとして、新しいツールやリソースを追加する際の参考にしてください。
"""
from clickutils import click_common_opts, import_click
from mcp.server.fastmcp import FastMCP

from . import __version__, get_logger
from .cli.client_cli import client_cli
from .core import get_mcp_instance, set_mcp_instance
from .tools.add import register_add_tool
from .tools.echo import register_echo_tool
from .tools.subtract import register_subtract_tool
from .tools.version import register_version_resource

click = import_click(async_flag=True)


# FastMCPサーバーインスタンスを初期化します。
# サーバー名はプロジェクト名と一致させるのが一般的です。
@click.group(invoke_without_command=True)
@click_common_opts(click, __version__)
def cli(ctx, debug):
    """MCP Server and Client CLI tool."""
    __log = get_logger(__name__, debug)
    __log.debug("command name = %a", ctx.command.name)
    __log.debug("subcommand = %a", ctx.invoked_subcommand)

    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug

    # FastMCPサーバーインスタンスを初期化します。
    # サーバー名はプロジェクト名と一致させるのが一般的です。
    mcp = FastMCP("mcp_svr1")

    # 追加: mcp インスタンスを core に設定
    set_mcp_instance(mcp, debug=debug)

    # 各ツールとリソースをFastMCPサーバーに登録します。
    # 新しいツールやリソースを作成した場合は、
    # ここに登録関数を追加してください。
    register_add_tool(mcp)
    register_subtract_tool(mcp)
    register_version_resource(mcp)
    register_echo_tool(mcp)

    if not ctx.invoked_subcommand:
        click.echo(ctx.get_help())


@cli.command()
@click_common_opts(click, __version__)
async def server(ctx, debug):
    """Start the MCP server."""
    __log = get_logger(__name__, debug)
    __log.debug("command name = %a", ctx.command.name)

    # transport="stdio" は標準入出力を使用することを示します。
    # 他のトランスポートオプション（例: "tcp"）も利用可能です。
    mcp = get_mcp_instance()
    await mcp.run_stdio_async()

# 変更: client_cli を cli グループに登録
cli.add_command(client_cli, name="client")

if __name__ == "__main__":
    cli()
