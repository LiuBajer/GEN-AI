
from openai import OpenAI
import os

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model = "text-embedding-3-small"
client = OpenAI(base_url=endpoint, api_key=token)

def get_embedding(text):
    response = client.embeddings.create(input=text, model=model)
    return response.data[0].embedding

def get_embeddings(texts: list[str]):
    response = client.embeddings.create(input=texts, model=model)
    return [x.embedding for x in response.data]