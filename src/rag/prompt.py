# ====[ Public API ]===================================================================


def build_system_prompt() -> str:
    return """
    You are an assistant that answers questions based only on the following context.
    Try to answer the question only if it is clearly related to the provided context.
    If it's completely unrelated, respond with:
    'Sorry, I can only answer questions related to the provided documents.'
    """


def build_user_prompt(context_chunks: list[str], question: str) -> str:
    context = "\n\n".join(context_chunks)
    return f"""
        Context: {context}

        Question: {question}

        Answer:
    """
