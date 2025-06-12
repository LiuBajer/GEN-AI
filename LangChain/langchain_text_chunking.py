from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader("Anyksciai.txt", encoding="utf-8")

docs = loader.load()
splitter = RecursiveCharacterTextSplitter(
    chunk_size=750,
    chunk_overlap=100
    )

chunks = splitter.split_documents(docs)

print(chunks[2].page_content)
print("Separator")
print(chunks[3].page_content)
print(len(chunks))