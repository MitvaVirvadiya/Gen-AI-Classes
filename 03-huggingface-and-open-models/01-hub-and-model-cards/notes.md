# The Hub and model cards

## One-sentence truth

The Hub is git for weights. A model repo is `config.json` + tensors +
tokenizer + a model card that you should actually read.

## Do this again

```
https://huggingface.co/{org}/{name}
  config.json          # architecture
  *.safetensors        # weights
  tokenizer.json       # Lesson 1.1, married to the weights
  README.md            # card: license, intended use, evals
```

`from_pretrained("org/name")` clones / caches that repo and builds the
Python objects.

---

## Read before you download

- **License** — Apache-2.0 vs Llama community vs "research only"
- **Gated** — some models require you to accept terms (`huggingface-cli login`)
- **Architecture** — decoder-only? embedding model? reward model?
- **Context length** and **chat template** (`tokenizer.chat_template`)
- **Quantized variants** — `*-AWQ`, `*-GGUF` are different files

## Local cache

Default: `~/.cache/huggingface/`. It will grow. Know how to delete it.

## When we lab this

We will pick a *small* causal model (e.g. Qwen2.5-0.5B or SmolLM) so
downloads are minutes, not evenings.
