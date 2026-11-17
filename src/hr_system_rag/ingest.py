"""One-shot ingestion: policies/ -> markdown -> chunks -> embeddings -> Qdrant.

Run:  uv run python -m hr_system_rag.ingest
"""
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from qdrant_client import models

from hr_system_rag.embeddings import get_embeddings
from hr_system_rag.loaders import chunk_documents, load_corpus

load_dotenv()

POLICIES_DIR = (
    Path(__file__).resolve().parents[2]
    / "src" / "data" / "hr_rag_data" / "policies"
)
COLLECTION_NAME = os.environ.get("QDRANT_COLLECTION", "aurelia_hr_v1")


def main() -> None:
    docs = load_corpus(POLICIES_DIR)
    chunks = chunk_documents(docs)
    print(f"{len(chunks)} chunks from {len(docs)} page-documents")

    QdrantVectorStore.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        url=os.environ["QDRANT_URL"],
        api_key=os.environ.get("QDRANT_API_KEY") or None,
        collection_name=COLLECTION_NAME,
        distance=models.Distance.COSINE,
        force_recreate=True,
    )
    print(f"Ingested into collection '{COLLECTION_NAME}'")


if __name__ == "__main__":
    main()
