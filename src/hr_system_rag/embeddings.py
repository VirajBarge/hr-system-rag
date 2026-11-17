import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

EMBEDDING_MODEL = os.environ.get("EMBEDDING_MODEL", "nvidia/nemotron-3.5-embed-1b:free")
# Optional: truncate vectors (like OpenAI's dimensions=256). Empty = model's
# native size (2048 for embed-1b, 4096 for embed-8b).
EMBEDDING_DIMENSIONS = os.environ.get("EMBEDDING_DIMENSIONS")


def get_embeddings() -> OpenAIEmbeddings:
    kwargs = {}
    if EMBEDDING_DIMENSIONS:
        kwargs["dimensions"] = int(EMBEDDING_DIMENSIONS)
    # check_embedding_ctx_length=False -> send raw strings; NVIDIA's endpoint
    # rejects the tiktoken token-ID arrays LangChain sends otherwise.
    return OpenAIEmbeddings(
        model=EMBEDDING_MODEL, check_embedding_ctx_length=False, **kwargs
    )
