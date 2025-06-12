import os
from dotenv import load_dotenv
# LangChain openAI client
from langchain_openai import ChatOpenAI
from langchain_core import messages
from langchain.prompts import PromptTemplate

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

template = PromptTemplate.from_template("Translate '{text}' to French")
prompt1 = template.format(text="Hello, how are you?")
prompt2 = template.format(text="My name is Milana, what's yours?")
prompt3 = template.format(text="I'm Andrius")

print(prompt1)
print(prompt2)
print(prompt3)