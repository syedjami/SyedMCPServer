"""Direct unit tests for weather service without MCP subprocess."""
import pytest
from weather_service import WeatherAPIService


@pytest.mark.asyncio
async def test_weather_api_service_direct():
    """Test weather service directly (no MCP subprocess)"""
    ws = WeatherAPIService()
    
    # This calls get_weather directly, making it easy to debug
    result = await ws.get_weather("London")
    
    assert result
    assert "London" in result
    assert "°C" in result
    print(f"\nWeather: {result}")
