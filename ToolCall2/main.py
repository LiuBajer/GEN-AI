from openai import OpenAI
import os
from dotenv import load_dotenv
from tools import get_weather, get_weather_definition
from rich import print
import json


load_dotenv()

API_KEY = os.getenv("GITHUB_TOKEN")
PLATFORM_ENPOINT = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

EXIT_KEYWORDS = ["exit"]

client = OpenAI(base_url=PLATFORM_ENPOINT, api_key=API_KEY)
messages = [{"role": "system", "content": "You are a helpful assistant. Answer about weather only."}]

while True:
    prompt = input("User: ").strip()
    if prompt.lower() in EXIT_KEYWORDS:
        break

    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=[get_weather_definition],
        tool_choice="auto"
    )

    tool_calls = response.choices[0].message.tool_calls
    if tool_calls != None:
        tool_call = tool_calls[0]
        city = json.loads(tool_call.function.arguments)["city"]
        tool_response = get_weather(city)
        tool_response_as_text = json.dumps(tool_response)
        messages.append({"role": "assistant", "tool_calls" : [tool_call]})
        messages.append({"role": "tool", "tool_call_id" : tool_call.id, "content": str(tool_response_as_text)})
        response = client.chat.completions.create(
        model=model,
        messages=messages,
        tools=[get_weather_definition],
        tool_choice="auto"
    )

        
    chatbot_response = response.choices[0].message.content
    #print(chatbot_response)
    #print(response)
    print(f"[green]AI: [/green] {chatbot_response}")