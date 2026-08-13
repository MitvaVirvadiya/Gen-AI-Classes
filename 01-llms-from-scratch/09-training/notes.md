# Training and backpropagation — lecture notes

## One-sentence truth

Training is a loop: batch of tokens → forward → cross-entropy on the
shifted targets → backward (chain rule) → optimizer step. Repeat until
the loss stops being interesting.

## Do this again

```python
for batch in data:
    logits = model(batch.inputs)              # (B, T, vocab)
    loss = cross_entropy(
        logits.view(-1, vocab),
        batch.targets.view(-1),
        ignore_index=pad_id,
    )
    opt.zero_grad()
    loss.backward()
    clip_grad_norm_(model.parameters(), 1.0)
    opt.step()
```

That is a pretraining step. SFT is the same loop on a different dataset.

---

## 1. What backprop actually is

Every op (matmul, gelu, softmax) knows its local derivative.
Backprop walks the graph from `loss` to every parameter and multiplies
those local derivatives (chain rule).

You do not write this by hand after Lesson 0. Autograd (PyTorch) does.
You *do* need:

- the graph must be differentiable (it is)
- a NaN anywhere poisons everything
- `ignore_index` for pads or you train the model to predict padding

---

## 2. The optimizer

**SGD:** `W -= lr * grad`
**AdamW:** keeps a per-parameter momentum and variance, plus **weight
decay** that actually decays `W` (not the Adam math). This is the default
for transformers.

Knobs that matter more than which Adam fork you picked:

- **learning rate** + **warmup** + **cosine decay**
- **batch size** (tokens per step, not "sentences")
- **grad clip** (one bad batch should not explode the run)
- **weight decay**

---

## 3. Data is the real model

Pretraining data is trillions of tokens: web, books, code, papers.
The architecture is public. The data mix is the secret sauce.

For *us*, in the lab:

- a tiny text file (Shakespeare, or our own notes)
- context length 64–256
- minutes on a laptop

You will overfit on purpose. That is how you know the loop works
(loss → 0, model memorizes). Then we talk about generalization.

---

## 4. Three trainings people collapse into one word

| Stage | Data | Result |
|---|---|---|
| **Pretrain** | raw internet-scale text | base model |
| **SFT** | instruction → response | follows requests |
| **Preference** (RLHF/DPO) | chosen vs rejected | more "aligned" |

Same loop (or a close cousin). Different labels. Track 2 unpacks 2 and 3.

---

## 5. Scaling laws (one paragraph)

Loss falls as a power law of **parameters**, **data**, and **compute**.
A bigger model on too little data underperforms a smaller one trained
correctly. Chinchilla: you should scale tokens with parameters, not
just stack layers and reuse the same corpus.

---

## Common mistakes

- Forgetting to shift labels
- No `ignore_index` on pad
- LR too high → NaNs; too low → "nothing happens"
- Calling a 500-step overfit on Shakespeare "pretraining an LLM"

## Done when

You can write the training loop from memory and say what each line is for.

## Next

[Sampling](../10-sampling/README.md) — turning logits into text.
