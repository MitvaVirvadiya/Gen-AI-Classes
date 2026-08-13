# Attention — lecture notes

## One-sentence truth

Attention is a weighted sum of **values**, where the weights come from
how well a **query** matches a set of **keys**.

## Do this again

```
scores  = (Q @ K.T) / sqrt(d_k)     # (n_q, n_k)
weights = softmax(scores, dim=-1)   # rows sum to 1
out     = weights @ V               # (n_q, d_v)
```

That is scaled dot-product attention. The rest of "transformers" is
this, plus masks, plus many heads, plus an MLP.

---

## 1. Retrieval, not magic

Imagine a dusty filing cabinet:

- **Query** — what you walk in asking ("the subject of this sentence")
- **Keys** — labels on the drawers
- **Values** — the papers inside

You score query against every key, turn scores into a distribution,
and take the mixture of values. Differentiable lookup.

A tiny numeric picture (d=2):

```
q = [1, 0]
k1 = [1, 0]    score = 1
k2 = [0, 1]    score = 0
```

Softmax makes the output almost `v1`. The query "found" key 1.

---

## 2. Why divide by √d_k?

Dot products of random d-dimensional vectors grow like `√d` in spread.
Softmax then saturates (weights ≈ one-hot), gradients die. Scaling by
`√d_k` keeps the scores in a friendly range. This is not decoration.

---

## 3. Shapes (write these until they are boring)

| Tensor | Shape |
|---|---|
| Q | `(n_q, d_k)` |
| K | `(n_k, d_k)` |
| V | `(n_k, d_v)` |
| scores | `(n_q, n_k)` |
| out | `(n_q, d_v)` |

In a batch + heads world:

```
Q, K, V : (batch, heads, seq, d_head)
scores  : (batch, heads, seq, seq)
```

If a later bug exists, it is a shape bug.

---

## 4. Cross-attention vs the next lesson

This lesson does **not** assume Q, K, V come from the same place.

- **Cross-attention:** Q from the decoder, K/V from the encoder
  (translation, the 2017 Transformer)
- **Self-attention:** Q, K, V from the same sequence (next lesson)

Same math. Different wiring.

---

## Common mistakes

- Softmax over the wrong axis (must be over keys)
- Forgetting the `√d` scale
- Calling attention "the model understanding" — it is mixing vectors

## Done when

You can implement the three lines (scores, softmax, mix) in numpy
without looking.

## Next

[Self-attention and multi-head](../06-self-attention/README.md)
