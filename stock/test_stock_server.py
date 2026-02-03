import pytest
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import json
import os

@pytest.mark.asyncio
async def test_stock_server_initialization():
    """Test server starts and initializes correctly"""

    env = os.environ.copy()
    env["PYTHONPATH"] = os.getcwd()
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "stock.mcp_server.mcp_server"],
        env=env,
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # Verify tools are available
            tools = await session.list_tools()
            tool_names = [tool.name for tool in tools.tools]
            assert "get_stock_info" in tool_names

@pytest.mark.asyncio
async def test_stock_server_get_stock_info():
    """Test stock info lookup for a company stock symbol"""

    env = os.environ.copy()
    env["PYTHONPATH"] = os.getcwd()
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "stock.mcp_server.mcp_server"],
        env=env,
    )
    
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            
            # Call weather tool
            result = await session.call_tool(
                "get_stock_info",
                arguments={"symbol": "AAPL"}
            )
            
            # Verify response
            assert result.content
            content = result.content[0].text
            # The stock service returns a string like "latest_price: $200, open_price: $198, previous_close: $199"
            assert "latest_price" in content
            assert "previous_close" in content