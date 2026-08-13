# 0.1 Math you actually need

**Track:** 0 — Foundations
**Time:** 45 minutes
**Status:** gist notes (no assignment unless you feel rusty)

## One-sentence truth

An LLM is matrix multiplies, a softmax, and a cross-entropy loss, stacked
many times. If those three are solid, the rest of Track 1 is vocabulary.

## Do this again

When a later lesson writes `softmax(QKᵀ / √d) V`, come back here.

## Vectors

A vector is an ordered list of numbers. In this course it is almost always
a **row of features for one token** or a **column of weights**.

```
v = [1.0, 2.0, 3.0]     # 3-dimensional
```

- **Length / L2 norm:** `‖v‖ = sqrt(1² + 2² + 3²)`
- **Dot product:** `a · b = a1*b1 + a2*b2 + ...` — "how aligned are they?"
- **Cosine similarity:** `(a · b) / (‖a‖ ‖b‖)` — same idea, scale-invariant

Attention is a pile of dot products.

## Matrices

A matrix is a rectangle of numbers. We care about multiply:

```
(m × n) @ (n × p)  →  (m × p)
```

A linear layer is `x @ W + b`.

- `x` is `(batch, d_in)`
- `W` is `(d_in, d_out)`
- output is `(batch, d_out)`

That is 90% of a transformer's compute.

## Softmax

Turns any list of numbers ("logits") into a probability distribution:
non-negative, sums to 1.

```
softmax(z)_i = exp(z_i) / sum_j exp(z_j)
```

Properties you will use constantly:

- Bigger logit → bigger probability, but never 0 or 1 unless the gap is huge
- Subtracting a constant from all logits does not change the result
  (numerically we subtract `max(z)` so `exp` does not explode)
- **Temperature** later is just `softmax(z / T)`

## Cross-entropy

For next-token prediction the target is "token number 42 is the answer."
The model produced a vocab-sized probability vector `p`. Loss is:

```
loss = -log(p[42])
```

- If `p[42] = 1`, loss = 0 (perfect)
- If `p[42] = 0.01`, loss ≈ 4.6 (bad)
- If `p[42] ≈ 0`, loss → ∞ (the model assigned no mass to the truth)

**Perplexity** is `exp(average loss)`. It is "how many tokens was the
model typically torn between?"

## Gradient (just the idea)

Loss is a function of the weights. The **gradient** is the direction of
steepest increase. We step the other way:

```
W ← W - lr * dLoss/dW
```

That is gradient descent. AdamW is a fancier version of this update.
You do not need to derive Adam. You need to know the loss must be
differentiable, which softmax + cross-entropy is.

## Shapes you should be able to read

| Object | Typical shape |
|---|---|
| token ids | `(batch, seq)` |
| embeddings | `(batch, seq, d_model)` |
| attention scores | `(batch, heads, seq, seq)` |
| logits | `(batch, seq, vocab)` |

If a bug exists in Track 1 code, it is usually a shape bug.

## Done when

You can, on paper:

1. Compute a 2-D dot product
2. Write softmax for `[1, 2, 3]` (calculator fine)
3. Say what happens to loss if the model puts probability 1 on the wrong token
