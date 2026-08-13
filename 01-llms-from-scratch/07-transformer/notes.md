# Transformer architecture — lecture notes

## One-sentence truth

A decoder-only transformer is: embed + positions, then N identical
blocks of (norm → attention → residual → norm → FFN → residual), then
a linear head to vocab logits.

## Do this again (Llama-style pre-norm)

```
x = embed(ids)                  # + RoPE inside attention, not added here
for block in blocks:
    x = x + attn(rms_norm(x))
    x = x + ffn(rms_norm(x))
logits = lm_head(rms_norm(x))   # (B, T, vocab)
```

That is the whole model. Papers add flavor (SwiGLU, GQA, QK-norm).
The skeleton does not change.

---

## 1. The block, unpacked

**Residual.** `x + sublayer(x)`. Depth would be untrainable without this.
The residual stream is the model's working memory. Attention and FFN
*read* from it and *write* back a delta.

**Norm.** LayerNorm (GPT-2) or RMSNorm (Llama). Stabilizes scale.
**Pre-norm** (norm before the sublayer) is the modern default — trains
deeper, cleaner.

**Attention.** Lesson 1.6. Tokens talk to each other.

**FFN / MLP.** Tokens do *not* talk. Each position is processed alone:

```
# GPT-2 style
h = gelu(x @ W1 + b1)     # expand to 4*d_model
y = h @ W2 + b2           # project back

# Llama style (SwiGLU, no bias)
y = (silu(x @ W_gate) * (x @ W_up)) @ W_down
```

Most of the parameters live here, not in attention.

---

## 2. Three topologies

| | Looks at | Job |
|---|---|---|
| Encoder-only (BERT) | bidirectional self-attn | classify, embed |
| Encoder-decoder (T5) | encoder + cross + decoder | translate, span infill |
| Decoder-only (GPT, Llama) | causal self-attn | next token / generate |

We build decoder-only. That is the LLM.

---

## 3. A tiny config you can hold in your head

```
vocab      = 128
n_layer    = 4
n_head     = 4
d_model    = 128
d_ff       = 512
block_size = 64
```

This will train on a laptop in Lesson 1.9. Scaling up is the same
diagram with bigger numbers.

---

## 4. Information flow in one sentence

Token IDs become vectors; each block lets them read each other then
think individually; the last vector at the last position is projected
to a bet over the next ID.

---

## Common mistakes

- Post-norm vs pre-norm mixups when reading old papers
- Forgetting the residual (the net becomes untrainable fast)
- Calling the FFN "feed-forward *network of the whole model*" — it is
  per-token, inside each block

## Done when

You can draw one block and stack it, and name every tensor's shape.

## Next

[Parameters and weights](../08-parameters-and-weights/README.md) — what "7B" means.
