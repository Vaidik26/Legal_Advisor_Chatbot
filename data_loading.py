from src.vector_store import vector_store
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


if __name__ == "__main__":
    vector_store()