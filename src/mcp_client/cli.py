import asyncio
import json

import asyncclick as click
from click_shell import shell

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
    """Call a tool on the MCP server.

    TOOL_NAME: The name of the tool to call.
    ARGS: Arguments for the tool in key=value format (e.g., a=1 b=2).
    """
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
async def list_tools(server: str):
    """List available tools on the MCP server."""
    try:
        client = await get_mcp_client(server)
        async with client:
            tools = await client.list_tools()
            for tool_name in tools:
                click.echo(tool_name)
    except Exception as e:
        click.echo(f"Error listing tools: {e}", err=True)


@list.command(name="resources")
@click.option(
    "--server",
    default=None,
    help="""MCP server URL or path to server instance."""
)
async def list_resources(server: str):
    """List available resources on the MCP server."""
    try:
        client = await get_mcp_client(server)
        async with client:
            resources = await client.list_resources()
            for resource_uri in resources:
                click.echo(resource_uri)
    except Exception as e:
        click.echo(f"Error listing resources: {e}", err=True)





@shell(prompt='mcp > ', intro='Starting MCP shell...')
def mcp_shell():
    pass

mcp_client.add_command(mcp_shell, "shell")

def main():
    asyncio.run(mcp_client())
