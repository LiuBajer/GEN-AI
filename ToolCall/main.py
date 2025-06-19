from tools import sum, uppercase
from dispatcher import execute
result = sum(4, 4.8)
print(result)

import os
from openai import OpenAI
from dotenv import load_dotenv
from rich import print
import json

sum_function_definition = {
    "name": "sum",
    "description": "Adds two numbers together",
    "parameters": {
        "type": "object",
        "properties": {
            "a": {"type": "number", "description": "The first number"},
            "b": {"type": "number", "description": "The second number"}
        },
        "required": ["a", "b"]
    }
}

uppecase_function_definition = {
    "name": "uppercas",
    "description": "Makes text into uppercase",
    "parameters": {
        "type": "object",
        "properties": {
            "text": {"type": "string", "description": "The given text"}
        },
        "required": ["text"]
    }
}

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

client = OpenAI(base_url=endpoint, api_key=token)

response = client.chat.completions.create(
    model = model,
    messages = [{"role": "system", "content": "If You get prompted for math, pls use provided tools. \n If You get prompted with math please give the answer in this format \" The answer to this question {queston} is: \" "}, 
                {"role": "user", "content": "What is 23.5 + 6.5"}],
    temperature=0.7,
    tools=[{"type": "function", "function": sum_function_definition}],
    tool_choice="auto"
)

tool_calls = response.choices[0].message.tool_calls
print(response)
print(tool_calls)

# checks if any tools were called:
if len(tool_calls) != 0:
    tool_call = tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    result = execute(tool_call.function.name, **args)
    print(f"[green]{result}[/green]")

if result != None:
    response = client.chat.completions.create(
    model = model,
    messages = [{"role": "system", "content": "If You get prompted for math, pls use provided tools. \n If You get prompted with math please give the answer in this format \" The answer to this question {queston} is: \" "}, 
                {"role": "user", "content": "What is 23.5 + 6.5"},
                {"role": "assistant", "content": f"the result is {result}"}],
    temperature=0.7,
    tools=[{"type": "function", "function": sum_function_definition}],
    tool_choice="auto"
    )


print(tool_calls)