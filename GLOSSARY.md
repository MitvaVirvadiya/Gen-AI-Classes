# Glossary

One-paragraph truths. Full treatment lives in the linked lesson.

| Term | Meaning | Lesson |
|---|---|---|
| **Token** | The atomic unit an LLM sees. Not always a word. Often a subword or a byte-group. Everything is counted, billed, and attended over in tokens. | [1.1](01-llms-from-scratch/01-tokenization/notes.md) |
| **Tokenizer** | The program that maps `str ↔ list[int]`. Encode goes text → IDs. Decode goes IDs → text. | [1.1](01-llms-from-scratch/01-tokenization/notes.md) |
| **Vocabulary / vocab size** | The finite set of tokens the model knows. 32k–200k is typical. Each ID is an index into this set. | [1.1](01-llms-from-scratch/01-tokenization/notes.md) |
| **BPE** | Byte Pair Encoding. Start from bytes/chars, repeatedly merge the most common adjacent pair. Used by GPT-family models. | [1.1](01-llms-from-scratch/01-tokenization/notes.md) |
| **WordPiece** | BERT-style. Like BPE but merges by likelihood, not raw frequency. | [1.1](01-llms-from-scratch/01-tokenization/notes.md) |
| **SentencePiece / Unigram** | Language-agnostic tokenizer that treats text as raw unicode/bytes. Common for Llama, T5, Gemma. | [1.1](01-llms-from-scratch/01-tokenization/notes.md) |
| **Special tokens** | Reserved IDs: pad, unk, bos/eos, and chat markers like `<\|user\|>`. They are not "words." | [1.1](01-llms-from-scratch/01-tokenization/notes.md) |
| **OOV** | Out of vocabulary. A word-level tokenizer's fatal flaw. Subword tokenizers almost never truly OOV because they can fall back to bytes. | [1.1](01-llms-from-scratch/01-tokenization/notes.md) |
| **tiktoken** | OpenAI's BPE library. What GPT-4-class APIs use to count tokens. | [1.1](01-llms-from-scratch/01-tokenization/notes.md) |
| **spaCy tokenizer** | Linguistic word splitter. Useful for NLP features. Not what LLMs use. | [1.1](01-llms-from-scratch/01-tokenization/notes.md) |
| **Embedding** | A learned vector for a token (or a piece of text). The model's first layer is a lookup table of these. | [1.2](01-llms-from-scratch/02-embeddings/notes.md) |
| **Embedding matrix** | Shape `(vocab_size, d_model)`. Row `i` is the vector for token ID `i`. | [1.2](01-llms-from-scratch/02-embeddings/notes.md) |
| **d_model** | Width of the residual stream. 768, 2048, 4096 are common. Every block talks in this size. | [1.2](01-llms-from-scratch/02-embeddings/notes.md) |
| **Cosine similarity** | How aligned two vectors are. Used to ask "which tokens/docs are nearby?" | [1.2](01-llms-from-scratch/02-embeddings/notes.md) |
| **Contextual embedding** | A vector that depends on neighbors (what transformers produce). Opposite of static Word2Vec. | [1.2](01-llms-from-scratch/02-embeddings/notes.md) |
| **Next-token prediction** | The pretraining job: given tokens `1..t`, predict token `t+1`. | [1.3](01-llms-from-scratch/03-language-modeling/notes.md) |
| **Context window** | Maximum tokens the model can see at once. 4k, 8k, 128k, 1M, ... | [1.3](01-llms-from-scratch/03-language-modeling/notes.md) |
| **Perplexity** | `exp(average negative log-likelihood)`. Lower = the model is less surprised by the text. | [1.3](01-llms-from-scratch/03-language-modeling/notes.md) |
| **Cross-entropy loss** | The training loss for classification over the vocab. Same math as NLL of the next token. | [1.3](01-llms-from-scratch/03-language-modeling/notes.md) |
| **Positional encoding** | Extra signal so the model knows token order. Sinusoidal, learned, RoPE, ALiBi. | [1.4](01-llms-from-scratch/04-positional-encoding/notes.md) |
| **RoPE** | Rotary Position Embedding. Rotates Q/K by angle proportional to position. Llama, many modern models. | [1.4](01-llms-from-scratch/04-positional-encoding/notes.md) |
| **Attention** | "For this query, mix values with weights from softmax(query · keys / √d)." | [1.5](01-llms-from-scratch/05-attention/notes.md) |
| **Q, K, V** | Query, Key, Value. Query asks, keys are looked up, values are what you actually mix. | [1.5](01-llms-from-scratch/05-attention/notes.md) |
| **Self-attention** | Q, K, V all come from the same sequence. | [1.6](01-llms-from-scratch/06-self-attention/notes.md) |
| **Causal / masked attention** | Token `t` may not look at `t+1, t+2, ...`. Required for next-token LMs. | [1.6](01-llms-from-scratch/06-self-attention/notes.md) |
| **Multi-head attention** | Several attention heads in parallel, each with its own QKV projections, then concatenated. | [1.6](01-llms-from-scratch/06-self-attention/notes.md) |
| **Transformer block** | Pre-norm (or post-norm) + attention + residual + FFN + residual. Stack N of them. | [1.7](01-llms-from-scratch/07-transformer/notes.md) |
| **FFN / MLP** | Two (or three, if SwiGLU) linear layers that process each token independently. | [1.7](01-llms-from-scratch/07-transformer/notes.md) |
| **Residual connection** | `x + sublayer(x)`. The highway that lets gradients and information travel deep. | [1.7](01-llms-from-scratch/07-transformer/notes.md) |
| **LayerNorm / RMSNorm** | Stabilizes activations. RMSNorm is the modern Llama-style default. | [1.7](01-llms-from-scratch/07-transformer/notes.md) |
| **Decoder-only** | GPT/Llama style. Each token predicts the next. This is "an LLM" in 2024–2026. | [1.7](01-llms-from-scratch/07-transformer/notes.md) |
| **Encoder-only** | BERT style. Bidirectional. Good for embeddings/classification, not open-ended generation. | [1.7](01-llms-from-scratch/07-transformer/notes.md) |
| **Parameter** | A learned number. Weights and biases. "7B" ≈ 7 billion of them. | [1.8](01-llms-from-scratch/08-parameters-and-weights/notes.md) |
| **Weight** | The matrix (or vector) a layer multiplies by. Stored in `.safetensors` / `.gguf`. | [1.8](01-llms-from-scratch/08-parameters-and-weights/notes.md) |
| **Backpropagation** | Chain rule through the graph so each weight knows how to reduce loss. | [1.9](01-llms-from-scratch/09-training/notes.md) |
| **Pretraining** | Next-token training on a huge corpus. Produces a base model. | [1.9](01-llms-from-scratch/09-training/notes.md) |
| **Temperature** | Divides logits before softmax. High = flatter, more random. 0 ≈ greedy. | [1.10](01-llms-from-scratch/10-sampling/notes.md) |
| **Top-k / top-p** | Only sample from the k best, or from the smallest set whose probs sum to p (nucleus). | [1.10](01-llms-from-scratch/10-sampling/notes.md) |
| **SFT** | Supervised fine-tuning on instruction/response pairs. Turns a base model into a useful assistant-shaped model. | [2.1](02-adapt-and-serve/01-fine-tuning/notes.md) |
| **LoRA** | Train a low-rank pair of matrices instead of the full weight. Cheap fine-tune. | [2.2](02-adapt-and-serve/02-lora-peft/notes.md) |
| **PEFT** | Family name: parameter-efficient fine-tuning. LoRA is the popular member. | [2.2](02-adapt-and-serve/02-lora-peft/notes.md) |
| **QLoRA** | LoRA on a quantized frozen base. Fine-tune 7B–70B on one GPU. | [2.2](02-adapt-and-serve/02-lora-peft/notes.md) |
| **RLHF** | Reinforce a reward model (from human prefs) with PPO-like RL. Classic ChatGPT recipe. | [2.3](02-adapt-and-serve/03-alignment/notes.md) |
| **DPO** | Direct Preference Optimization. Align from chosen/rejected pairs without a separate RM + PPO loop. | [2.3](02-adapt-and-serve/03-alignment/notes.md) |
| **Quantization** | Store weights in fewer bits (8, 4, sometimes 2). Speed + memory, some quality loss. | [2.5](02-adapt-and-serve/05-quantization/notes.md) |
| **GGUF** | llama.cpp's file format for quantized local models. What Ollama uses under the hood. | [2.5](02-adapt-and-serve/05-quantization/notes.md) |
| **Distillation** | Train a small student to match a large teacher. | [2.6](02-adapt-and-serve/06-compression/notes.md) |
| **KV cache** | Saved keys/values from previous tokens so generation is O(new tokens), not O(n²) every step. | [2.7](02-adapt-and-serve/07-inference-optimization/notes.md) |
| **vLLM** | High-throughput OpenAI-compatible server. PagedAttention, continuous batching. | [2.7](02-adapt-and-serve/07-inference-optimization/notes.md) |
| **Hugging Face Hub** | Git-like host for models, tokenizers, datasets. | [3.1](03-huggingface-and-open-models/01-hub-and-model-cards/notes.md) |
| **transformers** | The Python library that loads those models. | [3.2](03-huggingface-and-open-models/02-transformers-generate/notes.md) |
| **Pipeline** | One-liner HF helper: `pipeline("text-generation", model=...)`. | [3.2](03-huggingface-and-open-models/02-transformers-generate/notes.md) |
| **Prompting** | The input you construct. System + user + tools + RAG context. | [4.1](04-applied-genai/01-prompting/notes.md) |
| **RAG** | Retrieve relevant chunks, stuff them into the prompt, then generate. | [4.2](04-applied-genai/02-rag/notes.md) |
| **Chunking** | Splitting documents so retrieval can return the right piece. | [4.2](04-applied-genai/02-rag/notes.md) |
| **LangChain** | Framework of chains, tools, memory, integrations. Easy to start, easy to overuse. | [4.3](04-applied-genai/03-langchain/notes.md) |
| **LangGraph** | Graph/state-machine layer for agents with cycles, persistence, human-in-the-loop. | [4.4](04-applied-genai/04-langgraph/notes.md) |
| **LlamaIndex** | Data-first framework. Ingestion, indexes, query engines. Strong for RAG. | [4.5](04-applied-genai/05-llamaindex/notes.md) |
| **Agent** | An LLM in a loop with tools, state, and a stop condition. Not a chatbot with extra prompt text. | [5.1](05-agents-and-mcp/01-what-is-an-agent/notes.md) |
| **Tool / function calling** | Model emits a structured "call this function with these args"; you run it and feed the result back. | [5.2](05-agents-and-mcp/02-tool-calling/notes.md) |
| **MCP** | Model Context Protocol. Standard way to expose tools/resources/prompts to any MCP-capable client. | [5.5](05-agents-and-mcp/05-mcp/notes.md) |
