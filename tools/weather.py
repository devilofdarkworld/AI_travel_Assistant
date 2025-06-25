import requests
import os
from langchain.tools import tool
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

@tool
def get_weather(destination: str) -> str:
    """Get current weather info for a city using OpenWeatherMap API"""
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return "API key not found. Please set OPENWEATHER_API_KEY in your .env file."

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": destination,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        weather = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        return f"The current weather in {destination} is {weather}, temperature: {temp}°C (feels like {feels_like}°C)."
    except requests.RequestException as e:
        return f"Failed to get weather for {destination}. Error: {str(e)}"
    except KeyError:
        return f"Weather data not available for {destination}."

# For direct testing

