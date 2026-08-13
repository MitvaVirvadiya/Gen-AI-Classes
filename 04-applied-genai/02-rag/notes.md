# RAG from first principles

## One-sentence truth

The model does not have your files. RAG retrieves relevant chunks at
query time and puts them in the prompt so next-token prediction has
something true to continue from.

## Do this again

```
index time:  docs → chunk → embed → vector store  (+ keywords)
query time:  question → embed → top-k chunks → prompt → generate
```

We will write this in ~80 lines: numpy or a tiny FAISS, no LangChain.

---

## The actual hard parts

1. **Chunking** — too small: no context. too big: noisy retrieval, token tax
2. **Embedding model** — a *different* model than the LLM. Same space
   for queries and docs
3. **Retrieval quality** — hit-rate@k on a labeled set. Hybrid (BM25 +
   vectors) beats vectors alone more often than Twitter admits
4. **Prompt stuffing** — cite sources, instruct abstention, stay under
   the window
5. **Eval** — "did we retrieve the right chunk?" is a separate metric
   from "was the answer pretty?"

## What RAG is not

- not fine-tuning (you did not change weights)
- not an agent (one retrieve, one generate — unless you loop)
- not free of hallucination (the model can still ignore the chunks)

## When we lab this

A folder of our own lesson notes as the corpus. Query: "what is BPE?"
If we cannot retrieve Lesson 1.1, the pipeline is wrong.
