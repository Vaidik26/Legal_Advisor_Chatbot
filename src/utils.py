from llama_index.core import SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core import Settings
from llama_index.core import StorageContext, load_index_from_storage
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# LLM loading
def llm_load():
    model="gemini-2.5-flash"
    llm = GoogleGenAI(model=model)
    Settings.llm = llm
    return llm

# Load documents from a directory
def load_documents(directory_path):
    documents = SimpleDirectoryReader(directory_path).load_data()
    return documents

# Embed documents
def embedder():
    Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    return Settings.embed_model
    

# Split documents into chunks
def split_documents():
    splitter = SentenceSplitter(chunk_size=1000, chunk_overlap=150)
    return splitter

# Loading the index
def load_vector():
    embedding = embedder()
    storage_context = StorageContext.from_defaults(persist_dir="./storage")
    index = load_index_from_storage(storage_context, embed_model=embedding)
    return index
    