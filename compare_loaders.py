"""Scratch benchmark: compare PDF extraction quality across loaders.

Run:  uv run python compare_loaders.py
"""
import time
from pathlib import Path

import pymupdf4llm
from langchain_community.document_loaders import (
    PDFPlumberLoader,
    PyMuPDFLoader,
    PyPDFLoader,
)

PDF = Path("src/data/hr_rag_data/hr_rag_data/policies/HR-POL-001_Leave_Policy_v3.0_CURRENT.pdf")
NEEDLE = "Paternity"          # lives inside the entitlement table
WINDOW = 400                   # chars of context to show around the needle


def show_around(text: str, needle: str = NEEDLE) -> str:
    i = text.find(needle)
    if i == -1:
        return f"<{needle!r} not found in extracted text>"
    start = max(0, i - 80)
    return text[start : i + WINDOW]


def bench_langchain(name: str, loader_cls) -> None:
    t = time.perf_counter()
    docs = loader_cls(str(PDF)).load()
    secs = time.perf_counter() - t
    full = "\n".join(d.page_content for d in docs)
    print(f"== {name} ".ljust(60, "="))
    print(f"   {len(docs)} docs | {len(full):,} chars | {secs:.2f}s")
    print(show_around(full))
    print()


def bench_pymupdf4llm() -> None:
    t = time.perf_counter()
    md = pymupdf4llm.to_markdown(str(PDF))
    secs = time.perf_counter() - t
    print(f"== pymupdf4llm (markdown) ".ljust(60, "="))
    print(f"   {len(md):,} chars | {secs:.2f}s")
    print(show_around(md))
    print()


if __name__ == "__main__":
    print(f"PDF: {PDF.name}\n")
    bench_langchain("PyPDFLoader", PyPDFLoader)
    bench_langchain("PyMuPDFLoader", PyMuPDFLoader)
    bench_langchain("PDFPlumberLoader", PDFPlumberLoader)
    bench_pymupdf4llm()
