import os
from openai import OpenAI
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def get_embedding(text):
    response = client.embeddings.create(input=text, model=model_name)
    return response.data[0].embedding

texts = [
    "How can I reset my password?",
    "Where can I find my billing history?",
    #"How do I contact customer support?",
    #"What is the refund policy?"
    "Where can I plant strawberries"
]

import numpy as np

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "text-embedding-3-large"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

response = client.embeddings.create(
    input=texts,
    model=model_name,
)

for item in response.data:
    length = len(item.embedding)
    print(
        f"data[{item.index}]: length={length}, "
        f"[{item.embedding[0]}, {item.embedding[1]}, "
        f"..., {item.embedding[length-2]}, {item.embedding[length-1]}]"
    )
    

response2 = client.embeddings.create(
    input="Where to plant my strawberries?",
    model=model_name,
)


dataEmb = response.data[0].embedding
initEmb = response2.data[0].embedding

i = 0
for emb in response.data:
    similarity = cosine_similarity(emb.embedding, initEmb)
    i += 1
    print(f"{i}: {similarity}")
# print(response.data[0].embedding)
