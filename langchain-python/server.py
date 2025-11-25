from mcp.server.fastmcp import FastMCP

# Create an MCP server instance
mcp = FastMCP("Demo Server")

# Define a simple tool (function) that can be called by the LLM
@mcp.tool()
def add(a: int, b: int) -> int:
    """
    Add two numbers together.
    :param a: First number.
    :param b: Second number.
    :return: Sum of the numbers.
    """
    return a + b

# Run the server using STDIO transport (default for local development)
if __name__ == "__main__":
    mcp.run(transport="stdio")
