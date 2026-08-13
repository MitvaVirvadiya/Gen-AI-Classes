# Self-attention and multi-head — lecture notes

## One-sentence truth

Self-attention: every token builds a query, key, and value from *itself*,
then looks at the other tokens. Multi-head: do that in several subspaces
and concatenate.

## Do this again

```
# x: (B, T, C)   C = d_model
Q = x @ W_q      # (B, T, C)
K = x @ W_k
V = x @ W_v

# split into H heads, d_head = C / H
# scores: (B, H, T, T)
scores = (Q @ K.transpose(-2, -1)) / sqrt(d_head)
scores = scores + causal_mask     # -inf above the diagonal
w = softmax(scores)
y = (w @ V).merge_heads @ W_o     # back to (B, T, C)
```

---

## 1. Self vs cross (the ChatGPT list, cleaned up)

| | Q from | K, V from |
|---|---|---|
| Self-attention | this sequence | this sequence |
| Cross-attention | decoder sequence | encoder sequence |

A GPT-style LLM is **decoder-only**: only causal self-attention. No
encoder, no cross-attention. BERT is encoder-only: bidirectional
self-attention (no causal mask). T5 is encoder-decoder: both.

When someone says "LLM" in 2026 they almost always mean decoder-only.

---

## 2. The causal mask

For next-token training, position `t` must not see `t+1, t+2, ...`.

```
mask[t, s] = 0 if s <= t else -inf
scores = scores + mask
```

Softmax of `-inf` is 0. The future is gone.

Without this mask the model cheats: it "predicts" a token it already
looked at. Loss collapses, generation is nonsense.

Padding gets a similar mask: `pad` keys should be `-inf` so they receive
no weight.

---

## 3. Why many heads?

One head is forced to pick *one* mixing pattern. Several heads can
specialize:

- one tracks the subject
- one tracks recent punctuation
- one copies a name from earlier in the prompt

Empirically this helps. `d_head` is usually 64 or 128.
`n_heads * d_head = d_model` (or `d_model` for Q and a smaller K/V in GQA).

### GQA / MQA (you will see this on Llama)

- **MHA:** every head has its own K and V
- **MQA:** all heads share one K, V (faster, less KV cache)
- **GQA:** groups of heads share K, V (Llama-3 default)

Same idea, cheaper generation.

---

## 4. Cost

Scores are `(T, T)` per head. Memory and compute grow **quadratically**
with sequence length. That is why 128k context is an engineering problem
(Track 2 inference) and why tokenization (Lesson 1.1) is a cost problem.

---

## Common mistakes

- Applying softmax, *then* masking (too late — the future already stole mass)
- Mixing up `d_model` and `d_head`
- Thinking 32 heads means 32× more *tokens* of context

## Done when

You can draw a 4-token causal score matrix and mark which cells are `-inf`.

## Next

[Transformer architecture](../07-transformer/README.md) — wrap this in a block.
