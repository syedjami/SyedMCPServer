import os
from mcp.server.fastmcp import FastMCP

from weather_service import WeatherAPIService

mcp = FastMCP("mcp_server")


@mcp.tool()
async def get_weather(city: str) -> str:
    
    # api_key = os.getenv("WEATHER_API_KEY")
    # if not api_key:
    #     return "Server: API key missing. Set WEATHER_API_KEY in your environment."

    """Return current weather for a city using OpenWeatherMap."""
    ws = WeatherAPIService()
    return await ws.get_weather(city)

def run():
    mcp.run(transport="stdio")