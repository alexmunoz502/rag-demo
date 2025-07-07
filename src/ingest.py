import os
from pathlib import Path
from tqdm import tqdm

import openai
import chromadb
import settings


# ====[ Environment ]==================================================================
openai.api_key = os.environ.get("UV_OPENAI_API_KEY")

# ====[ Configuration ]================================================================
CHROMA_DIR = Path("./chroma_store")
DOCS_COLLECTION_NAME = "docs"
DATA_DIR = Path("./data")
CHUNK_SIZE = 500
OVERLAP = 200

chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
docs_collection = chroma_client.get_or_create_collection(name=DOCS_COLLECTION_NAME)


# ====[ Private API ]==================================================================
def _read_documents() -> list[tuple[str, str]]:
    # TODO: is this prone to OOM errors if docs are too large?
    docs = []
    for filename in DATA_DIR.glob("*.md"):
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
            docs.append((file.name, text))
    return docs


def _chunk_text(
    text: str, chunk_size: int = CHUNK_SIZE, overlap: int = OVERLAP
) -> list:
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks


def _embed_texts(texts: list[str]) -> list:
    response = openai.embeddings.create(
        model=settings.OPENAI_EMBEDDING_MODEL, input=texts
    )
    return [item.embedding for item in response.data]


# ====[ Public API ]===================================================================
def main() -> None:
    documents = _read_documents()
    chunk_id = 0

    for doc_name, text in documents:
        chunks = _chunk_text(text)
        # TODO: upgrade to log or something
        print(f"Ingesting {doc_name} with {len(chunks)} chunks....")

        for i in tqdm(range(0, len(chunks), 20)):
            batch = chunks[i : i + 20]
            embeddings = _embed_texts(batch)
            ids = [f"{doc_name}-{chunk_id + j}" for j in range(len(batch))]
            metadatas = [
                {"source": doc_name} for _ in batch
            ]  # TODO: change this to use MetaData type?

            docs_collection.add(
                documents=batch, embeddings=embeddings, metadatas=metadatas, ids=ids
            )
            chunk_id += len(batch)

    # TODO: upgrade to log or something
    print("✅ Ingestion complete.")


def ingest_text(text: str, source_id: str) -> None:
    chunks = _chunk_text(text)
    # TODO: upgrade to log or something
    print(f"Ingesting {source_id} with {len(chunks)} chunks....")

    chunk_id = 0
    for i in tqdm(range(0, len(chunks), 20)):
        batch = chunks[i : i + 20]
        embeddings = _embed_texts(batch)
        ids = [f"{source_id}-{chunk_id + j}" for j in range(len(batch))]
        metadatas = [
            {"source": source_id} for _ in batch
        ]  # TODO: change this to use MetaData type?

        docs_collection.add(
            documents=batch, embeddings=embeddings, metadatas=metadatas, ids=ids
        )
        chunk_id += len(batch)

    print(f"Ingested {source_id}")


if __name__ == "__main__":
    if "docs" in [c.name for c in chroma_client.list_collections()]:
        print("Dropping docs collection")
        chroma_client.delete_collection("docs")
        docs_collection = chroma_client.get_or_create_collection(
            name=DOCS_COLLECTION_NAME
        )

    main()
