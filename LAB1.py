import os

from dotenv import  load_dotenv

load_dotenv()
#secret = os.getenv("GITHUB_TOKEN")



import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)
KW = ["apartment", "flat", "room", "renovation", "furniture", "storage", "decor"]
prompt_guard = "You are an expert on improving apartments. If the user asks anything outside that domain," \
" answer: \"Sorry, I don't have knowledge on that.\" Wait for a new question."

while True:
    question = input("🧑 You: ").strip().lower()
    if any(kw in question for kw in KW):
        response = client.chat.completions.create(
            temperature=0.7,
            top_p=1.0,
            model=model,
            messages=[
                {"role": "system", "content": prompt_guard},
                {"role": "user", "content": question}
            ]
        )
        print(response.choices[0].message.content)
    else:
        print("Sorry, I don't have knowledge on that.")