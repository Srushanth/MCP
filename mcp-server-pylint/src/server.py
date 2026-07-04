from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="pylint",
    host="127.0.0.1",
    port=8000,
    sse_path="/sse",
    streamable_http_path="/mcp",
)
