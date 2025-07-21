import requests
from datetime import datetime, timedelta

def get_weather(lat, lon):
    end = (datetime.utcnow() + timedelta(hours=12)).isoformat()
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}&hourly=temperature_2m,precipitation,wind_speed_10m&"
        f"start={datetime.utcnow().isoformat()}&end={end}"
    )
    res = requests.get(url)
    return res.json()