# LLM deployment

## One-sentence truth

Deployment is: a process that loads **exactly one** (model, tokenizer,
chat template, sampler defaults) and serves `prompt → tokens` over an
API you can monitor.

## Do this again (the path we will actually take)

1. Run locally with **Ollama** or `llama.cpp` and confirm quality
2. Wrap with the OpenAI-compatible HTTP API (Ollama and vLLM both speak it)
3. Put config in env vars: model name, max tokens, timeouts
4. Log prompt length, output length, latency, errors (never log secrets)
5. Only then Docker / a GPU box / a provider

```
client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
client.chat.completions.create(model="qwen2.5:7b", messages=[...])
```

Same client code later points at Groq, vLLM, or a cloud.

---

## Choices

| Need | Tool |
|---|---|
| Laptop, hobby, demos | Ollama, LM Studio |
| Serious local / prod GPU | vLLM |
| Edge / CPU / Apple | llama.cpp, MLX |
| Don't want to host | hosted API (pay per token) |

## Production checklist (short)

- pin model hash / tag, not `:latest`
- health endpoint
- timeouts and max context
- separate "eval" traffic from "users"
- a rollback (previous GGUF / previous container)

## What we will not do first

Kubernetes-on-day-one, multi-region, custom CUDA. A working local
server + one eval set beats a beautiful empty cluster.
