import mcp_client

client = mcp_client.Client()

# Call record_tokens
print(client.record_tokens(session_id="session1", tokens=100))
print(client.record_tokens(session_id="session1", tokens=50))
print(client.record_tokens(session_id="session2", tokens=200))

# Call get_token_usage
print(client.get_token_usage())
