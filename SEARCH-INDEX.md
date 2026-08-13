# Search index

Find a word, open the file. Prefer `notes.md` for the explanation and
`code/` for the working example.

## Track 1 — from scratch

| You searched for | Open |
|---|---|
| token, tokenize, BPE, vocab, tiktoken, spaCy, special token, OOV, SentencePiece, WordPiece, encode, decode | [01-tokenization/notes.md](01-llms-from-scratch/01-tokenization/notes.md) |
| embedding, vector, cosine, Word2Vec, lookup table, d_model | [02-embeddings/notes.md](01-llms-from-scratch/02-embeddings/notes.md) |
| next token, language model, loss, perplexity, context window, causal LM | [03-language-modeling/notes.md](01-llms-from-scratch/03-language-modeling/notes.md) |
| position, RoPE, sinusoidal, ALiBi, order | [04-positional-encoding/notes.md](01-llms-from-scratch/04-positional-encoding/notes.md) |
| attention, QKV, softmax, scaled dot product | [05-attention/notes.md](01-llms-from-scratch/05-attention/notes.md) |
| self-attention, multi-head, causal mask, padding mask | [06-self-attention/notes.md](01-llms-from-scratch/06-self-attention/notes.md) |
| transformer, GPT, decoder, FFN, residual, LayerNorm, RMSNorm, SwiGLU | [07-transformer/notes.md](01-llms-from-scratch/07-transformer/notes.md) |
| parameters, 7B, weights, safetensors, memory, VRAM | [08-parameters-and-weights/notes.md](01-llms-from-scratch/08-parameters-and-weights/notes.md) |
| training, backprop, optimizer, AdamW, gradient, pretrain, batch | [09-training/notes.md](01-llms-from-scratch/09-training/notes.md) |
| sampling, temperature, top-k, top-p, greedy, generate | [10-sampling/notes.md](01-llms-from-scratch/10-sampling/notes.md) |

## Track 2 — adapt and serve

| You searched for | Open |
|---|---|
| fine-tune, SFT, instruction tune, catastrophic forgetting | [01-fine-tuning/notes.md](02-adapt-and-serve/01-fine-tuning/notes.md) |
| LoRA, PEFT, QLoRA, adapter, rank | [02-lora-peft/notes.md](02-adapt-and-serve/02-lora-peft/notes.md) |
| RLHF, DPO, alignment, reward model, preference | [03-alignment/notes.md](02-adapt-and-serve/03-alignment/notes.md) |
| eval, benchmark, MMLU, hallucination, LLM-as-judge | [04-evaluation/notes.md](02-adapt-and-serve/04-evaluation/notes.md) |
| quantize, int8, int4, GGUF, GPTQ, AWQ, bitsandbytes | [05-quantization/notes.md](02-adapt-and-serve/05-quantization/notes.md) |
| distill, prune, compress, student, teacher | [06-compression/notes.md](02-adapt-and-serve/06-compression/notes.md) |
| KV cache, vLLM, speculative decoding, batching, paged attention | [07-inference-optimization/notes.md](02-adapt-and-serve/07-inference-optimization/notes.md) |
| deploy, Ollama, llama.cpp, API, Docker, production | [08-deployment/notes.md](02-adapt-and-serve/08-deployment/notes.md) |

## Track 3 — Hugging Face

| You searched for | Open |
|---|---|
| Hub, model card, license, gated model | [01-hub-and-model-cards/notes.md](03-huggingface-and-open-models/01-hub-and-model-cards/notes.md) |
| AutoModel, generate, pipeline, device_map | [02-transformers-generate/notes.md](03-huggingface-and-open-models/02-transformers-generate/notes.md) |
| datasets, map, collator, padding | [03-tokenizers-and-datasets/notes.md](03-huggingface-and-open-models/03-tokenizers-and-datasets/notes.md) |
| TRL, SFTTrainer, peft library | [04-finetune-peft-trl/notes.md](03-huggingface-and-open-models/04-finetune-peft-trl/notes.md) |

## Track 4 — applied

| You searched for | Open |
|---|---|
| prompt, system prompt, few-shot, CoT, chat template | [01-prompting/notes.md](04-applied-genai/01-prompting/notes.md) |
| RAG, retrieve, chunk, vector DB, hybrid search | [02-rag/notes.md](04-applied-genai/02-rag/notes.md) |
| LangChain, LCEL, chain | [03-langchain/notes.md](04-applied-genai/03-langchain/notes.md) |
| LangGraph, state machine, checkpoint | [04-langgraph/notes.md](04-applied-genai/04-langgraph/notes.md) |
| LlamaIndex, index, query engine, node | [05-llamaindex/notes.md](04-applied-genai/05-llamaindex/notes.md) |
| which framework, when to use raw API | [06-when-to-use-which/notes.md](04-applied-genai/06-when-to-use-which/notes.md) |

## Track 5 — agents

| You searched for | Open |
|---|---|
| agent, ReAct, loop | [01-what-is-an-agent/notes.md](05-agents-and-mcp/01-what-is-an-agent/notes.md) |
| tool, function calling, JSON schema | [02-tool-calling/notes.md](05-agents-and-mcp/02-tool-calling/notes.md) |
| memory, planning, scratchpad | [03-memory-and-planning/notes.md](05-agents-and-mcp/03-memory-and-planning/notes.md) |
| multi-agent, supervisor, swarm | [04-multi-agent/notes.md](05-agents-and-mcp/04-multi-agent/notes.md) |
| MCP, Model Context Protocol, server, resource | [05-mcp/notes.md](05-agents-and-mcp/05-mcp/notes.md) |
| capstone, final project | [06-capstone/notes.md](05-agents-and-mcp/06-capstone/notes.md) |

## Track 0 — foundations

| You searched for | Open |
|---|---|
| vector, matrix, dot product, softmax, gradient | [01-math-you-need/notes.md](00-foundations/01-math-you-need/notes.md) |
| MLP, activation, ReLU, linear layer, loss | [02-neural-nets/notes.md](00-foundations/02-neural-nets/notes.md) |
