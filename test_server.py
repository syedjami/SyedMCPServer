import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import json
import os

@pytest.mark.asyncio
async def test_weather_server_initialization():
    """Test server starts and initializes correctly"""
    # Set the API key in environment for subprocess
    env = os.environ.copy()
    env["WEATHER_API_KEY"] = "your_api_key_here"
    
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "mcp_server.mcp_server"],
        env=env,
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # Verify tools are available
            tools = await session.list_tools()
            tool_names = [tool.name for tool in tools.tools]
            assert "get_weather" in tool_names

@pytest.mark.asyncio
async def test_get_weather():
    """Test weather lookup for a city"""
    # Set the API key in environment for subprocess
    env = os.environ.copy()
    # x = env["WEATHER_API_KEY"]
    # env["WEATHER_API_KEY"] = "your_api_key_here"
    
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "mcp_server.mcp_server"],
        env=env,
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # Call weather tool
            result = await session.call_tool(
                "get_weather",
                arguments={"city": "London"}
            )
            
            # Verify response
            assert result.content
            content = result.content[0].text
            # The weather service returns a string like "London: 10°C, clear sky"
            assert "London" in content
            assert "°C" in content