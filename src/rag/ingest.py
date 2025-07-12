from tqdm import tqdm

import openai
import chromadb

from src.config import settings
from src.rag.store import collection
from src.utils import log

# ====[ Configuration ]================================================================


DEFAULT_CHUNK_SIZE = 500
DEFAULT_OVERLAP = 200

logger = log.get_logger(__name__)


# ====[ Private API ]==================================================================


def _embed_texts(texts: list[str]) -> list:
    response = openai.embeddings.create(
        model=settings.OPENAI_EMBEDDING_MODEL, input=texts
    )
    return [item.embedding for item in response.data]


def _embed_and_store(chunks: list[str], source_id: str) -> None:
    chunk_id = 0
    for i in tqdm(range(0, len(chunks), 20)):
        batch = chunks[i : i + 20]
        embeddings = _embed_texts(batch)
        ids = [f"{source_id}-{chunk_id + j}" for j in range(len(batch))]
        metadatas: chromadb.Metadatas = [{"source": source_id} for _ in batch]

        collection.add(
            documents=batch, embeddings=embeddings, metadatas=metadatas, ids=ids
        )
        chunk_id += len(batch)


def _chunk_text(
    text: str, chunk_size: int = DEFAULT_CHUNK_SIZE, overlap: int = DEFAULT_OVERLAP
) -> list[str]:
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks


# ====[ Public API ]===================================================================


def ingest_text(
    text: str,
    source_id: str,
) -> None:
    logger.info(f"Ingesting {source_id}")
    chunks = _chunk_text(text)
    _embed_and_store(chunks, source_id)
