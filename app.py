import random
from typing import Any
import os

from mcp.server.fastmcp import FastMCP

# Use PORT environment variable provided by Render, fallback to 9876
port = int(os.environ.get("PORT", 9876))
mcp = FastMCP("Local Remote MCP", port=port)


@mcp.tool()
def get_random_number() -> dict[str, Any]:
    """Gets a random whole number between 0 and 100."""

    return {
        "number": random.randint(0, 100),
    }


if __name__ == "__main__":
    print(f"Server starting on port {port}")
    print(f"SSE endpoint: http://0.0.0.0:{port}/sse")
    # FastMCP automatically binds to 0.0.0.0
    mcp.run("sse")