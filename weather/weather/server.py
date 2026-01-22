from mcp.server.fastmcp import FastMCP
import httpx
import os

mcp = FastMCP("weather")
API_KEY = 'eb2872a46709af57eff58bf31118cff7'
# API_KEY = os.getenv("WEATHER_API_KEY")

@mcp.tool()
async def get_weather(city: str) -> str:
    """Return current weather for a city using OpenWeatherMap."""
    if not API_KEY:
        return "Missing WEATHER_API_KEY"

    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        data = r.json()

    if "main" not in data:
        return f"Error: {data}"

    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]

    return f"{city}: {temp}°C, {desc}"

def main():
    mcp.run(transport="stdio")