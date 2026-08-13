# Inference optimization

## One-sentence truth

Generation is slow because it is sequential. The tricks are: do not
recompute the past (KV cache), pack many users onto the GPU
(batching / paged attention), and sometimes guess extra tokens
(speculative decoding).

## Do this again

**Prefill:** one parallel forward over the prompt → fill KV cache.
**Decode:** for each new token, attend using cached K/V + this token.

Without a cache, step t would cost O(t²) from scratch. With a cache,
step t costs O(t) to *write* the new row and score it.

---

## The menu

| Trick | What it buys |
|---|---|
| KV cache | decode is usable at all |
| FlashAttention | faster, less memory for the T×T scores |
| Continuous batching | vLLM: new requests join in-flight ones |
| PagedAttention | KV in non-contiguous pages, less waste |
| GQA/MQA | smaller KV cache (Lesson 1.6) |
| Quantized KV | cache in 8/4-bit, longer context on same card |
| Speculative decoding | a small model drafts, big model verifies in parallel |
| Prefix / prompt cache | reuse the system prompt's KV across requests |

## What you should do in practice

- Local one-user: Ollama / llama.cpp already do KV cache + good kernels
- Many concurrent users: vLLM (or TGI, TensorRT-LLM)
- Do not hand-roll a CUDA kernel in this course

## ChatGPT list note

This step is "make decode cheap." Deployment (next) is "put that behind
a socket and operate it."
