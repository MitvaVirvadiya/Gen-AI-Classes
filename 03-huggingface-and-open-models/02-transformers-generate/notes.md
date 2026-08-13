# transformers: load and generate

## One-sentence truth

`AutoTokenizer` + `AutoModelForCausalLM` + `generate()` is the production
version of Lessons 1.1, 1.7, and 1.10.

## Do this again

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

name = "Qwen/Qwen2.5-0.5B-Instruct"
tok = AutoTokenizer.from_pretrained(name)
model = AutoModelForCausalLM.from_pretrained(name, device_map="auto")

messages = [{"role": "user", "content": "Define a token in one sentence."}]
ids = tok.apply_chat_template(messages, return_tensors="pt", add_generation_prompt=True)
out = model.generate(ids.to(model.device), max_new_tokens=80, temperature=0.7, top_p=0.9)
print(tok.decode(out[0][ids.shape[-1]:], skip_special_tokens=True))
```

---

## Pieces, mapped to Track 1

| HF object | Lesson |
|---|---|
| `tok.encode / decode / apply_chat_template` | 1.1 |
| `model.model.embed_tokens` | 1.2 |
| `model.model.layers[i].self_attn` | 1.6–1.7 |
| `generate(...)` | 1.10 |

## pipeline()

```python
from transformers import pipeline
pipe = pipeline("text-generation", model=name)
```

Fine for a demo. Prefer the explicit path when you need chat templates
or you are debugging.

## device_map and dtype

- `device_map="auto"` — accelerate shards across GPUs / CPU
- `torch_dtype="auto"` or `bfloat16`
- 4-bit: `BitsAndBytesConfig` (Track 2 quantization)

## When we lab this

Right after Track 1 closes. First "real" model you run is a small
instruct model, not GPT-2 unless we want a base-model contrast.
