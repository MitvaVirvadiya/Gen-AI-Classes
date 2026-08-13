# Quantization

## One-sentence truth

Store (and sometimes compute) weights in fewer bits so the model fits
in RAM/VRAM and moves faster. Quality drops a little if you do it well,
a lot if you do not.

## Do this again

```
fp16  : 2 bytes/weight     7B ≈ 14 GB
int8  : 1 byte             7B ≈  7 GB
int4  : 0.5 byte           7B ≈  3.5 GB   (GGUF Q4, AWQ, GPTQ)
```

Ollama / llama.cpp: download a `Q4_K_M` GGUF and run. Hugging Face:
`bitsandbytes` load_in_4bit, or an AWQ/GPTQ repo.

---

## Two different jobs

| | When | Example |
|---|---|---|
| **Weight-only** | inference | GGUF, GPTQ, AWQ |
| **QAT / QLoRA** | training adapters on quantized base | QLoRA |

## Methods in one line each

- **LLM.int8 / bitsandbytes:** dynamic, easy, not the smallest
- **GPTQ:** offline calibration, popular HF weights
- **AWQ:** protect "salient" channels, often better 4-bit quality
- **GGUF + k-quants:** llama.cpp's formats. What local apps use

## What breaks first

Math, long-tail names, multilingual. Always eval (2.4) after quantizing.
Do not ship Q2 because it is cute.

## ChatGPT list note

Quantization *is* compression of weights. The next lesson is the other
family: fewer weights, not fewer bits.
