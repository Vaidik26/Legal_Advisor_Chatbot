from src.utils import *
from llama_index.core import VectorStoreIndex, StorageContext, load_index_from_storage
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["HF_TOKEN"] = os.getenv("HF_TOKEN")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")




# For split, embedding and storing the index 
def vector_store():
    embedding = embedder()
    llm = llm_load()
    documents = load_documents("data")
    splitter = split_documents()
    index = VectorStoreIndex(documents, transformations=[splitter], llm=llm, embed_model=embedding)
    
    index.storage_context.persist() # Storing the index
    return index

# Loading the index
def load_vector():
    embedding = embedder()
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context, embed_model=embedding)
    return index

#vector_store()


