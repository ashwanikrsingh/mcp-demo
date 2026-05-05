from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "Math": {
                "command": "python",
                "args": ["mathserver.py"], # The command to run the MCP server
                "transport": "stdio", # The transport protocol to use
            },
            "Weather": {
                "url": "http://localhost:8000/mcp", # The URL of the MCP server
                "transport": "streamable-http", # The transport protocol to use
            },
        }
    )
    
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY is not set")
    model = ChatGroq(model="llama-3.1-8b-instant", api_key=api_key)

    tools = await client.get_tools()

    agent = create_agent(model=model, tools=tools)
    
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is (3 + 4) * 5?"}]}
    )
    print("Math response:", math_response["messages"][-1].content)

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Get the weather for Tokyo?"}]}
    )
    print("Weather response:", weather_response["messages"][-1].content)
    

asyncio.run(main())