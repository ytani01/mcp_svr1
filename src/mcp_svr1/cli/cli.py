import json
import re
import textwrap
from typing import Union

import asyncclick as click
from mcp.types import (  # type: ignore
    BlobResourceContents,
    TextResourceContents,
)

from mcp_svr1.cli.utils import get_mcp_client


@click.group()
@click.pass_context
def mcp_client(ctx):
    """MCP Client CLI tool."""
    ctx.ensure_object(dict)


@mcp_client.command()
@click.argument("tool_name")
@click.argument("args", nargs=-1)
@click.option(
    "--server",
    default=None,
    help="""MCP server URL or path to server instance.""",
)
@click.pass_context
async def call(ctx, tool_name: str, server: str, args: tuple[str, ...]):
    """Call a tool on the MCP server."""

    tool_args = {}
    for arg in args:
        if "=" in arg:
            key, value = arg.split("=", 1)
            tool_args[key] = json.loads(value) # Attempt to parse as JSON
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


@mcp_client.command()
@click.argument("resource_uri")
@click.option(
    "--server",
    default=None,
    help="""MCP server URL or path to server instance.""",
)
@click.pass_context
async def read(ctx, resource_uri: str, server: str):  # type: ignore
    """Read a resource from the MCP server.

    RESOURCE_URI: The URI of the resource to read (e.g., server://version).
    """

    try:
        client = await get_mcp_client(server)
        async with client:
            raw_result = await client.read_resource(resource_uri)
            result: (
                Union[TextResourceContents, BlobResourceContents]
            ) = raw_result  # type: ignore
            if isinstance(result, TextResourceContents):
                click.echo(result.text)
            elif isinstance(result, BlobResourceContents):
                click.echo(
                    "Binary content received."
                )
            else:
                try:
                    click.echo(json.dumps(result, indent=2))
                except TypeError:
                    click.echo(repr(result))
    except Exception as e:
        click.echo(f"Error reading resource: {e}", err=True)


@mcp_client.group()
def list():
    """List tools or resources on the MCP server."""
    pass


@list.command(name="tools")
@click.option(
    "--server",
    default=None,
    help="""MCP server URL or path to server instance.""",
)
@click.option(
    "--verbose",
    is_flag=True,
    help="""Show verbose tool information.""",
)
@click.pass_context
async def list_tools(ctx, server: str, verbose: bool):
    """List available tools on the MCP server."""

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
                            tool.description or "",
                            re.DOTALL
                        )
                        if tool_description_match and tool.description:
                            text = tool_description_match.group(1)
                            desc = text.strip() if text else ""
                            tool_description_text = desc
                        else:
                            desc = (tool.description.strip()
                               if tool.description else "")
                            tool_description_text = desc

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
                                    tool.description or "",
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
                                    if param_desc_match:
                                        param_description = \
                                            param_desc_match.group(1).strip()

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
                            tool.description or "",
                            re.DOTALL
                        )
                        if tool_description_match and tool.description:
                            text = tool_description_match.group(1)
                            desc = text.strip() if text else ""
                            tool_description_text = desc
                        else:
                            desc = (tool.description.strip()
                               if tool.description else "")
                            tool_description_text = desc
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
    help="""MCP server URL or path to server instance.""",
)
@click.option(
    "--verbose",
    is_flag=True,
    help="""Show verbose resource information.""",
)
@click.pass_context
async def list_resources(ctx, server: str, verbose: bool):
    """List available resources on the MCP server."""

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

