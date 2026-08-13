# Curriculum

This is the full path: **LLMs from scratch → adapt and serve → Hugging Face
→ applied GenAI → agents and MCP**.

We start at Track 1. Later tracks already have gist notes so you can search
them, but we do not study them until the earlier track is done.

---

## Verdict on the ChatGPT 14-step roadmap

The list you brought:

```
Tokenization → Embeddings → Positional Encoding → Attention →
Self-Attention → Transformer → Parameters & Weights →
Training / Backprop → Fine-tuning → LoRA / PEFT →
Quantization → Compression → Inference Optimization → Deployment
```

### What it gets right

- The first half is the correct spine of "how a transformer reads text."
- It separates *building* a model from *adapting* and *serving* one.
- LoRA after full fine-tuning is the right order (special case after general case).
- Deployment at the end is correct. Do not start there.

### What is wrong or incomplete

| Issue | Why it matters |
|---|---|
| **No language-modeling objective** | Tokens and attention are pointless until you know the model is trained to predict the *next token*. That is the job. |
| **Attention and Self-Attention as two big steps** | Self-attention *is* attention where Q, K, V all come from the same sequence. Teach the math once, then the special case, then multi-head. |
| **Parameters & Weights as its own chapter** | That is just "what a neural net stores." It belongs in foundations + inside the transformer block, not as a separate mystery. |
| **Training is one box** | Pretraining, supervised fine-tuning, and preference training (RLHF / DPO) are three different jobs. One word ("training") hides that. |
| **No sampling** | Temperature, top-k, top-p is how you *use* a trained LM. Without it you do not understand why outputs change. |
| **No architecture fork** | Encoder-only (BERT), encoder-decoder (T5), decoder-only (GPT/Llama) are not the same. Almost all "LLMs" you will use are decoder-only. |
| **Quantization vs compression overlap** | Quantization *is* a compression method. Distillation and pruning are the other family. Split them cleanly. |
| **No evaluation** | You cannot fine-tune or deploy honestly without eval. |
| **No applied stack** | Hugging Face, RAG, LangChain, LlamaIndex, agents, MCP are how you ship. The 14 steps stop at "model exists." |
| **spaCy as the tokenization start** | Your ChatGPT thread taught linguistic tokenization. LLMs use subword BPE / SentencePiece. We fix that in Lesson 1. |

### The corrected order

```
[optional] math + neural nets
        ↓
tokenization → embeddings → next-token objective
        ↓
positional encoding → attention / self-attention / multi-head
        ↓
transformer block → decoder-only GPT-style model
        ↓
training loop (loss, backprop, data) → sampling
        ↓
fine-tune → LoRA/PEFT → alignment (idea-level)
        ↓
eval → quantize → other compression → inference tricks → deploy
        ↓
Hugging Face as the standard library
        ↓
prompting → RAG → LC / LangGraph / LlamaIndex
        ↓
tool-calling agents → MCP → a real agent you keep
```

---

## Track 0 — Foundations (only if rusty)

Skip if you can already answer: what is a dot product, what is softmax,
what is cross-entropy, what does an MLP layer do.

| # | Lesson | Folder |
|---|---|---|
| 0.1 | Math you actually need | [00-foundations/01-math-you-need](00-foundations/01-math-you-need/notes.md) |
| 0.2 | Neural nets in one sitting | [00-foundations/02-neural-nets](00-foundations/02-neural-nets/notes.md) |

## Track 1 — LLMs from scratch  ← current

Goal: you can explain and code the path from raw text to a tiny
decoder-only transformer that generates tokens.

| # | Lesson | Why it is here |
|---|---|---|
| 1.1 | [Tokenization](01-llms-from-scratch/01-tokenization/README.md) | Text must become IDs. This is where cost, bugs, and multilingual pain start. |
| 1.2 | [Embeddings](01-llms-from-scratch/02-embeddings/README.md) | IDs are not meaning. A table of vectors is. |
| 1.3 | [Language modeling objective](01-llms-from-scratch/03-language-modeling/README.md) | The job is next-token prediction. Everything else serves this. |
| 1.4 | [Positional encoding](01-llms-from-scratch/04-positional-encoding/README.md) | Attention has no sense of order without this. |
| 1.5 | [Attention](01-llms-from-scratch/05-attention/README.md) | Weighted sum of values, weights from query·key. |
| 1.6 | [Self-attention and multi-head](01-llms-from-scratch/06-self-attention/README.md) | Same sequence attends to itself. Several heads in parallel. |
| 1.7 | [Transformer architecture](01-llms-from-scratch/07-transformer/README.md) | Block = norm + attention + residual + FFN. Stack them. |
| 1.8 | [Parameters and weights](01-llms-from-scratch/08-parameters-and-weights/README.md) | What 7B actually means. Where the bytes go. |
| 1.9 | [Training and backprop](01-llms-from-scratch/09-training/README.md) | Loss, gradients, a real loop on a tiny corpus. |
| 1.10 | [Sampling and generation](01-llms-from-scratch/10-sampling/README.md) | How a probability vector becomes text. |

## Track 2 — Adapt, compress, serve

Goal: take a model you did not pretrain and make it useful, small, fast.

| # | Lesson | Why it is here |
|---|---|---|
| 2.1 | [Fine-tuning](02-adapt-and-serve/01-fine-tuning/notes.md) | SFT: teach style and tasks with full (or almost full) weights. |
| 2.2 | [LoRA / PEFT](02-adapt-and-serve/02-lora-peft/notes.md) | Adapt a giant model by training tiny adapters. |
| 2.3 | [Alignment, briefly](02-adapt-and-serve/03-alignment/notes.md) | RLHF / DPO — why ChatGPT is not just a pretrained LM. |
| 2.4 | [Evaluation](02-adapt-and-serve/04-evaluation/notes.md) | How you know it got better, not just different. |
| 2.5 | [Quantization](02-adapt-and-serve/05-quantization/notes.md) | Fewer bits per weight. GGUF, int8, int4. |
| 2.6 | [Compression](02-adapt-and-serve/06-compression/notes.md) | Distillation, pruning — the other way to get smaller. |
| 2.7 | [Inference optimization](02-adapt-and-serve/07-inference-optimization/notes.md) | KV cache, batching, speculative decoding, vLLM ideas. |
| 2.8 | [Deployment](02-adapt-and-serve/08-deployment/notes.md) | Ollama, llama.cpp, a small API, what "production" means. |

## Track 3 — Hugging Face and open models

Goal: the ecosystem is no longer magic. You can load, tokenize, generate,
and fine-tune with the standard library of open LLMs.

| # | Lesson |
|---|---|
| 3.1 | [The Hub and model cards](03-huggingface-and-open-models/01-hub-and-model-cards/notes.md) |
| 3.2 | [transformers: load and generate](03-huggingface-and-open-models/02-transformers-generate/notes.md) |
| 3.3 | [tokenizers + datasets](03-huggingface-and-open-models/03-tokenizers-and-datasets/notes.md) |
| 3.4 | [Fine-tune with PEFT / TRL](03-huggingface-and-open-models/04-finetune-peft-trl/notes.md) |

## Track 4 — Applied GenAI

Goal: products, not papers. Prompting, retrieval, and the two libraries
everyone asks about.

| # | Lesson |
|---|---|
| 4.1 | [Prompting that is not folklore](04-applied-genai/01-prompting/notes.md) |
| 4.2 | [RAG from first principles](04-applied-genai/02-rag/notes.md) |
| 4.3 | [LangChain](04-applied-genai/03-langchain/notes.md) |
| 4.4 | [LangGraph](04-applied-genai/04-langgraph/notes.md) |
| 4.5 | [LlamaIndex](04-applied-genai/05-llamaindex/notes.md) |
| 4.6 | [When to use which](04-applied-genai/06-when-to-use-which/notes.md) |

## Track 5 — Agents and MCP

Goal: a model that *does things*, with tools that are not hardcoded to one app.

| # | Lesson |
|---|---|
| 5.1 | [What an agent actually is](05-agents-and-mcp/01-what-is-an-agent/notes.md) |
| 5.2 | [Tool calling / function calling](05-agents-and-mcp/02-tool-calling/notes.md) |
| 5.3 | [Memory, planning, loops](05-agents-and-mcp/03-memory-and-planning/notes.md) |
| 5.4 | [Multi-agent patterns](05-agents-and-mcp/04-multi-agent/notes.md) |
| 5.5 | [MCP](05-agents-and-mcp/05-mcp/notes.md) |
| 5.6 | [Build one agent you keep](05-agents-and-mcp/06-capstone/notes.md) |

---

## How we will work through this

1. I teach one lesson at a time (notes + code + assignment).
2. You run the code and do the assignment.
3. You come back with answers / questions.
4. We mark `PROGRESS.md` and open the next lesson.
5. When a later lesson needs a new library, we add it to `requirements.txt`
   and document the install in that lesson — not before.

**This week: Lesson 1.1 Tokenization only.**
