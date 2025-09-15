import asyncio
from fastmcp import Client
from mcp_svr1.__main__ import mcp

async def test_fastmcp_client():
    try:
        client = Client(mcp)
        async with client:
            result = await client.call_tool("add", {"a": 1, "b": 2})
            print(f"Result: {result.data.__dict__}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(test_fastmcp_client())
