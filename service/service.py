import os
import httpx

API_KEY = os.getenv("WEATHER_API_KEY") # it is picked from the client config file, not the OS environment

class WeatherAPIService:

    async def get_weather(self, city: str) -> str:

        """Return current weather for a city using OpenWeatherMap."""
        if not API_KEY:
            return "Missing WEATHER_API_KEY in Client Config"

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