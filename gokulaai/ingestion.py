"""
Embeds and ingests knowledge base into ChromaDB.
Run: python -m gokulaai.ingestion
"""
import json
import os
from pathlib import Path

import chromadb
import tiktoken
from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.progress import track

load_dotenv()

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"
CHROMA_DIR = Path(__file__).parent.parent / "chroma_db"
COLLECTION_NAME = "gokulaai_knowledge"
EMBED_MODEL = "text-embedding-3-small"
CHUNK_TOKENS = 500
CHUNK_OVERLAP = 50

console = Console()


def _embed_batch(client: OpenAI, texts: list[str]) -> list[list[float]]:
    resp = client.embeddings.create(model=EMBED_MODEL, input=texts)
    return [e.embedding for e in resp.data]


def _chunk_text_by_tokens(text: str, max_tokens: int, overlap: int) -> list[str]:
    enc = tiktoken.get_encoding("cl100k_base")
    tokens = enc.encode(text)
    chunks = []
    start = 0
    while start < len(tokens):
        end = min(start + max_tokens, len(tokens))
        chunk_tokens = tokens[start:end]
        chunks.append(enc.decode(chunk_tokens))
        if end == len(tokens):
            break
        start += max_tokens - overlap
    return chunks


def load_qa_pairs() -> list[tuple[str, dict]]:
    qa_path = KNOWLEDGE_DIR / "qa_dataset.json"
    if not qa_path.exists():
        console.print("[yellow]qa_dataset.json not found — skipping Q&A pairs[/yellow]")
        return []
    pairs = json.loads(qa_path.read_text(encoding="utf-8"))
    chunks = []
    for item in pairs:
        text = f"Q: {item['question']}\nA: {item['answer']}"
        meta = {
            "source": "qa_dataset",
            "category": item.get("category", "general"),
            "topics": json.dumps(item.get("topics", [])),
        }
        chunks.append((text, meta))
    return chunks


def load_bio_sections() -> list[tuple[str, dict]]:
    bio_path = KNOWLEDGE_DIR / "master_bio.md"
    if not bio_path.exists():
        return []
    content = bio_path.read_text(encoding="utf-8")
    sections = []
    current_header = "intro"
    current_text = []
    for line in content.splitlines():
        if line.startswith("## "):
            if current_text:
                sections.append((current_header, "\n".join(current_text).strip()))
            current_header = line.lstrip("#").strip()
            current_text = [line]
        else:
            current_text.append(line)
    if current_text:
        sections.append((current_header, "\n".join(current_text).strip()))

    chunks = []
    for header, text in sections:
        if not text.strip():
            continue
        # Split FAQ sections into per-entry chunks for better retrieval precision
        if "frequently asked questions" in header.lower() or "faq" in header.lower():
            # Each FAQ entry starts with "Q:"
            import re as _re
            entries = _re.split(r"\n(?=Q:)", text)
            for entry in entries:
                entry = entry.strip()
                if entry.startswith("Q:") and "A:" in entry:
                    meta = {"source": "master_bio", "category": "faq", "topics": json.dumps(["FAQ", header])}
                    chunks.append((entry, meta))
        else:
            meta = {"source": "master_bio", "category": "bio", "topics": json.dumps([header])}
            chunks.append((text, meta))
    return chunks


def load_pdf_chunks() -> list[tuple[str, dict]]:
    try:
        from pypdf import PdfReader
    except ImportError:
        return []

    chunks = []
    for pdf_path in KNOWLEDGE_DIR.glob("*.pdf"):
        reader = PdfReader(str(pdf_path))
        full_text = ""
        for page in reader.pages:
            full_text += (page.extract_text() or "") + "\n"

        text_chunks = _chunk_text_by_tokens(full_text, CHUNK_TOKENS, CHUNK_OVERLAP)
        for i, chunk in enumerate(text_chunks):
            if chunk.strip():
                meta = {
                    "source": pdf_path.name,
                    "category": "resume",
                    "topics": json.dumps(["resume", pdf_path.stem]),
                }
                chunks.append((chunk, meta))
    return chunks


def ingest_knowledge_base() -> None:
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    chroma_client = chromadb.PersistentClient(path=str(CHROMA_DIR))

    # Drop and recreate for a clean ingest
    try:
        chroma_client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass
    collection = chroma_client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    all_chunks: list[tuple[str, dict]] = []

    console.print("[cyan]Loading Q&A pairs...[/cyan]")
    all_chunks.extend(load_qa_pairs())
    console.print(f"  {len(all_chunks)} Q&A chunks")

    console.print("[cyan]Loading bio sections...[/cyan]")
    bio_chunks = load_bio_sections()
    all_chunks.extend(bio_chunks)
    console.print(f"  {len(bio_chunks)} bio chunks")

    console.print("[cyan]Loading PDF chunks...[/cyan]")
    pdf_chunks = load_pdf_chunks()
    all_chunks.extend(pdf_chunks)
    console.print(f"  {len(pdf_chunks)} PDF chunks")

    console.print(f"[bold]Total: {len(all_chunks)} chunks to embed[/bold]")

    # Embed in batches of 100
    BATCH = 100
    ids, embeddings, documents, metadatas = [], [], [], []

    batches = [all_chunks[i : i + BATCH] for i in range(0, len(all_chunks), BATCH)]
    for batch_idx, batch in enumerate(track(batches, description="Embedding...")):
        texts = [text for text, _ in batch]
        metas = [meta for _, meta in batch]
        vecs = _embed_batch(client, texts)
        for j, (text, meta, vec) in enumerate(zip(texts, metas, vecs)):
            idx = batch_idx * BATCH + j
            ids.append(f"chunk_{idx}")
            embeddings.append(vec)
            documents.append(text)
            metadatas.append(meta)

    collection.add(
        ids=ids,
        embeddings=embeddings,
        documents=documents,
        metadatas=metadatas,
    )

    console.print(f"[bold green]Ingested {len(ids)} chunks into ChromaDB collection '{COLLECTION_NAME}'[/bold green]")


if __name__ == "__main__":
    ingest_knowledge_base()
