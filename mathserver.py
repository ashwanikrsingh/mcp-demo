from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> int:
    """Divide two numbers"""
    return a / b

@mcp.tool()
def power(a: int, b: int) -> int:
    """Raise a number to the power of another number"""
    return a ** b

# The transport is the protocol used to communicate with the MCP server.
# In this case, we are using the stdio transport, 
# which means the server will communicate with the client over the standard input and output streams.
# You can also use the http transport, which means the server will communicate with the client over the HTTP protocol.
# You can also use the websocket transport, which means the server will communicate with the client over the WebSocket protocol.
# You can also use the tcp transport, which means the server will communicate with the client over the TCP protocol.
# You can also use the udp transport, which means the server will communicate with the client over the UDP protocol.
# You can also use the unix transport, which means the server will communicate with the client over the Unix domain socket protocol.
# You can also use the ssh transport, which means the server will communicate with the client over the SSH protocol.
# You can also use the telnet transport, which means the server will communicate with the client over the Telnet protocol.
# You can also use the ftp transport, which means the server will communicate with the client over the FTP protocol.
if __name__ == "__main__":
    mcp.run(transport="stdio")