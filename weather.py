from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """Get the weather location"""
    return "The weather for location is sunny."

# The transport is the protocol used to communicate with the MCP server.
if __name__ == "__main__":
    mcp.run(transport="streamable-http")