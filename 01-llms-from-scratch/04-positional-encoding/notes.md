# Positional encoding — lecture notes

## One-sentence truth

Self-attention has no built-in order. We inject position so that
"who is next to whom" is visible to the model.

## Do this again

Three families you will meet:

| Family | How | Used by |
|---|---|---|
| **Add a vector** | `x_t = e_t + p_t` | original Transformer (sin/cos), GPT-2 (learned `p_t`) |
| **Rotate Q and K** | RoPE: rotate pairs of dims by `t * θ` | Llama, Qwen, most modern decoder-only |
| **Bias the scores** | ALiBi: subtract `slope * distance` from attention logits | some long-context work |

If you remember one modern name, remember **RoPE**.

---

## 1. Why attention is position-blind

The score `q · k` does not contain `t` or `s`. Permute the tokens, the
set of scores is the same (causal mask aside). Language is not a bag of
tokens. Order is the whole game.

---

## 2. Sinusoidal (the 2017 paper)

For dimension `2i` and `2i+1` at position `t`:

```
p[t, 2i]     = sin(t / 10000^(2i/d))
p[t, 2i+1]   = cos(t / 10000^(2i/d))
```

Then `x = token_embed + p`.

Why sinusoids? Nearby positions look similar; there is a linear way to
attend relatively (`p_{t+k}` is a linear function of `p_t`). You do not
need to memorize the formula. You need: **fixed, no extra parameters,
adds to the embedding.**

---

## 3. Learned absolute positions (GPT-2)

A second table `P` of shape `(max_seq, d_model)`. `x_t = E[id_t] + P[t]`.

Simple. Hard ceiling: you cannot natively go past `max_seq` without
hacks (interpolation, ALiBi, RoPE scaling).

---

## 4. RoPE (what you will actually see)

Do not add a vector. **Rotate** the query and key of each token in 2-D
planes, by an angle proportional to its position.

Intuition: the dot product `q_t · k_s` then depends on `(t - s)`, i.e.
*relative* distance, which is what language usually cares about
("the adjective just before the noun").

Properties:

- no extra `d_model` added into the residual stream
- extrapolates (with caveats / scaling tricks) beyond train length
- implemented inside the attention kernel, not as a first-layer add

You will not implement full RoPE until the transformer lab. For now:
**RoPE = positions live in the angles of Q and K.**

---

## 5. ALiBi

Leave Q/K unrotated. When you compute attention scores, subtract
`m * |t - s|` (head-specific slope `m`). Distant tokens are down-weighted
by construction. Elegant for long context. Less universal than RoPE today.

---

## Common mistakes

- Thinking the model "knows" index `t` because Python does
- Adding RoPE *and* learned absolute positions by accident
- Using GPT-2-style `P[t]` past the trained length and expecting magic

## Done when

You can say, for a named model (GPT-2 vs Llama), *where* position enters
the math.

## Next

[Attention](../05-attention/README.md) — the actual mixing.
