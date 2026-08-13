# Parameters and weights — lecture notes

## One-sentence truth

A parameter is a learned number. "7B" means about 7 billion of them.
Weights are those numbers arranged as matrices. The file on disk is
just that table, plus the tokenizer.

## Do this again

Rough VRAM / RAM for *inference* (weights only, not activations):

```
bytes ≈ n_params * bytes_per_param
fp16 / bf16 : 2 bytes  →  7B ≈ 14 GB
int8        : 1 byte   →  7B ≈  7 GB
int4        : 0.5      →  7B ≈  3.5 GB
```

Activations, KV cache, and batch size add more (Track 2).

---

## 1. Where the 7B lives (decoder-only, order of magnitude)

For each layer:

- attention: `W_q, W_k, W_v, W_o` ≈ `4 * d * d` (less with GQA)
- FFN (SwiGLU): `W_gate, W_up, W_down` ≈ `3 * d * d_ff` with `d_ff ≈ 8/3 d` to `4d`

Plus:

- embedding table `vocab * d` (and maybe a tied lm_head)
- norms: tiny

Worked sketch, Llama-ish 7B: `n_layer=32, d=4096, d_ff=11008, vocab=32k`.
The FFN dominates. Embeddings are a few hundred million. Norms are noise.

You do not need the exact paper formula. You need to know **which knobs
multiply**:

```
params ≈ n_layer * (attn + ffn) + vocab * d
```

---

## 2. Weights vs activations vs optimizer state

| Thing | Lives | Size |
|---|---|---|
| Weights | always | `n_params * dtype` |
| Activations | during forward | grows with batch × seq × d × layers |
| Gradients | during training | same as weights |
| AdamW state | during training | ~2× weights (m and v) |

**Inference** needs weights + activations + KV cache.
**Full fine-tune** needs weights + grads + optimizer ≈ **4×** more than
fp16 weights. That is why LoRA exists (Track 2).

---

## 3. Files you will see

| Format | What |
|---|---|
| `.safetensors` | standard HF weight dump. Fast, no pickle RCE. |
| `pytorch_model.bin` | old pickle. Avoid when you can. |
| `.gguf` | llama.cpp / Ollama. Often already quantized. |
| `config.json` | architecture hyperparameters, not weights |
| `tokenizer.json` / `*.model` | the married tokenizer (Lesson 1.1) |

Loading a model is: read `config.json`, allocate the matrices, copy
bytes into them, load the tokenizer.

---

## 4. "Frozen" vs "trainable"

A parameter is just a tensor with `requires_grad` on or off.

- Frozen: used in the forward pass, no gradient, no update
- Trainable: gets a gradient and an optimizer step

LoRA freezes the big matrices and adds tiny trainable ones beside them.

---

## Common mistakes

- "7B means 7 billion tokens of training" — no, that is *parameters*
- Ignoring the embedding table on huge vocabs
- Expecting a 7B fp16 model to fit in 8 GB (the weights alone do not)

## Done when

You can estimate whether a model fits on your machine from name + dtype.

## Next

[Training and backprop](../09-training/README.md)
