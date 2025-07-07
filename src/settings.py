import os


# ====[ Helpers ]======================================================================
def load_required_env_variable(variable_name: str) -> str:
    value = os.getenv(variable_name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: '{variable_name}'")
    return value


# ====[ Environment ]==================================================================

OPENAI_API_KEY = load_required_env_variable("OPENAI_API_KEY")
OPENAI_LLM_MODEL = load_required_env_variable("OPENAI_LLM_MODEL")
OPENAI_EMBEDDING_MODEL = load_required_env_variable("OPENAI_EMBEDDING_MODEL")
