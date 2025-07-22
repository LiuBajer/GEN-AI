import requests
from datetime import datetime, timedelta

def get_weather(lat, lon):
        
    # Set the forecast length to 12 hours (Open-Meteo uses `forecast_days` or `forecast_hours`)
    url = (
        f"https://api.open-meteo.com/v1/forecast?"
        f"latitude={lat}&longitude={lon}"
        f"&hourly=temperature_2m,precipitation,wind_speed_10m"
        f"&forecast_hours=12" 
        f"&timezone=auto"   
    )
    
    res = requests.get(url)
    result = res.json()
    print(result)
    return result