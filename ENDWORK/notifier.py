from weather import get_weather
from llm import get_clothing_advice
from db import get_due_users
from datetime import datetime
import smtplib

def format_prompt(user, weather_data):
    prompt = f"""
    Provide clothing recommendations for:
    - User: {user['email']}
    - Children: {user['children']}
    - Activities: {user.get('notes', '')}
    - Weather forecast: {weather_data}
    """
    return prompt

def send_email(to_address, body):
    from_addr = "your.email@example.com"
    password = "your-email-password"

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(from_addr, password)
        message = f"Subject: Clothing Advice\n\n{body}"
        server.sendmail(from_addr, to_address, message)

def notify():
    hour = datetime.now().hour
    users = get_due_users(hour)
    for user in users:
        weather = get_weather(user["latitude"], user["longitude"])
        prompt = format_prompt(user, weather)
        advice = get_clothing_advice(prompt)

        if user["preferred_contact"] == "email":
            send_email(user["email"], advice)
        # You can expand this to SMS using Twilio or similar