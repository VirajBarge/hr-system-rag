import os

from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_qdrant import QdrantVectorStore
from qdrant_client import QdrantClient, models

from hr_system_rag.embeddings import get_embeddings

load_dotenv()

COLLECTION_NAME = os.environ.get("QDRANT_COLLECTION", "aurelia_hr_v1")

vector_store = QdrantVectorStore(
    client=QdrantClient(
        url=os.environ["QDRANT_URL"],
        # api_key=os.environ.get("QDRANT_API_KEY"),
    ),
    collection_name=COLLECTION_NAME,
    embedding=get_embeddings(),
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are the HR assistant for Aurelia Systems Pvt. Ltd. "
               "Answer only from the supplied context. "
               "Do not invent policy entitlements, dates, or amounts. "
               "Cite document IDs (e.g., HR-POL-001). "
               "If the context does not contain the answer, say so and "
               "suggest raising a ticket via PeopleHub > Help."),
    ("human", "Question: {question}\nContext:\n{context}"),
])

chain = prompt | ChatOpenAI(model="nvidia/nemotron-3.5-super-vl:free", temperature=0) | StrOutputParser()

CURRENT_ONLY = models.Filter(must=[models.FieldCondition(
    key="metadata.status", match=models.MatchValue(value="current"))])


def retrieve(question: str, k: int = 5):
    return vector_store.similarity_search_with_score(question, k=k, filter=CURRENT_ONLY)


def answer(question: str, k: int = 5) -> str:
    results = retrieve(question, k=k)
    context = "\n\n".join(doc.page_content for doc, _ in results)
    return chain.invoke({"question": question, "context": context})
