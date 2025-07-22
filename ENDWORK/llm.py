from dotenv import  load_dotenv

load_dotenv()

import os
from openai import OpenAI

token = os.environ["GITHUB_TOKEN"]
print(token)
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

def get_clothing_advice(prompt):
    response = client.chat.completions.create(
            temperature=0.7,
            top_p=1.0,
            model=model,
            messages=[
                {"role": "system", "content": """You are an expert of how to dress on different weather
                  for all people and all ages. You must answer only how the provided additional people (children)
                 and the parent of the children should be dressing for the provided houry weather forecast data.
                 Your clothing advice must be insightful and helpful for all the related people provided.
                 Answer as concise as possible, providing only necessary weather and cloting details"""},
                {"role": "user", "content": prompt}
            ]
        )
    res = response.choices[0].message.content
    print(res)
    return res
