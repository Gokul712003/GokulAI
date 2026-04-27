"""
Generates 200 synthetic Q&A pairs from master_bio.md using GPT-4o mini.
Run: python -m gokulaai.data_generator
"""
import json
import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from rich.console import Console
from rich.table import Table

load_dotenv()

KNOWLEDGE_DIR = Path(__file__).parent.parent / "knowledge"
OUTPUT_FILE = KNOWLEDGE_DIR / "qa_dataset.json"

console = Console()

BATCH_PROMPTS = {
    "technical": (
        50,
        "Generate exactly 50 Q&A pairs about TECHNICAL DEPTH only. "
        "Questions like: How does X work? What was hard about Y? Why did you choose Z technology? "
        "How did you implement structured output validation? What is LangGraph and how did you use it? "
        "Answers must be specific, detailed, first-person as Gokul. "
        'Return a JSON object: {"items": [...]}. Each item: '
        '{"question":"...","answer":"...","category":"technical","topics":["..."]}. Exactly 50 items.'
    ),
    "project": (
        50,
        "Generate exactly 50 Q&A pairs about PROJECT SPECIFICS only. "
        "Questions like: What does ClauseGuard do? How does PulseIQ detect drift? "
        "What's the architecture of the AI Therapist? What tech stack did you use? "
        "Cover ClauseGuard, PulseIQ, AI Therapist, and Portfolio AI Assistant equally. "
        "Answers must be specific, detailed, first-person as Gokul. "
        'Return a JSON object: {"items": [...]}. Each item: '
        '{"question":"...","answer":"...","category":"project","topics":["..."]}. Exactly 50 items.'
    ),
    "career": (
        40,
        "Generate exactly 40 Q&A pairs about CAREER & AVAILABILITY only. "
        "Questions like: Are you available? What salary? What roles? Can you start immediately? "
        "Remote vs onsite? Notice period? Why AI/ML? What's your 5-year plan? "
        "Answers must be specific, confident, first-person as Gokul. "
        'Return a JSON object: {"items": [...]}. Each item: '
        '{"question":"...","answer":"...","category":"career","topics":["..."]}. Exactly 40 items.'
    ),
    "personal": (
        30,
        "Generate exactly 30 Q&A pairs about PERSONAL BACKGROUND only. "
        "Questions like: Where did you study? What's your CGPA? Where are you from? "
        "Tell me about your internship. What's your publication about? "
        "Answers must be specific, accurate, first-person as Gokul. "
        'Return a JSON object: {"items": [...]}. Each item: '
        '{"question":"...","answer":"...","category":"personal","topics":["..."]}. Exactly 30 items.'
    ),
    "behavioral": (
        30,
        "Generate exactly 30 Q&A pairs about BEHAVIORAL questions only. "
        "Questions like: Tell me about a hard problem you solved. How do you debug? "
        "How do you learn new technologies? Describe a time you iterated many times. "
        "What motivates you? How do you handle ambiguity? "
        "Answers must be specific, story-driven, first-person as Gokul. "
        'Return a JSON object: {"items": [...]}. Each item: '
        '{"question":"...","answer":"...","category":"behavioral","topics":["..."]}. Exactly 30 items.'
    ),
}


def load_bio() -> str:
    bio_path = KNOWLEDGE_DIR / "master_bio.md"
    return bio_path.read_text(encoding="utf-8")


def load_pdfs() -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        return ""

    pdf_text = ""
    for pdf_path in KNOWLEDGE_DIR.glob("*.pdf"):
        reader = PdfReader(str(pdf_path))
        for page in reader.pages:
            pdf_text += page.extract_text() or ""
    return pdf_text


def _call_batch(client: OpenAI, context: str, category: str, prompt: str) -> list[dict]:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"Here is Gokul's bio:\n\n{context}"},
        ],
        temperature=0.7,
        max_tokens=8000,
        response_format={"type": "json_object"},
    )
    raw = response.choices[0].message.content
    data = json.loads(raw)
    if isinstance(data, dict):
        items = data.get("items") or data.get("qa_pairs") or data.get("dataset") or next(iter(data.values()))
    else:
        items = data
    return items


def generate_qa_dataset() -> list[dict]:
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    bio = load_bio()
    pdf_text = load_pdfs()

    context = bio
    if pdf_text.strip():
        context += f"\n\n## Resume / Additional Documents\n{pdf_text[:6000]}"

    all_pairs: list[dict] = []

    for category, (expected_count, prompt) in BATCH_PROMPTS.items():
        console.print(f"[cyan]Generating {expected_count} {category} pairs...[/cyan]")
        batch = _call_batch(client, context, category, prompt)
        console.print(f"  [green]Got {len(batch)} pairs[/green]")
        all_pairs.extend(batch)

    OUTPUT_FILE.write_text(json.dumps(all_pairs, indent=2, ensure_ascii=False), encoding="utf-8")

    dist: dict[str, int] = {}
    for item in all_pairs:
        cat = item.get("category", "unknown")
        dist[cat] = dist.get(cat, 0) + 1

    table = Table(title=f"Generated {len(all_pairs)} Q&A pairs", show_header=True)
    table.add_column("Category", style="cyan")
    table.add_column("Count", style="green", justify="right")
    for cat, count in sorted(dist.items()):
        table.add_row(cat, str(count))

    console.print(table)
    console.print(f"[green]Saved to {OUTPUT_FILE}[/green]")

    return all_pairs


if __name__ == "__main__":
    generate_qa_dataset()
