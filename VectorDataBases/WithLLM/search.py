import chromadb
import embed
chroma_client = chromadb.PersistentClient(path="./vector-db") # in long term database

# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
drivingRules = chroma_client.get_or_create_collection(name="driving_rules")

query = input("Ask information about driving: ")

queryEmbed = embed.get_embedding(query)

result = drivingRules.query(query_embeddings=[queryEmbed], n_results=3)

print(result["documents"][0][0])
print(result["distances"])