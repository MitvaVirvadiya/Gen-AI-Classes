# Gen AI Classes

Personal tuition notes: LLMs from scratch → Hugging Face → RAG → agents and MCP.

This repo is your searchable classroom. Every topic we learn lives here as
notes, runnable code, assignments, and a short "how do I do this again?"
section. Come back months later, search the topic, and you should be able
to rebuild the idea without us sitting together.

You are not collecting blog posts. You are building a second brain for:

1. How LLMs actually work (from tokens to a trained transformer)
2. How to adapt and serve them (fine-tune, LoRA, quantize, deploy)
3. How to use them (Hugging Face, prompting, RAG)
4. How to build systems around them (LangChain / LangGraph, LlamaIndex)
5. How agents and MCP work in the real world

## Start here

| If you want...                               | Open this                                         |
| -------------------------------------------- | ------------------------------------------------- |
| What to do today                             | [START-HERE.md](START-HERE.md)                     |
| The full path and why it is ordered this way | [CURRICULUM.md](CURRICULUM.md)                     |
| How these notes are written and how to study | [how-to-use-this-repo.md](how-to-use-this-repo.md) |
| A word you forgot                            | [GLOSSARY.md](GLOSSARY.md)                         |
| Jump to a topic by keyword                   | [SEARCH-INDEX.md](SEARCH-INDEX.md)                 |
| Tick boxes as you finish                     | [PROGRESS.md](PROGRESS.md)                         |

## Tracks

| # | Track                                           | Folder                                                                    | Status                   |
| - | ----------------------------------------------- | ------------------------------------------------------------------------- | ------------------------ |
| 0 | Foundations (math + neural nets, only if rusty) | [00-foundations](00-foundations/README.md)                                 | Ready to read            |
| 1 | LLMs from scratch                               | [01-llms-from-scratch](01-llms-from-scratch/README.md)                     | **You are here**   |
| 2 | Adapt, compress, serve                          | [02-adapt-and-serve](02-adapt-and-serve/README.md)                         | Mapped, notes first pass |
| 3 | Hugging Face and open models                    | [03-huggingface-and-open-models](03-huggingface-and-open-models/README.md) | Mapped, notes first pass |
| 4 | Applied GenAI (prompting, RAG, LC, LlamaIndex)  | [04-applied-genai](04-applied-genai/README.md)                             | Mapped, notes first pass |
| 5 | Agents and MCP                                  | [05-agents-and-mcp](05-agents-and-mcp/README.md)                           | Mapped, notes first pass |

Track 1 is the one we study first. Later tracks already have searchable
gist notes so you can peek ahead, but we do not skip the foundation.

## How a lesson is laid out

```
01-llms-from-scratch/01-tokenization/
  README.md        ← start of the class (goals, time, files)
  notes.md         ← the lecture
  assignment.md    ← you do this, then we review
  code/            ← runnable scripts
  data/            ← tiny corpora we actually use
```

Every lesson answers the same four questions:

- **What is this?** one honest definition
- **Why does it exist?** the problem it solves
- **How do I do it?** code you can run
- **How do I know I got it?** an assignment with a done-when checklist

## Setup

```bash
cd "/Users/mitvavirvadiya/Developer/Code/Gen AI"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Lesson 1 (tokenization from scratch) runs with the standard library alone.
Install the rest when a lesson tells you to.

## Rule for this repo

If we learned it and it is not written here, it did not happen.
When we finish a session, we update the lesson notes, the assignment
answers if needed, and [PROGRESS.md](PROGRESS.md).
