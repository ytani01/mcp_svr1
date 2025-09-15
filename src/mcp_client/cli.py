import asyncio
import json
import textwrap

import asyncclick as click

from mcp_client.utils import get_mcp_client


@click.group()
def mcp_client():
    """MCP Client CLI tool."""
    pass


@mcp_client.command()
@click.argument("tool_name")
@click.argument("args", nargs=-1)
@click.option(
    "--server",
    default=None,
    help="""MCP server URL or path to server instance."""
)
async def call(tool_name: str, server: str, args: tuple[str, ...]):
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
    help="""MCP server URL or path to server instance."""
)
async def read(resource_uri: str, server: str):  # type: ignore
    """Read a resource from the MCP server.

    RESOURCE_URI: The URI of the resource to read (e.g., server://version).
    """
    try:
        client = await get_mcp_client(server)
        async with client:
            result = await client.read_resource(resource_uri)
            if hasattr(result, 'text'):
                click.echo(result.text)
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
    help="""MCP server URL or path to server instance."""
)
@click.option(
    "--verbose",
    is_flag=True,
    help="""Show verbose tool information."""
)
async def list_tools(server: str, verbose: bool):
    """List available tools on the MCP server."""
    try:
        client = await get_mcp_client(server)
        async with client:
            tools = await client.list_tools()
            if tools:
                if verbose:
                    click.echo("利用可能なツール:")
                    for tool in tools:
                        click.echo(f"  - {tool.name}:")
                        description_lines = textwrap.wrap(
                            tool.description, width=70
                        )
                        for line in description_lines:
                            click.echo(f"    {line}")
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
                                click.echo(
                                    f"      - {param_name} ({param_type}):"
                                )
                                param_description_lines = textwrap.wrap(
                                    param_description, width=65
                                )
                                for line in param_description_lines:
                                    click.echo(f"        {line}")
                else:
                    tool_names = [tool.name for tool in tools]
                    click.echo("利用可能なツール: " + ", ".join(tool_names))
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
async def list_resources(server: str, verbose: bool):
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
                            resource.description, width=70
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





def main():
    asyncio.run(mcp_client())