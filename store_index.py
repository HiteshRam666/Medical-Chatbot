from src.helper import load_pdf_file, text_split 
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv, find_dotenv
import os
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone, ServerlessSpec

_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]
pinecone_api_key = os.environ.get("PINECONE_API_KEY")

# Loading Helper functions and embedding model
extracted_data = load_pdf_file(data = 'data/')
text_chunks = text_split(extracted_data)
embedding = OpenAIEmbeddings(model = "text-embedding-3-small")

# Pinecone Vector Database
pc = Pinecone(api_key=pinecone_api_key)

index_name = "medicalbot"
pc.create_index(
    name=index_name,
    dimension=1536, # model dimensions
    metric="cosine", # model metric
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    ) 
)

# Embed each chunk and upsert the embeddings into pinecone index 
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks, 
    index_name=index_name,
    embedding=embedding
)

