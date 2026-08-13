# Track 1 — LLMs from scratch

This is the track we study first.

By the end you can take a string, turn it into token IDs, embed them,
run causal self-attention, stack transformer blocks, train a toy model
on a tiny corpus, and sample text. You will not train Llama. You will
understand why Llama works.

## Lessons

| # | Lesson | Status | Time |
|---|---|---|---|
| 1.1 | [Tokenization](01-tokenization/README.md) | **Class ready** | 90 min + assignment |
| 1.2 | [Embeddings](02-embeddings/README.md) | **Class ready** | 75 min + assignment |
| 1.3 | [Language modeling objective](03-language-modeling/README.md) | Notes ready | 45 min |
| 1.4 | [Positional encoding](04-positional-encoding/README.md) | Notes ready | 45 min |
| 1.5 | [Attention](05-attention/README.md) | Notes ready | 60 min |
| 1.6 | [Self-attention and multi-head](06-self-attention/README.md) | Notes ready | 60 min |
| 1.7 | [Transformer architecture](07-transformer/README.md) | Notes ready | 60 min |
| 1.8 | [Parameters and weights](08-parameters-and-weights/README.md) | Notes ready | 40 min |
| 1.9 | [Training and backprop](09-training/README.md) | Notes ready | 60 min |
| 1.10 | [Sampling and generation](10-sampling/README.md) | Notes ready | 45 min |

**Class ready** means notes + runnable code + assignment.
**Notes ready** means you can study the idea now; the lab lands when we
reach that lesson together.

## Order is not optional

Do not open attention before embeddings. Do not open training before
you can write the loss in one line. Each lesson assumes the previous
one is in your hands, not just your bookmarks.

## What you already had

`tokenization/text-tokens.py` (repo root) is a spaCy demo. Lesson 1.1
explains why that is a different job from LLM tokenization and keeps
the file as a contrast.
