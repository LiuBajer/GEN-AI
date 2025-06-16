# complaint letter recognizer
# is_complaint: boolean which would tell if a letter was complainatory
# is_refund_request: boolean which would tell if a letter was an inquiry for refund
# positive_score: a float from 0 to 1 telling how positive the letter was.
# complaint_tags: string, one or two of the following: "not satisfied", "very disappointed", "complain", "unacceptable", "issue", "problem", "angry", "bad experience", "frustrated", "refund", "faulty", "poor service", "doesn't work", "worst"

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

complaint_letter = """Dear Customer Service,
I am writing to express my dissatisfaction with the recent purchase I made from your store.
The product arrived damaged and did not match the description provided on your website.
I expected a much higher quality based on the price I paid. I would like a full refund and an apology for the inconvenience.
Thank you for your attention to this matter.
Sincerely, Jonas"""

loving_product_letter = """Dear Customer Service,
The product was shipped fast (in four days). Product was easy to use, it's quality was the best!
Thank you for your service!
Sincerely, Jone
"""

from pydantic import BaseModel
class LetterInformation(BaseModel):
    "This is class for analysing letter content."
    "This class represents information about letter, specifically focusing on whether it is a complaint"
    "And what type of complaint it is"
    "It inherits from BaseModel"
    "positive_score is float telling how positive the letter was from 0 to 1, 1 - being the most positive."
    is_complaint: bool
    is_refund_request: bool
    positive_score: float
    complaint_tags: list[str]

complaint_keywords = [
        "not satisfied", "very disappointed", "complain", "unacceptable",
        "issue", "problem", "angry", "bad experience", "frustrated", "refund",
        "faulty", "poor service", "doesn't work", "worst"]

response = client.beta.chat.completions.parse(
    messages=[
        {
            "role": "system",
            "content": f"""You are a helpful assistant that classifies customer letters.
            Analyse the following message and respond in valid JSON
            Complaint tags should be a list of strings where strings can be the following:
            {", ".join(complaint_keywords)}"""
        },
        {
            "role": "user",
            "content": f"""\"{complaint_letter}\""""
        }
    ],
    model=model,
    response_format=LetterInformation
)

print(response)