# Sampling and generation — lecture notes

## One-sentence truth

The model outputs a probability distribution over the vocab. Sampling
is how we pick the next ID from that distribution, append it, and repeat.

## Do this again

```
ids = encode(prompt)
for _ in range(max_new):
    logits = model(ids)[:, -1, :]          # last position only
    logits = logits / temperature
    logits = top_k_or_top_p(logits)
    next_id = categorical_sample(softmax(logits))
    ids.append(next_id)
    if next_id == eos: break
text = decode(ids)
```

Training used teacher forcing (true prefix). Generation uses its own
outputs. Errors compound. That is why long generations drift.

---

## 1. Greedy vs sample

- **Greedy:** `argmax`. Deterministic. Often repetitive.
- **Sample:** draw from the softmax. Diverse, can be stupid.

Nobody serious uses raw full-vocab sampling on a chat model. They
reshape the distribution first.

---

## 2. Temperature

```
p = softmax(logits / T)
```

- `T → 0` — approaches greedy
- `T = 1` — the model's native distribution
- `T > 1` — flatter, more random
- `T < 1` — peakier, more conservative

Temperature does not make the model "more creative" in any deep sense.
It makes the dice fairer or less fair.

---

## 3. Top-k and top-p (nucleus)

**Top-k:** keep the k largest logits, zero the rest, renormalize.
Typical k: 20–100.

**Top-p:** keep the smallest set of tokens whose probabilities sum to
`p` (0.9, 0.95). The set size *adapts*: 2 tokens if the model is sure,
40 if it is not.

These exist to cut off the long tail of garbage tokens the model barely
believes in, which otherwise get sampled on a long enough horizon.

You can combine: top-k *then* top-p, then temperature. Libraries differ
on order. Read the docs when it matters.

---

## 4. Other knobs you will meet

- **Repetition penalty** — down-weight IDs already in the prompt/output
- **Presence / frequency penalty** — OpenAI-style cousins
- **Min-p** — keep tokens above `p * max_prob` (modern alternative)
- **Beam search** — keep several prefixes. Rare for chat, common in
  translation / short constrained tasks
- **EOS / stop sequences** — how the loop ends

---

## 5. Prefill vs decode (preview of Track 2)

- **Prefill:** run the whole prompt in one parallel forward. Build KV cache.
- **Decode:** one new token at a time, reuse the cache.

Latency you feel in chat is almost all decode. This is why KV cache
and speculative decoding matter later.

---

## Common mistakes

- Temperature on already-softmaxed probabilities (must be on logits)
- Top-p = 0 or 1 accidentally, then wondering why it is greedy or wild
- Comparing two models with different default sampling configs

## Done when

You can explain one weird output as "the sampler, not the weights"
when that is actually true — and know when it is not.

## Track 1 ends here

You now have the spine: tokens → vectors → positions → attention →
block → weights → train → sample.

Next track: take a model you did **not** pretrain and make it useful.
[Track 2](../../02-adapt-and-serve/README.md)
