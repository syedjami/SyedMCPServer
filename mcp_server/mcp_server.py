import os
from mcp.server.fastmcp import FastMCP

from weather_service import WeatherAPIService

mcp = FastMCP("mcp_server")

# Weather Tool
@mcp.tool()
async def get_weather(city: str) -> str:
    
    # api_key = os.getenv("WEATHER_API_KEY")
    # if not api_key:
    #     return "Server: API key missing. Set WEATHER_API_KEY in your environment."

    """Return current weather for a city using OpenWeatherMap."""
    ws = WeatherAPIService()
    return await ws.get_weather(city)


# Stock Tool
from stock_service import StockAPIService
@mcp.tool()
def get_stock_info(symbol: str) -> str:
    """Return the latest price, open price, and previous close for a stock symbol."""
    ss = StockAPIService()
    return ss.get_stock_info(symbol)

def run():
    mcp.run(transport="stdio")