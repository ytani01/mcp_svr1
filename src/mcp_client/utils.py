from typing import Optional

from fastmcp import Client

from mcp_svr1.__main__ import mcp


async def get_mcp_client(server_url: Optional[str] = None) -> Client:
    """
    FastMCPクライアントインスタンスを取得します。
    server_urlがNoneの場合、既存のインメモリサーバーインスタンスに接続します。
    それ以外の場合、指定されたURLに接続します。
    """
    if server_url is None:
        # 既存のインメモリサーバーインスタンスに接続
        client = Client(mcp)  # type: ignore
    else:
        # 指定されたURLに接続
        client = Client(server_url)

    # エラーハンドリングは、Clientの接続時に発生する可能性のある例外を考慮
    # 現時点では、Clientの初期化自体は例外を発生させないため、
    # 接続エラーはcall_toolやread_resourceの呼び出し時に発生する可能性が高い
    # そのため、ここでは基本的な初期化のみを行う
    return client