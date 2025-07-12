import openai

from src.config import settings
from src.rag import prompt, store
from src.utils import log

# ====[ Configuration ]================================================================


logger = log.get_logger(__name__)


# ====[ Private API ]==================================================================


def _embed_query(query: str) -> list[float]:
    response = openai.embeddings.create(
        model=settings.OPENAI_EMBEDDING_MODEL, input=[query]
    )
    return response.data[0].embedding


def _retrieve_chunks(query_embedding: list[float], k: int) -> list[str]:
    results = store.collection.query(query_embeddings=[query_embedding], n_results=k)

    if results is None or results["documents"] is None:
        logger.error("results or result documents is None")
        return []

    context_chunks = results["documents"][0]
    return context_chunks


def _generate_response(context_chunks: list[str], user_question: str) -> str:
    user_prompt = prompt.build_user_prompt(context_chunks, user_question)

    completion = openai.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {"role": "system", "content": prompt.build_system_prompt()},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.3,
    )

    answer = completion.choices[0].message.content
    return answer or ""


# ====[ Public API ]===================================================================


def query_docs(query: str) -> str:
    logger.info(f"Processing query: '{query}'")

    query_embedding = _embed_query(query)
    context_chunks = _retrieve_chunks(query_embedding, k=3)
    response = _generate_response(context_chunks, query)

    return response
