import chromadb

from src.config import settings


client = chromadb.PersistentClient(path=settings.CHROMA_DIR)
collection = client.get_or_create_collection(name=settings.COLLECTION_NAME)
