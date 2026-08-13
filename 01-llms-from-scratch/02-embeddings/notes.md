# Embeddings — lecture notes

## One-sentence truth

An embedding is a row in a table: `vector = E[token_id]`. The model
learns the numbers in that table so tokens that are used alike end up
pointing alike.

## Do this again

```python
# ids: (batch, seq) int64
# E:   (vocab_size, d_model) float
# x:   (batch, seq, d_model)
x = E[ids]          # numpy / torch advanced indexing
# or, in PyTorch: nn.Embedding(vocab_size, d_model)(ids)
```

That is the entire first layer of an LLM.

---

## 1. IDs are names, not meaning

After Lesson 1.1 you have integers. `hello → 25` and `world → 65` in our
toy BPE. Those numbers are **arbitrary**. 25 is not "closer" to 26 than
to 65. You cannot add them. You cannot ask the model to compare them.

So we replace each ID with a list of learned floats — a vector.

```
id 25  →  [ 0.12, -0.40, 0.88, ... ]     # d_model numbers
id 65  →  [ 0.10, -0.38, 0.91, ... ]
```

If training worked, similar usage → similar vectors → large cosine.

---

## 2. The embedding matrix

Shape: `(vocab_size, d_model)`

| vocab | d_model | parameters in E alone |
|---|---|---|
| 50k | 768 | ~38M (GPT-2 small) |
| 128k | 4096 | ~524M (a modern 7B pays a real tax here) |

`E[i]` is a **parameter**. It is trained by backprop just like any other
weight. At step 0 it is random. After pretraining it is a compressed
record of how that token was used in the corpus.

There is usually a **tie** or a **separate** output head:

- input embed: id → vector
- output head: last vector → vocab logits (often `x @ E.T` if tied)

We will meet that in Lesson 1.3 / 1.7.

---

## 3. Cosine similarity is the ruler

```
cos(a, b) = (a · b) / (‖a‖ ‖b‖)     # -1 to 1
```

- `1` — same direction
- `0` — orthogonal, no linear relationship
- `-1` — opposite

We use cosine (not Euclidean) because embedding training often cares
about **direction** more than raw length. Length can encode frequency
or confidence; direction encodes neighborhood.

In `code/02_cosine_neighbors.py` the vectors are 2-D on purpose so you
can plot them on paper.

---

## 4. Static vs contextual

**Static** (Word2Vec, GloVe, the raw embedding table):

- one vector per token, regardless of sentence
- `bank` in "river bank" = `bank` in "bank account"

**Contextual** (everything after the first transformer block):

- the vector at position `t` has mixed in other tokens via attention
- `bank` becomes two different vectors in those two sentences

The embedding table is still static. Context is added **on top**, by
attention. People say "embeddings" for both. When you need to be
precise:

- *token embedding* = row of `E`
- *hidden state / contextual embedding* = output of a block

RAG (Track 4) usually embeds **chunks of text** with a sentence model
(another network). That is a third thing: a vector for a *passage*, not
a token. Same geometry, different object.

---

## 5. Distributional hypothesis (why this can work)

"You shall know a word by the company it keeps." Tokens that appear in
the same neighborhoods get pulled toward each other by the loss.

Word2Vec made this explicit (predict context from word, or word from
context). An LLM does it implicitly: if two tokens are interchangeable
as the next token, their output rows, and often their input rows, end
up related.

You do not need to implement Word2Vec. You need the intuition: **usage
clusters in vector space.**

---

## 6. What d_model buys you

- Too small (16, 32): cannot separate tens of thousands of tokens
- Typical: 768 → 4096 → 8192 as models scale
- Every later layer talks in `d_model`. Residuals add vectors of this size.

There is no sacred number. It is a capacity / cost knob.

---

## 7. How you will do this again

```python
import torch
import torch.nn as nn

emb = nn.Embedding(vocab_size, d_model)
x = emb(token_ids)          # (B, T, C)

# cosine between two token vectors
a, b = emb.weight[i], emb.weight[j]
cos = torch.nn.functional.cosine_similarity(a, b, dim=0)
```

Hugging Face (Track 3):

```python
from transformers import AutoModel
model = AutoModel.from_pretrained("gpt2")
model.transformer.wte  # the embedding table (word token embeddings)
```

---

## Common mistakes

- Treating the token *id* as a feature ("bigger id = later in vocab")
- Averaging token embeddings and calling it "the sentence meaning"
  (sometimes a baseline, never the full story)
- Mixing embedding spaces: cosine between a GPT vector and a BERT vector
  is meaningless
- Forgetting `pad` still has a vector — mask it or it pollutes means

## Done when

You can write a lookup + cosine from memory, and explain why `bank`
needs attention before it has one meaning.

## Next

The model must *do a job* with these vectors: predict the next token.
[Lesson 1.3](../03-language-modeling/README.md)
