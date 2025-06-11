import chromadb
chroma_client = chromadb.PersistentClient(path="./vector-db") # in long term database

# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
drivingRules = chroma_client.get_or_create_collection(name="driving_rules")

query = input("Ask information about driving: ")

result = drivingRules.query(query_texts=[query], n_results=1)

print(result["documents"][0][0])