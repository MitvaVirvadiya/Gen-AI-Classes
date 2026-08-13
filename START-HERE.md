# Start here

You asked for a documented tuition path: LLMs from scratch → using models
→ agents and MCP. We are **not** starting with Hugging Face, agents, or
deployment. Those are later tracks. If you skip the first track you will
be calling APIs you cannot debug.

## What you do this week

1. Read [CURRICULUM.md](CURRICULUM.md) once. Do not study it. Just see the map.
2. Skim [how-to-use-this-repo.md](how-to-use-this-repo.md) so you know how
   these notes are meant to be used.
3. Open **Lesson 1 — Tokenization** and treat it like a class:
   - [01-llms-from-scratch/01-tokenization/README.md](01-llms-from-scratch/01-tokenization/README.md)
   - Read `notes.md` with a notebook open
   - Run every script in `code/`
   - Do `assignment.md` before asking for Lesson 2 review
4. Only then open Lesson 2 — Embeddings.

## The one correction to your existing code

You already have `tokenization/text-tokens.py`. It uses **spaCy**.

spaCy is a linguistic tokenizer (words, punctuation, POS-style features).
GPT, Llama, Gemma, and almost every modern LLM use **subword tokenizers**
(BPE / SentencePiece). Same English word, different IDs, different costs,
different bugs.

We keep your spaCy file as a contrast demo. Lesson 1 explains why it is
the wrong tool for LLM work, then builds the right one from scratch.

## Pace

- One lesson = one sitting if the notes say 60–90 minutes
- Do not binge five theory files in a day
- Code + assignment is the class. Reading alone is not

## After Track 1

Then we do Track 2 (fine-tune / LoRA / quantize / deploy), then Hugging
Face as a *library* (not as magic), then RAG, then agents and MCP.

If you ever come back cold: search [SEARCH-INDEX.md](SEARCH-INDEX.md) or
[GLOSSARY.md](GLOSSARY.md), then jump to that lesson's `notes.md`.
