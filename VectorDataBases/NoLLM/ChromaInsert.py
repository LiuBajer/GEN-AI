import chromadb
import uuid
chroma_client = chromadb.PersistentClient(path="./vector-db") # in long term database

# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
drivingRules = chroma_client.get_or_create_collection(name="driving_rules")

insertion = input(f"Specify to add about driving rules, we have {drivingRules.count()}: ")

new_id = str(uuid.uuid4())
# switch `add` to `upsert` to avoid adding the same documents every time
drivingRules.upsert(
    documents=[ insertion ],
    ids=[f"driving_rule_{drivingRules.count()+1}"]
)

print(f"Added like pro, now we have {drivingRules.count()}")