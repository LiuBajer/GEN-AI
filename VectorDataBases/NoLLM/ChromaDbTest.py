import chromadb
chroma_client = chromadb.Client() # in RAM database

# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
collection = chroma_client.get_or_create_collection(name="my_collection")

# switch `add` to `upsert` to avoid adding the same documents every time
collection.upsert(
    documents=[
        "This is a document about pineapple",
        "This is a document about oranges",
        "This is a document about machines"
    ],
    ids=["id1", "id2", "is3"]
)

results = collection.query(
    query_texts=["This is a query document about cars"], # Chroma will embed this for you
    n_results=3 # how many results to return
)

print(results)