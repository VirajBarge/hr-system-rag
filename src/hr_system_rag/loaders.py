"""Turn the files in the corpus folder into chunked LangChain Documents."""
import re
from pathlib import Path

import pymupdf4llm
from langchain_community.document_loaders import CSVLoader, TextLoader
from langchain_core.documents import Document
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

SCAN_FOLDERS = {"scans"}      # PDFs kept here are images, so they need OCR

# stage 1: split markdown on headers (h1/h2/h3 land in each chunk's metadata)
md_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=[("#", "h1"), ("##", "h2"), ("###", "h3")],
    strip_headers=False,       # keep the header line inside the chunk text
)
# stage 2: cap size; overlap rescues sentences cut mid-way inside a section
rec_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=150)


def _pdf(path: Path) -> list[Document]:
    if path.parent.name in SCAN_FOLDERS:
        from langchain_community.document_loaders import UnstructuredPDFLoader

        return UnstructuredPDFLoader(str(path), mode="elements", strategy="ocr_only").load()
    docs = []
    for page in pymupdf4llm.to_markdown(str(path), page_chunks=True):
        docs.append(Document(
            page_content=page["text"],
            metadata={"page": page["metadata"].get("page_number"), "format": "markdown"},
        ))
    return docs


def _doc_id(name: str) -> str:
    m = re.search(r"HR-[A-Z]+-\d+(?:-\d+)?", name)   # HR-POL-001, HR-CIR-2026-014
    return m.group(0) if m else name.split("_")[0]


LOADER_FOR = {
    ".pdf": _pdf,
    ".md": lambda p: TextLoader(str(p), encoding="utf-8").load(),
    ".txt": lambda p: TextLoader(str(p), encoding="utf-8").load(),
    ".csv": lambda p: CSVLoader(str(p), encoding="utf-8").load(),
}


def load_file(path: Path) -> list[Document]:
    docs = LOADER_FOR[path.suffix.lower()](path)
    for doc in docs:
        doc.metadata.update(
            source=str(path),
            filename=path.name,
            doc_id=_doc_id(path.name),           # HR-POL-001, HR-CIR-2026-014, ...
            area=path.parent.name,               # policies, circulars, forms ...
            doc_type=path.suffix.lstrip(".").lower(),
            status=("superseded" if ("ARCHIVE" in path.name or "SUPERSEDED" in path.name)
                    else "current"),
        )
    return docs


def load_corpus(root: Path) -> list[Document]:
    docs, failed = [], []
    for path in sorted(root.rglob("*")):
        if path.suffix.lower() not in LOADER_FOR:
            continue
        try:
            docs.extend(load_file(path))
        except Exception as exc:                 # keep going, report at the end
            failed.append(f"{path.name}: {exc}")
    print(f"Loaded {len(docs)} documents from {root}")
    for line in failed:
        print("  skipped", line)
    return docs


def _prepend_context(doc: Document) -> None:
    """Metadata isn't embedded — only page_content is. Give the vector the
    doc id + section path so retrieval (and citations) can see it."""
    crumbs = [doc.metadata.get(k) for k in ("doc_id", "h1", "h2", "h3")]
    trail = " > ".join(str(c) for c in crumbs if c)
    if trail:
        doc.page_content = f"{trail}\n\n{doc.page_content}"


def chunk_documents(docs: list[Document]) -> list[Document]:
    chunks = []
    for doc in docs:
        if doc.metadata.get("format") == "markdown":
            pieces = md_splitter.split_text(doc.page_content)      # per section
            pieces = rec_splitter.split_documents(pieces)          # per size cap
        elif doc.metadata.get("doc_type") == "csv":
            pieces = [doc]                                         # a row IS a chunk
        else:
            pieces = rec_splitter.split_documents([doc])
        for i, piece in enumerate(pieces):
            piece.metadata.update(doc.metadata)                    # restore file-level fields
            piece.metadata["chunk_index"] = i                      # position within its doc
            _prepend_context(piece)
        chunks.extend(pieces)
    return chunks
