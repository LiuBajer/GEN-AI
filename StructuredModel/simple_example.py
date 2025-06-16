import os
from openai import OpenAI
from dotenv import load_dotenv
from rich import print
from pydantic import BaseModel

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

client = OpenAI(base_url=endpoint, api_key=token)

class CityData(BaseModel):
    totalPopulation: int
    men_population: int
    women_population: int
    reason_why_city_is_popular: str
    city_name: str
class CityDataObject(BaseModel):
    top_cities: list[CityData]

response = client.beta.chat.completions.parse(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant who knows about europe countries and gives statistics in json mode"
        },
        {
            "role": "system",
            "content": "What are the top 3 cities of France and what are the city population of men and women?"
        }
    ],
    model=model,
    response_format=CityDataObject
)

print(response.choices[0].message.parsed.top_cities[0].city_name)