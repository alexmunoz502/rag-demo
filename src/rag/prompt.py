# ====[ Public API ]===================================================================


def build_system_prompt() -> str:
    return """
    You are an assistant that answers questions based only on the provided context.

    - If the context does not contain any relevant information, respond with:
      "Sorry, I can only answer questions related to the provided documents."

    - If no context is provided at all, respond with:
      "No documents were available to answer this question."

    Do not use any external knowledge. Only use the context given to you.
    """


def build_user_prompt(context_chunks: list[str], question: str) -> str:
    context = "\n\n".join(context_chunks) if context_chunks else "No Context"
    return f"""
        Context: {context}

        Question: {question}

        Answer:
    """
