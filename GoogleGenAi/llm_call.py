from google import genai
from dotenv import load_dotenv
from pydantic import BaseModel
import os
from rich import print

class 

load_dotenv()

GOOGLE_AI_KEY = os.getenv("GOOGLE_AI_KEY")

client = genai.Client(api_key=GOOGLE_AI_KEY)

MODEL = "gemini-embedding-exp-03-07"
response = client.models.generate_content(
    model=MODEL,
    contents="How does AI work?")

print(response)

response = client.models.embed_content(
    model=MODEL,
    contents="How does AI work?")

print(response)
print(response.embeddings)