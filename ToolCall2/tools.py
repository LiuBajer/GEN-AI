import requests
from rich import print
import json
from dotenv import load_dotenv
import os

load_dotenv()
WEATHER_API_KEY = os.getenv("WKEY")

def get_weather(city:str):
    parameters = {
    "q" : city,
    "key" : WEATHER_API_KEY
    }
    response = requests.get(
        url="https://api.weatherapi.com/v1/current.json?",
        params=parameters
    )
    data = response.json()
    current = data["current"]

    return {
        "temp": current["temp_c"],
        "is_day": bool(current["is_day"]),
        "wind_kph": current["wind_kph"],
        "pressure_mb": current["pressure_mb"],
        "humidity": current["humidity"],
        "feelslike_c": current["feelslike_c"],
        "condition": current["condition"]["text"]
    }



#data = response.json() # deserialization
#dataAsText = json.dumps(data) # serialization

data = get_weather("Kaunas")
print(data)
#print(data["current"]["temp_c"])