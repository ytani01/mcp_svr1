import json
import re
import textwrap
import asyncclick as click

from clickutils import click_common_opts

from .. import __version__, get_logger

# 変更: mcp_client.utils から mcp_svr1.cli.utils に変更
from mcp_svr1.cli.utils import get_mcp_client


@click.group()
# 変更: mcp_client から client_cli に変更
@click_common_opts(__version__)
def client_cli(ctx, debug):
    """MCP Client CLI tool."""

    __log = get_logger(__name__, debug)
    __log.debug("command name = %a", ctx.command.name)


@client_cli.command()
@click.argument("tool_name")
@click.argument("args", nargs=-1)
@click.option(
    "--server",
    default=None,
    help="""MCP server URL or path to server instance."""
)
@click_common_opts(__version__)
async def call(ctx, tool_name: str, server: str, args: tuple[str, ...], debug):
    """Call a tool on the MCP server."""
    __log = get_logger(__name__, debug)
    __log.debug("command name = %a", ctx.command.name)

    tool_args = {}
    for arg in args:
        if "=" in arg:
            key, value = arg.split("=", 1)
            try:
                tool_args[key] = json.loads(value)
            except json.JSONDecodeError:
                tool_args[key] = value
        else:
            click.echo(
                f"Invalid argument format: {arg}. Expected key=value.",
                err=True
            )
            return

    try:
        client = await get_mcp_client(server)
        async with client:
            result = await client.call_tool(tool_name, tool_args)
            click.echo(json.dumps(result.data.__dict__, indent=2))
    except Exception as e:
        click.echo(f"Error calling tool: {e}", err=True)


@client_cli.command()
@click.argument("resource_uri")
@click.option(
    "--server",
    default=None,
    help="""MCP server URL or path to server instance."""
)
@click_common_opts(__version__)
async def read(ctx, resource_uri: str, server: str, debug: bool):  # type: ignore
    """Read a resource from the MCP server.

    RESOURCE_URI: The URI of the resource to read (e.g., server://version).
    """
    __log = get_logger(__name__, debug)
    __log.debug("command name = %a", ctx.command.name)

    try:
        client = await get_mcp_client(server)
        async with client:
            result = await client.read_resource(resource_uri)
            from mcp.types import (
                BlobResourceContents,
                TextResourceContents,
            )
            for _r in result:
                __log.debug("type(_r)=%s", type(_r))
                __log.debug("_r.uri=%s", _r.uri)
                __log.debug("_r.text='%s'", _r.text)
                if isinstance(result, TextResourceContents):
                    click.echo(result.text)
                elif isinstance(result, BlobResourceContents):
                    click.echo("Binary content received.")
                else:
                    try:
                        click.echo(json.dumps(_r, indent=2))
                    except TypeError:
                        click.echo(repr(_r))
    except Exception as e:
        click.echo(f"Error reading resource: {e}", err=True)


@client_cli.group()
@click_common_opts(__version__)
def list(ctx, debug):
    """List tools or resources on the MCP server."""
    __log = get_logger(__name__, debug)
    __log.debug("command name = %a", ctx.command.name)

    

@list.command(name="tools")
@click.option(
    "--server",
    default=None,
    help="""MCP server URL or path to server instance."""
)
@click.option(
    "--verbose",
    is_flag=True,
    help="""Show verbose tool information."""
)
@click_common_opts(__version__)
async def list_tools(ctx, server: str, verbose: bool, debug):
    """List available tools on the MCP server."""
    __log = get_logger(__name__, debug)
    __log.debug("command name = %a", ctx.command.name)

    try:
        client = await get_mcp_client(server)
        async with client:
            tools = await client.list_tools()
            if tools:
                if verbose:
                    click.echo("利用可能なツール:")
                    for tool in tools:
                        # tool.description からツールの説明を抽出
                        tool_description_match = re.search(
                            r"^(.*?)(?:\s*Args:|$)",
                            (tool.description or ""),
                            re.DOTALL
                        )
                        tool_description_text = (
                            tool_description_match.group(1).strip()
                            if tool_description_match
                            else ""
                        )
                        

                        click.echo(
                            f"  - {tool.name}: {tool_description_text}"
                        )

                        if (
                            tool.inputSchema
                            and isinstance(tool.inputSchema, dict)
                            and tool.inputSchema.get('properties')
                        ):
                            click.echo("    引数:")
                            for param_name, param_schema in \
                                    tool.inputSchema['properties'].items():
                                param_type = param_schema.get("type", "不明")
                                param_description = param_schema.get(
                                    "description", "説明なし"
                                )

                                # tool.description から引数の説明を抽出
                                args_description_match = re.search(
                                    r"Args:\s*(.*)",
                                    (tool.description or ""),
                                    re.DOTALL
                                )
                                if args_description_match:
                                    args_description_str = \
                                        args_description_match.group(1)
                                    # 各引数の説明を抽出
                                    param_desc_match = re.search(
                                        rf"{param_name}:\s*(.*?)(?:\s*\w+:\s*|$)",
                                        args_description_str,
                                        re.DOTALL
                                    )
                                    param_description = (
                                        param_desc_match.group(1).strip()
                                        if param_desc_match
                                        else ""
                                    )

                                click.echo(
                                    f"      - {param_name} ({param_type}): "
                                    f"{param_description}"
                                )
                else:
                    click.echo("利用可能なツール:")
                    for tool in tools:
                        # tool.description からツールの説明を抽出
                        tool_description_match = re.search(
                            r"^(.*?)(?:\s*Args:|$)",
                            (tool.description or ""),
                            re.DOTALL
                        )
                        tool_description_text = (
                            tool_description_match.group(1).strip()
                            if tool_description_match
                            else ""
                        )
                        
                        click.echo(
                            f"  - {tool.name}: {tool_description_text}"
                        )
            else:
                click.echo("利用可能なツールはありません。")
    except Exception as e:
        click.echo(f"Error listing tools: {e}", err=True)


@list.command(name="resources")
@click.option(
    "--server",
    default=None,
    help="""MCP server URL or path to server instance."""
)
@click.option(
    "--verbose",
    is_flag=True,
    help="""Show verbose resource information."""
)
@click_common_opts(__version__)
async def list_resources(ctx, server: str, verbose: bool, debug):
    """List available resources on the MCP server."""
    __log = get_logger(__name__, debug)
    __log.debug("command name = %a", ctx.command.name)

    try:
        client = await get_mcp_client(server)
        async with client:
            resources = await client.list_resources()
            if resources:
                if verbose:
                    click.echo("利用可能なリソース:")
                    for resource in resources:
                        click.echo(f"  - {resource.uri}:")
                        description_lines = textwrap.wrap(
                            resource.description or "", width=70
                        )
                        for line in description_lines:
                            click.echo(f"    {line}")
                else:
                    resource_uris = [
                        str(resource.uri) for resource in resources
                    ]
                    click.echo(
                        "利用可能なリソース: " + ", ".join(resource_uris)
                    )
            else:
                click.echo("利用可能なリソースはありません。")
    except Exception as e:
        click.echo(f"Error listing resources: {e}", err=True)
