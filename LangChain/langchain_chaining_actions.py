import os
from dotenv import load_dotenv
# LangChain openAI client
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
token = os.getenv("GITHUB_TOKEN")
endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1-mini"

llm = ChatOpenAI(base_url=endpoint, api_key=token, model=model, temperature=0.7)

template = PromptTemplate.from_template("Translate '{text}' to {lang}")
chain = LLMChain(llm=llm, prompt=template)
result = chain.invoke({"text": "What's your name?", "lang": "Lithuanian"})
print(result)