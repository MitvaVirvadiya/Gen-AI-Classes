# Lesson 1.2 — Embeddings

**Track:** 1 — LLMs from scratch
**Status:** class ready
**Time:** 75 minutes + assignment
**Prerequisites:** [1.1 Tokenization](../01-tokenization/README.md)

## What you will be able to do

- Say what an embedding is without saying "meaning in vector space" as a vibe
- Implement a lookup table: token id → vector
- Measure similarity with cosine
- Explain why the first layer of an LLM is just `E[token_ids]`
- Distinguish static embeddings from the contextual ones transformers produce

## Files

| File | Role |
|---|---|
| [notes.md](notes.md) | Lecture |
| [assignment.md](assignment.md) | Homework |
| [code/01_lookup_table.py](code/01_lookup_table.py) | Embedding matrix from scratch |
| [code/02_cosine_neighbors.py](code/02_cosine_neighbors.py) | Similarity as nearest neighbors |
| [data/toy_vectors.json](data/toy_vectors.json) | Hand-built 2-D vectors so you can see the geometry |

## Next

[Lesson 1.3 — Language modeling objective](../03-language-modeling/README.md)
