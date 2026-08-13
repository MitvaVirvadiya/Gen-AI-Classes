# Time, outcomes, what comes after

**Assumption:** 11 focused hours / week. Notes + code + assignment,
not just reading. Miss a week → add a week. Heavy lessons sometimes
spill.

This is not “you become an AI researcher.” It is “you can build and
debug real LLM systems without cargo-culting Hugging Face.”

---

## The honest total

| Path                                        | Hours    | At 11 h/week                       |
| ------------------------------------------- | -------- | ---------------------------------- |
| Track 1 only (understand + tiny model)      | 35–45   | **3.5–4.5 weeks**           |
| Tracks 1–3 (understand + adapt + HF)       | 75–95   | **7–9 weeks**               |
| Full course through agents + MCP + capstone | 120–150 | **11–14 weeks** (~3 months) |

Use **13 weeks / ~3 months** as the planning number if you stay
consistent. 16 weeks if life happens or you redo a lab.

Track 0 is +1 week only if math/NNs are shaky.

---

## Week-by-week (11 hours)

### Weeks 1–4 — Track 1: LLMs from scratch

| Week | Lessons                                                | Hours (typical) |
| ---- | ------------------------------------------------------ | --------------- |
| 1    | 1.1 Tokenization + 1.2 Embeddings                      | 10–12          |
| 2    | 1.3 LM objective + 1.4 Positions + 1.5 Attention (lab) | 11              |
| 3    | 1.6 Self-attn + 1.7 Transformer block (lab)            | 11              |
| 4    | 1.8 Params + 1.9 Train a toy GPT + 1.10 Sampling       | 11–13          |

**Ready means after week 4 you can:**

- Explain a decoder-only LLM on a whiteboard (tokens → sample)
- Train a tiny transformer on a text file and generate from it
- Debug “this output is weird” as tokenizer / mask / sampler / weights
- Read a Hugging Face `forward()` and know what each tensor is

You cannot yet ship a product. You *can* stop being bluffed by jargon.

### Weeks 5–8 — Tracks 2–3: adapt and the standard library

| Week | Focus                                                             |
| ---- | ----------------------------------------------------------------- |
| 5    | SFT idea + eval + first HF generate (small instruct model)        |
| 6    | LoRA / QLoRA lab on a tiny instruction set                        |
| 7    | Quantize (GGUF / 4-bit), run locally (Ollama or llama.cpp)        |
| 8    | Inference mental model (KV cache) + a small OpenAI-compatible API |

**Ready means after week 8 you can:**

- Load any open instruct model with the correct tokenizer + chat template
- Fine-tune with LoRA, save a 20–50 MB adapter, eval before/after
- Fit a 7B-class model on a laptop via quantization (quality-aware)
- Serve it locally and call it with the same client as a hosted API
- Know when *not* to fine-tune (RAG / prompt / better data first)

### Weeks 9–13 — Tracks 4–5: products, agents, MCP

| Week | Focus                                                            |
| ---- | ---------------------------------------------------------------- |
| 9    | Prompting + RAG from scratch on*this repo’s notes*            |
| 10   | Same RAG in LlamaIndex; LangChain only where it earns its keep   |
| 11   | LangGraph + tool calling (one agent, two tools, step limit)      |
| 12   | MCP server over this course + connect a host                     |
| 13   | Capstone: study agent + 15-question eval + README for future you |

**Ready means after week 13 you can:**

- Build RAG on your own documents without a framework, then with one
- Choose LangChain vs LangGraph vs LlamaIndex vs raw API on purpose
- Ship a tool-using agent that does not loop forever
- Expose tools over MCP
- Measure whether a change helped (a private eval set, not vibes)

That is **builder-ready**, not **research-ready**.

---

## What “ready” is not

After this course you will **not** automatically be able to:

- Pretrain a 7B from scratch (data + cluster + months)
- Beat frontier labs on a benchmark
- Design new architectures
- Guarantee zero hallucinations
- Skip eval because “it looked good in the notebook”

You **will** be the person who can take a real problem (internal docs,
a support bot, a coding helper, a study agent) and choose the cheapest
correct tool: prompt, RAG, LoRA, or agent — and debug it when it lies.

---

## Pace rules so 11 hours actually compound

- One sitting = one lesson’s notes + its lab, or the assignment. Not five READMEs.
- If a lab breaks, the debug *is* the class. Do not skip to the next file.
- A week with only reading and no code does not count as a week.
- Redo Track 1 week 4 (tiny train + sample) from memory once. That is the exam for “I understand LLMs.”

---

## Next steps after the 13 weeks

In order. Do not do 4 before 1.

1. **Ship one ugly product on your data**Not a tutorial dataset. Your notes, your repo, your job files.RAG + eval + a simple UI or CLI. Keep it running for a month.
2. **Specialize (pick one, 4–8 more weeks)**

   - **Product / applied:** eval harnesses, prompt/versioning, tracing (LangSmith or raw logs), production RAG
   - **Adaptation:** more LoRA, DPO on your preference data, data quality
   - **Systems:** vLLM, batching, KV quantization, cost/latency
   - **Agents:** durable LangGraph, permissions, MCP in a real host
   - **Multimodal / other:** only after text is boring
3. **Read papers with a purpose**Attention Is All You Need, GPT-2/3, LoRA, QLoRA, DPO, RAG surveys.You will understand them *because* of Track 1. Do not start there.
4. **Optional: contribute or work**
   Fine-tune + eval writeup, an MCP server people use, a public notebook
   that is not a clone of someone else’s. Portfolio = artifacts from this
   repo + the one product in step 1.

---

## If you only have one month (44 hours)

Do Track 1 fully (weeks 1–4). Stop. You will understand LLMs.
Tracks 2–5 without Track 1 is how people get stuck in framework soup.

## If you only have two months (88 hours)

Track 1 + Track 2–3 (through a LoRA + a local server).
Build one RAG on the side in week 8 if energy remains. Agents wait.
