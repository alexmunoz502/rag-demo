import os
from pathlib import Path

import openai
import chromadb

# ====[ Environment ]==================================================================
openai.api_key = os.environ.get("UV_OPENAI_API_KEY")

# ====[ Configuration ]================================================================
# TODO: Move env and configuration stuff to a centralized location
CHROMA_DIR = Path("./chroma_store")
DOCS_COLLECTION_NAME = "docs"
DATA_DIR = Path("./data")

chroma_client = chromadb.PersistentClient(path=CHROMA_DIR)
docs_collection = chroma_client.get_or_create_collection(name=DOCS_COLLECTION_NAME)


# ====[ Private API ]==================================================================
def _build_prompt(context_chunks: list[str], question: str) -> str:
    context = "\n\n".join(context_chunks)
    # TODO: make this prompt my own
    return f"""
        You are an assistant that answers questions based only on the following context.
        Try to answer the question only if it is clearly related to the provided context. If it's completely unrelated, respond with: 'Sorry, I can only answer questions related to the provided documents.'

        Context:
        {context}

        Question: {question}

        Answer:
    """


def _embed_query(query: str) -> list[float]:
    response = openai.embeddings.create(model="text-embedding-ada-002", input=[query])
    return response.data[0].embedding


# TODO: What is k=3?
def _query_docs(user_question: str, k=5) -> str | None:
    query_embedding = _embed_query(user_question)

    results = docs_collection.query(query_embeddings=[query_embedding], n_results=k)

    if results is None or results["documents"] is None:
        # TODO: refactor
        print("Error: results or results documents is None")
        return

    context_chunks = results["documents"][0]
    prompt = _build_prompt(context_chunks, user_question)

    # TODO: understand this
    completion = openai.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3,
    )

    answer = completion.choices[0].message.content
    return answer


# ====[ Public API ]===================================================================
def query_docs(query: str) -> str:
    print(f"Processing Query: {query}")
    answer = _query_docs(query)
    return answer or ""


def main() -> None:
    print("🔍 Ask me something about your documents:")
    user_input = input(">> ")
    answer = _query_docs(user_input)
    print("\n🧠 Answer:")
    print(answer)


if __name__ == "__main__":
    main()
