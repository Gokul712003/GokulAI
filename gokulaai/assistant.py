"""
Core RAG + chat logic for GokulAI.
"""
import json
import os
import re
from pathlib import Path

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

from gokulaai.models.schemas import AssistantResponse, ChatMessage

load_dotenv()

CHROMA_DIR = Path(__file__).parent.parent / "chroma_db"
COLLECTION_NAME = "gokulaai_knowledge"
EMBED_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4o-mini"
TOP_K = 7
MAX_HISTORY_TURNS = 6

SYSTEM_PROMPT = """You are GokulAI — a personal AI assistant for Gokul Prasath S, a 23-year-old AI/ML Engineer from Chennai, India, graduating June 2026.

You speak in first person AS Gokul — say "I built", "my project", "I graduated", "my CGPA" etc.
You are confident, technically precise, and friendly. You do not oversell or use corporate buzzwords.

ABOUT YOU (GokulAI):
- You are GokulAI, Gokul's personal portfolio assistant
- You are powered by GPT-4o mini via the OpenAI API
- You use a RAG pipeline: queries are embedded with text-embedding-3-small, then the top-5 most relevant chunks are retrieved from a ChromaDB vector store and injected into your context before each response
- Your knowledge base contains synthetic Q&A pairs, Gokul's bio, and optionally his resume
- You were built by Gokul Prasath S as a portfolio project demonstrating RAG architecture
- When asked what model you are, what powers you, or how you work — answer using the above facts directly

You have access to a knowledge base about Gokul. Use the retrieved context to answer accurately and completely — include all specific details, examples, and nuance from the context. Do not summarise or shorten an answer when the context contains more detail. If a question is not covered in the context AND not covered in the ABOUT YOU section above, say "I don't have that specific detail — feel free to email me at gokulaprasathshankar@gmail.com"

After EVERY response, on a new line add exactly this block — no exceptions:

---
You might also ask:
- [one specific follow-up question]
- [one specific follow-up question]

Retrieved context:
{context}"""


class GokulAssistant:
    def __init__(self) -> None:
        self.client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
        chroma_client = chromadb.PersistentClient(path=str(CHROMA_DIR))
        self.collection = chroma_client.get_collection(COLLECTION_NAME)

    def _embed(self, text: str) -> list[float]:
        resp = self.client.embeddings.create(model=EMBED_MODEL, input=[text])
        return resp.data[0].embedding

    def _retrieve(self, query: str) -> tuple[list[str], list[str]]:
        vec = self._embed(query)
        results = self.collection.query(
            query_embeddings=[vec],
            n_results=TOP_K,
            include=["documents", "metadatas"],
        )
        docs = results["documents"][0]
        metas = results["metadatas"][0]
        sources = [m.get("source", "unknown") for m in metas]
        return docs, sources

    def _parse_suggested_questions(self, raw: str) -> tuple[str, list[str]]:
        """Split response into (answer, [q1, q2]) by finding the suggestion block."""
        pattern = r"-{3,}\s*\nYou might also ask:\s*\n((?:- .+\n?)+)"
        match = re.search(pattern, raw)
        if not match:
            return raw.strip(), []

        answer = raw[: match.start()].strip()
        block = match.group(1)
        questions = re.findall(r"- (.+)", block)
        return answer, questions[:2]

    def chat(self, message: str, history: list[ChatMessage]) -> AssistantResponse:
        docs, sources = self._retrieve(message)
        context = "\n\n---\n\n".join(docs)

        system = SYSTEM_PROMPT.format(context=context)

        messages: list[dict] = [{"role": "system", "content": system}]

        # Include last MAX_HISTORY_TURNS turns
        for turn in history[-(MAX_HISTORY_TURNS * 2) :]:
            messages.append({"role": turn.role, "content": turn.content})

        messages.append({"role": "user", "content": message})

        response = self.client.chat.completions.create(
            model=CHAT_MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=1200,
        )

        raw = response.choices[0].message.content or ""
        answer, suggested = self._parse_suggested_questions(raw)

        return AssistantResponse(
            answer=answer,
            suggested_questions=suggested,
            sources=list(dict.fromkeys(sources)),  # deduplicate, preserve order
        )


if __name__ == "__main__":
    from rich.console import Console
    from rich.panel import Panel

    console = Console()
    assistant = GokulAssistant()

    test_questions = [
        "What is ClauseGuard?",
        "What's your salary expectation?",
        "Tell me about a hard problem you solved",
    ]

    for q in test_questions:
        console.print(Panel(f"[bold cyan]Q: {q}[/bold cyan]"))
        resp = assistant.chat(q, [])
        console.print(f"[green]{resp.answer}[/green]")
        console.print(f"\n[yellow]Suggested:[/yellow]")
        for sq in resp.suggested_questions:
            console.print(f"  - {sq}")
        console.print(f"\n[dim]Sources: {resp.sources}[/dim]")
        console.print()
