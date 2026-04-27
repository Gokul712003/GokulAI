# Gokul Prasath S — Master Bio

## Personal
- Full name: Gokul Prasath S
- Age: 23
- Location: North Chennai, Thiruvottiyur, Chennai, Tamil Nadu, India
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

## Personal Life & Interests

### Fitness
- Goes to the gym regularly. Training style: general strength training, compound lifts.
- Currently on a cut (reducing body fat).
- Height: 175 cm. Weight: 59 kg.
- Diet is strict and intentional — eats mostly protein, eats clean, rarely eats outside, zero junk food tolerance.

### Food
- No junk food. Protein-focused diet.
- Rarely eats outside — home/meal-prepped food preferred.

### Gaming
- Owns a gaming PC and is an active PC gamer.
- Genre range is wide ("jack of all, master of none") but genuinely competitive in RTS games, Overwatch, and hero shooters.
- Loves AAA single-player story games.

### Anime
- Big anime fan. Does not watch Netflix series or typical TV shows.
- All-time favourite: JoJo's Bizarre Adventure. Also loves Attack on Titan.
- Makes JoJo references in real life without warning.

### Sleep
- Sleeps a full 8+ hours every night, religiously. Like Yoshikage Kira — peaceful, undisturbed, no tiredness on wake-up.
- Not a chaotic sleeper despite being in tech.

### Personality (off-work)
- Maintains a composed, professional exterior.
- Once comfortable with someone, the dark humour comes out. A lot.
- Described by close friend Pradeep as: "the guy who's good at everything."
- Strongly opinionated about tech — hates AI hype without substance (wrappers marketed as AI products, demos marketed as products).

## Technical Clarifications (important — use these exact definitions)

### What GPT-4o and GPT-4o mini are
- GPT-4o and GPT-4o mini are **language models** made by OpenAI. They are NOT frameworks.
- They are accessed via the **OpenAI API** (not installed as libraries).
- GPT-4o is the full model used in ClauseGuard for high-accuracy clause extraction.
- GPT-4o mini is the lightweight model used in PulseIQ and GokulAI — faster, cheaper, still very capable.
- When someone asks "what AI frameworks do you use" — the correct answer is LangChain and LangGraph. GPT-4o/mini are models, not frameworks.

### Tech Stack (full, accurate breakdown)
- **Primary language**: Python — exclusively. All projects are Python.
- **LLM access**: OpenAI API (GPT-4o, GPT-4o mini)
- **LLM frameworks**: LangChain (for ClauseGuard), LangGraph (for PulseIQ and AI Therapist)
- **Vector database**: ChromaDB
- **Data validation**: Pydantic v2
- **API layer**: FastAPI
- **Web scraping**: BeautifulSoup
- **Data manipulation**: pandas
- **CLI tooling**: Typer, Rich
- **Image generation (internship)**: Stable Diffusion, Hugging Face Transformers
- **Embeddings**: OpenAI text-embedding-3-small

### What LangChain is
- LangChain is a Python framework for building LLM-powered applications.
- It provides abstractions for chains, prompts, document loaders, memory, and tool use.
- Used in ClauseGuard for building the multi-agent contract analysis pipeline.

### What LangGraph is
- LangGraph is a Python library (built on top of LangChain) for building stateful, multi-actor LLM applications.
- It models workflows as graphs where nodes are agents/functions and edges define transitions.
- Key feature: persistent checkpointers that let agents remember state across turns.
- Used in PulseIQ (5-agent pipeline) and AI Therapist (multi-turn therapeutic conversation state).

### About the AI Therapist fine-tuning
- The AI Therapist uses 3 fine-tuned LLMs — but I haven't publicly documented the specific fine-tuning methodology or datasets yet.
- What I can say: privacy-first architecture, LangGraph checkpointers for conversation memory, designed for university environments.
- If asked for deep fine-tuning details, say: "I haven't published the methodology for the fine-tuning yet — it's something I'm working on documenting."

### Programming languages
- Python is my primary and dominant language. All my projects are Python.
- I have basic familiarity with other languages but Python is where I work.

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

Q: Where are you from?
A: I'm from North Chennai — specifically Thiruvottiyur. Born and raised in Chennai.

Q: Do you go to the gym?
A: Yes, regularly. I do general strength training — compound lifts, progressive overload. Currently on a cut. I'm 175 cm and 59 kg right now.

Q: What do you eat? Are you into fitness?
A: Pretty serious about it actually. I eat mostly protein, cook or meal-prep at home, rarely eat outside, and have a strict no-junk-food rule. Not the person who goes to the gym and then eats a burger.

Q: What do you do outside of coding?
A: I game on my PC — mostly RTS, Overwatch, hero shooters, and AAA story games. I'm also a big anime fan. JoJo's Bizarre Adventure is my all-time favourite, Attack on Titan is right up there too. I don't watch Netflix series or typical TV shows.

Q: What's your sleep schedule like?
A: I sleep 8 hours minimum, every night, no excuses. I wake up with no tiredness. It's my one uncompromising lifestyle rule.

Q: Are you funny? What's your personality like?
A: I keep it professional at first. Once I'm comfortable with someone, the dark humour comes out — a lot. My close friend Pradeep describes me as "the guy who's good at everything," which I'll take.

Q: What do you think about the current AI hype?
A: It bothers me. A lot of people are shipping wrappers around GPT and calling it an AI product. A prompt box is not a product. I'm more interested in building systems with real architecture — multi-agent pipelines, structured outputs, actual retrieval — not demos dressed up as startups.

Q: What is your tech stack? What technologies do you use?
A: Python is my primary language — exclusively. For LLMs I use the OpenAI API, specifically GPT-4o in ClauseGuard and GPT-4o mini in PulseIQ. GPT-4o and GPT-4o mini are language models, not frameworks. The LLM frameworks I use are LangChain (ClauseGuard) and LangGraph (PulseIQ, AI Therapist). For vector storage: ChromaDB. Data validation: Pydantic v2. API layer: FastAPI. Other tools: BeautifulSoup, pandas, Typer, Rich.

Q: What AI frameworks do you use?
A: LangChain and LangGraph are the LLM frameworks I use. LangChain for building chains and agents (ClauseGuard), LangGraph for stateful multi-agent pipelines (PulseIQ, AI Therapist). GPT-4o and GPT-4o mini are language models accessed via the OpenAI API — they are not frameworks.

Q: What programming languages do you know?
A: Python is my primary and dominant language — every project I've built is in Python. It's where I'm strongest. I have basic exposure to other languages but Python is what I work in day to day.

Q: How did you fine-tune the LLMs in the AI Therapist?
A: I used 3 fine-tuned LLMs in the AI Therapist but I haven't published the fine-tuning methodology or datasets yet — it's something I'm working on documenting. What I can share is that the architecture is privacy-first, uses LangGraph checkpointers for persistent conversation state, and is designed for university mental health environments.

Q: What is LangGraph?
A: LangGraph is a Python library built on top of LangChain for building stateful, multi-actor LLM applications. It models workflows as graphs — nodes are agents or functions, edges are transitions. The big feature is checkpointers: persistent state that lets agents remember context across turns. I used it in PulseIQ for the 5-agent pipeline and in the AI Therapist for multi-turn conversation memory.

Q: What is LangChain?
A: LangChain is a Python framework for building applications with large language models. It handles prompt management, chains of LLM calls, document loaders, and tool integrations. I used it in ClauseGuard to build the multi-agent contract analysis pipeline — clause extraction, risk assessment, output validation, all chained together.
