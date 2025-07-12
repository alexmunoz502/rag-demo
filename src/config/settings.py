import os
from pathlib import Path

import openai


# ====[ Helpers ]======================================================================
def load_required_env_variable(variable_name: str) -> str:
    value = os.getenv(variable_name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: '{variable_name}'")
    return value


# ====[ Environment ]==================================================================

# Required
OPENAI_API_KEY = load_required_env_variable("OPENAI_API_KEY")
OPENAI_LLM_MODEL = load_required_env_variable("OPENAI_LLM_MODEL")
OPENAI_EMBEDDING_MODEL = load_required_env_variable("OPENAI_EMBEDDING_MODEL")

# Optional
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

# ====[ Settings ]=================================================================

openai.api_key = OPENAI_API_KEY

CHROMA_DIR = Path("./chroma_store")
COLLECTION_NAME = "docs"
