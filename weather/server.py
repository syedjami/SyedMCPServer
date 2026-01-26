import os
from mcp.server.fastmcp import FastMCP

from service import WeatherAPIService

mcp = FastMCP("weather")

API_KEY = os.getenv("WEATHER_API_KEY")

@mcp.tool()
async def get_weather(city: str) -> str:
    """Return current weather for a city using OpenWeatherMap."""
    ws = WeatherAPIService()
    return await ws.get_weather(city)

def run():
    mcp.run(transport="stdio")