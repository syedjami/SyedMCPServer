from mcp.server.fastmcp import FastMCP
import httpx
import os

from service import WeatherAPIService

mcp = FastMCP("weather")
API_KEY = 'eb2872a46709af57eff58bf31118cff7'
# API_KEY = os.getenv("WEATHER_API_KEY")

@mcp.tool()
async def get_weather(city: str) -> str:
    """Return current weather for a city using OpenWeatherMap."""
    ws = WeatherAPIService()
    return await ws.get_weather(city)

def run():
    mcp.run(transport="stdio")