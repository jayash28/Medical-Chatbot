from src.helper import (
    load_pdf_file,
    text_split,
    download_hugging_face_embeddings,
)

from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
import os
import time

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medibot"

print("Loading PDFs...")
extracted_data = load_pdf_file("data/")

print("Splitting documents...")
text_chunks = text_split(extracted_data)

print("Loading embedding model...")
embeddings = download_hugging_face_embeddings()

if index_name not in pc.list_indexes().names():
    print("Creating Pinecone index...")
    pc.create_index(
        name=index_name,
        dimension=384,
        metric="cosine",
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1",
        ),
    )

    while not pc.describe_index(index_name).status["ready"]:
        time.sleep(2)

print("Index ready!")

print("Uploading vectors...")

docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    index_name=index_name,
    embedding=embeddings,
)

print("✅ Successfully uploaded all vectors!")