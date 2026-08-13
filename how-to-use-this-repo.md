# How to use this repo

This is not a bookmarks folder. It is a course you can re-take.

## The contract

I write:

- the lecture (`notes.md`)
- the lab (`code/`)
- the homework (`assignment.md`)
- the map (`CURRICULUM.md`, `SEARCH-INDEX.md`, `GLOSSARY.md`)

You write:

- answers in `assignment.md` under `## My answers` (or a sibling `answers.md`)
- ticks in `PROGRESS.md`
- questions at the bottom of a lesson if something did not land

If it is not in a file, we will forget it.

## How to study one lesson

1. Read the lesson `README.md` (10 min). Note the "you will be able to" list.
2. Read `notes.md` once without coding.
3. Run the scripts in order. Change an input. Break something on purpose.
4. Re-read the parts of `notes.md` that the code made real.
5. Do the assignment without looking at the notes first. Then check.
6. Tick `PROGRESS.md`.

## How to come back later

Search in this order:

1. `GLOSSARY.md` — one-paragraph definition
2. `SEARCH-INDEX.md` — which file owns that word
3. The lesson `notes.md` — full explanation + "how to do it again"
4. The lesson `code/` — the smallest working example

Every lesson's `notes.md` starts with a **one-sentence truth** and a
**do-this-again** box. Those two are the retrieval interface.

## File conventions

| File | Job |
|---|---|
| `README.md` (repo) | Front door |
| `START-HERE.md` | What to do today |
| `CURRICULUM.md` | Full path + critique of the ChatGPT roadmap |
| `GLOSSARY.md` | Term → short definition + link |
| `SEARCH-INDEX.md` | Keyword → file |
| `PROGRESS.md` | Checklist |
| `track/README.md` | Why this track exists |
| `lesson/README.md` | Goals, time, file list |
| `lesson/notes.md` | The class |
| `lesson/assignment.md` | Practice |
| `lesson/code/` | Runnable, numbered `01_`, `02_`, ... |
| `lesson/data/` | Tiny files we actually train/run on |

## What "done" means

You are done with a lesson when you can, from memory, on a blank file:

- define the idea in one sentence
- say what problem it solves
- write or reconstruct the core 20–40 lines of code
- name one way it fails in production

If you can only recognize the words, you are not done.

## What we will not do

- Skip to LangChain before you can write attention
- Treat Hugging Face as the model (it is a library around models)
- Collect 40 notebooks and never re-run them
- Use a 7B download when a 50-line numpy script teaches the same idea

## Stack we will actually touch (later)

Not all at once. Only when the track needs them.

- **From scratch:** Python, numpy, then a tiny torch model
- **Open models:** Hugging Face `transformers`, `tokenizers`, `datasets`, `peft`, `trl`
- **Local run:** Ollama or `llama.cpp` / GGUF when we deploy
- **Serving:** vLLM conceptually, then a small API
- **Applied:** LangChain / LangGraph, LlamaIndex, raw OpenAI-compatible APIs
- **Agents:** tool calling, then MCP

Karpathy's *Neural Networks: Zero to Hero*, `minbpe`, and `nanoGPT` are
the spiritual references for Track 1. We re-implement the ideas here so
the notes are yours.
