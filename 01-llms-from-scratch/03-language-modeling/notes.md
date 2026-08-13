# Language modeling objective — lecture notes

## One-sentence truth

A causal LLM is trained to predict the next token. Every capability you
see (coding, chat, RAG answers) is a side effect of that objective plus
later fine-tuning.

## Do this again

```
tokens:    [the, cat, sat, on, the, mat]
inputs:    [the, cat, sat, on, the]
targets:   [cat, sat, on, the, mat]     # shifted by one

for each position t:
    logits = model(tokens[:t])          # vocab-sized
    loss  += -log softmax(logits)[target_t]
```

That loop, averaged, is the pretraining loss.

---

## 1. The probability the model owns

```
P(x1, x2, ..., xT) = P(x1) * P(x2|x1) * P(x3|x1,x2) * ... * P(xT|x1..xT-1)
```

The chain rule turns "probability of a document" into "predict each next
token given the left context." That is why we use **causal** attention
(Lesson 1.6): the model may not peek at the future while predicting it.

---

## 2. Logits → softmax → loss

The last layer produces **logits** `z` of shape `(batch, seq, vocab)`.

```
p = softmax(z)                  # probabilities
loss = -log(p[target_id])       # cross-entropy, one position
```

In code you never write the softmax yourself for the loss. You use
`cross_entropy(logits, targets)` which is more stable (log-softmax fused).

**Perplexity** = `exp(mean loss)`.

- PPL 1 = perfect certainty
- PPL 100 ≈ "as unsure as a fair 100-way dice"
- Compare PPL only with the **same tokenizer** (different vocab → different PPL)

---

## 3. Teacher forcing

During training we do **not** feed the model's own guesses back in.
We feed the *true* previous tokens (the dataset) and ask for the next
true token at every position in parallel.

That is why a full sequence of length T produces T loss terms in one
forward pass. Generation (Lesson 1.10) is different: there we *do* feed
predictions back. Train ≠ generate.

---

## 4. Context window

The model only conditions on the last `n` tokens (4k, 8k, 128k, ...).
Anything older is gone unless you retrieve it (RAG) or summarize it
(memory). The window is measured in **tokens**, not words (Lesson 1.1).

---

## 5. Base model vs assistant

A **base** model, after this objective only, completes text:

```
"The capital of France is" → " Paris, a city that..."
```

It does not follow "Write me a poem." That behavior is **SFT + alignment**
(Track 2). Same architecture, different data after pretraining.

---

## Common mistakes

- Thinking the model is trained to "be helpful" from the start
- Comparing perplexity across tokenizers
- Forgetting the shift-by-one (inputs vs labels)
- Measuring quality only on train loss (it will go down even if the
  model is memorizing junk)

## Done when

You can write the shift, the loss, and the difference between training
and generation on a whiteboard.

## Next

Attention still has no idea of order. [Positional encoding](../04-positional-encoding/README.md).
