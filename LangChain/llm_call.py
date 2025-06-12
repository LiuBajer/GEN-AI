import os
from dotenv import load_dotenv
# LangChain openAI client
from langchain_openai import ChatOpenAI
from langchain_core import messages

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

llm = ChatOpenAI(base_url=endpoint, api_key=token, model=model, temperature=0.7)
message = messages.HumanMessage("What is LangChain?")
response = llm.invoke([message])
print(response.content)