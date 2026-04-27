# Gokul Prasath S — Master Bio

## Personal
- Full name: Gokul Prasath S
- Age: 23
- Location: Chennai, Tamil Nadu, India
- Email: gokulaprasathshankar@gmail.com
- GitHub: github.com/Gokul712003
- LinkedIn: linkedin.com/in/gokulaprasath
- Available: immediately for remote roles
- Target salary: ₹9–12 LPA (fresher)
- Target roles: AI/ML Engineer, LLM Engineer, Prompt Engineer, Agent Systems Engineer, anything AI/ML related

## Education
- M.Tech Computer Science (AI & ML)
  Vellore Institute of Technology, Chennai
  July 2024 – June 2026 (graduating June 2026)
  CGPA: 8.69
- B.Tech Computer Science (AI & ML)
  SRM Institute of Science and Technology
  2020 – June 2024
  CGPA: 9.09

## Work Experience
- AI Intern, Xerago eBiz, Chennai
  June 2023 – August 2023
  Built stock image generation pipeline using Stable Diffusion and Transformers.
  Automated image processing workflows.

## Publications
- "Visual Verse 2.0: Image Generation with Image Inpainting" — SPRINGER Conference Paper

## Projects

### ClauseGuard (Live — github.com/Gokul712003/ClauseGuard)
ClauseGuard is a production-grade contract analysis tool powered by a multi-agent LLM pipeline.
It processes legal contracts (PDFs) and extracts structured clause data with validation at every stage.
Architecture: document ingestion → clause extraction agent → risk assessment agent → structured output validator → report generator.
Uses Pydantic models for structured output validation to ensure every extracted clause meets a defined schema.
Tested on 500+ real contracts. Zero hallucinated clauses due to strict output validation.
Tech stack: Python, LangChain, GPT-4o, Pydantic, FastAPI, ChromaDB.
Key challenge: getting LLMs to produce consistent structured output across varied contract formats — solved with multi-turn validation and retry logic.

### PulseIQ (Live — github.com/Gokul712003/PulseIQ)
PulseIQ is a real-time market intelligence platform with a 5-agent pipeline.
Agents: scraper → data cleaner → analyst → trend detector → report writer.
Scrapes live financial and news data, detects anomalies and drift, generates plain-English reports.
Has a full CLI built with Typer — operators can run individual agents or the full pipeline.
14-iteration debugging session to fix scraper reliability under rate limits and anti-bot measures.
Tech stack: Python, LangGraph, GPT-4o mini, Typer, Rich, BeautifulSoup, pandas.
Built in under 7 days as a complete, working system.

### AI Therapist (Live)
Student mental health monitoring system using 3 fine-tuned LLMs with LangGraph checkpointers.
Privacy-first architecture.
Designed for university environments to detect early signs of distress and provide supportive responses.
Uses LangGraph state machines to manage multi-turn therapeutic conversations with memory.

### Portfolio AI Assistant (this project — Building)
RAG-based assistant that answers recruiter questions about Gokul. Uses ChromaDB for knowledge base, GPT-4o mini for responses.
Proactively suggests conversation topics.

## Personality & Working Style
- Builds production-grade systems, not tutorials
- Debugs systematically (14-iteration scraper fix on PulseIQ)
- Fast learner — built 2 complex projects in 7 days
- Prefers remote work, works independently
- Interested in: AI agents, LLM systems, automation, real-world AI applications

## About GokulAI
- I am GokulAI, Gokul's personal portfolio assistant
- Powered by GPT-4o mini via OpenAI API
- Built with RAG using ChromaDB vector store
- Knowledge base: Q&A pairs + resume + bio
- Built by Gokul Prasath S as a portfolio project demonstrating RAG architecture

## Frequently Asked Questions

Q: Are you open to relocation?
A: Prefer remote but open to discussion.

Q: Do you have a notice period?
A: No notice period — available immediately.

Q: What makes you different from other freshers?
A: I've shipped production-grade systems. ClauseGuard has structured output validation at every stage and was tested on 500+ real contracts. PulseIQ has a 5-agent pipeline with real scraping, real data, and a full CLI. Most freshers have tutorial projects. I have working tools.

Q: Can you work with a team?
A: Yes. Built both projects solo but understand collaborative workflows — git, code review, documentation (both projects have READMEs and clean commit history).

Q: What's your strongest technical skill?
A: Building multi-agent LLM pipelines with structured output validation. ClauseGuard and PulseIQ both demonstrate this.

Q: What model powers you?
A: I'm powered by GPT-4o mini with a RAG pipeline. My knowledge base lives in ChromaDB and gets retrieved via embedding similarity before each response.

Q: What are your future plans after graduation?
A: I want to join a team building real AI products — not research, not demos. I've been building production-grade agent systems as a student and I want to keep doing that professionally. ClauseGuard and PulseIQ are examples of what I want to keep building. Remote-first, AI-focused company is ideal.

Q: Are you considering a PhD?
A: Not right now. I want industry experience first — building real systems, not writing papers. Maybe later but not the immediate plan.
