from src.utils import *
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")

# For split, embedding and storing the index 
def vector_store():
    embedding = embedder()
    llm = llm_load()
    documents = load_documents("data")
    splitter = split_documents()
    index = VectorStoreIndex(documents, transformations=[splitter], llm=llm, embed_model=embedding)
    
    index.storage_context.persist() # Storing the index
    return index

vector_store()


