# Tokenization — lecture notes

## One-sentence truth

A tokenizer is a reversible map `text ↔ list of integers`. The model never
sees words. It sees those integers.

## Do this again

```text
text  --encode-->  token ids  --model-->  next-id  --decode-->  text
```

If a bug looks like "the model is bad at code / Hindi / spaces / JSON,"
check the tokenizer before the weights.

---

## 1. Why tokenize at all?

Neural nets multiply numbers. A string is not a number.

You must pick a **finite vocabulary** and represent every input as a
sequence of IDs from that set.

```
"cat"  →  7592      # example, not universal
" cats" → 4590      # leading space is often its own token
"Cat"  →  1629      # case can be a different ID
```

Those IDs index an embedding table (next lesson). Wrong tokenizer + right
weights = garbage, because the IDs no longer mean what the model was
trained on.

**Rule:** a model and its tokenizer are a married pair. Never mix them.

---

## 2. Three bad-or-good ideas

### Word tokens

Split on whitespace / punctuation.

```
"I love LLMs"  →  ["I", "love", "LLMs"]
```

Dies on:

- **OOV** — a new last name, a new library, a typo. No ID → crash or `<unk>`
- **Vocab explosion** — English has hundreds of thousands of word forms
- **Morphology** — `run` / `running` / `rerun` are unrelated IDs

Your spaCy script lives here. That is correct for *linguistic* NLP
(POS tags, entities). It is not how GPT or Llama read text.

### Character / byte tokens

```
"I love LLMs"  →  I,  , l, o, v, e,  , L, L, M, s
```

Never OOV (especially if you use raw bytes, 256 symbols). But:

- Sequences get 4–10× longer
- Attention is O(n²) in sequence length — you just burned the context window
- The model must *learn* that `c-a-t` is a unit, every time

### Subword tokens (what LLMs actually use)

Keep frequent chunks as one token (`the`, `ing`, `http`, `</`), split rare
ones (`Virvadiya` → `Vir` + `vad` + `iya`).

This is the compromise:

- vocab of ~32k–200k (fits in a table)
- almost never truly unknown (fall back to bytes)
- common words stay short; rare words cost more tokens

---

## 3. Byte Pair Encoding, the algorithm

BPE is a compression algorithm that became a tokenizer.

**Train (learn the vocab):**

1. Start with a base vocab. Modern GPT-style BPE starts from **256 bytes**.
   Our teaching version starts from **characters** so you can watch it.
2. Count every adjacent pair in the corpus.
3. Merge the most frequent pair into a new token. Add it to the vocab.
4. Repeat until you hit a target vocab size (or a merge count).

**Encode (use the vocab):**

1. Split the new text into the base units (chars or bytes).
2. Apply the learned merges, **in the same order they were learned**.
3. Look up each remaining piece in the vocab → IDs.

**Decode:**

Join the pieces. With byte-level BPE this is lossless for any unicode.

Worked toy example on `aaabdaaabac`:

```
start:  a a a b d a a a b a c
merge aa → A:  A a b d A a b a c
merge Aa → B:  B b d B b a c
...
```

You will run this for real in `code/03_bpe_from_scratch.py`.

### WordPiece vs BPE vs Unigram / SentencePiece

| Algorithm | Used by | Merge rule |
|---|---|---|
| BPE | GPT-2/3/4 (tiktoken), many others | most frequent pair |
| WordPiece | BERT, DistilBERT | pair that most improves likelihood |
| Unigram + SentencePiece | Llama, T5, Gemma, many multilingual | start big, prune tokens that hurt likelihood |

You do not implement all three. You implement BPE so the others are
"same job, different scoring."

---

## 4. What a real tokenizer also stores

- **vocab:** `token_string → id`
- **merges:** ordered list of pairs
- **special tokens:** `pad`, `unk`, `bos`, `eos`, and chat markers
- **pretokenization rules:** how to split before BPE (GPT-2 uses a regex
  so letters, numbers, and punctuation do not freely merge)
- **byte fallback:** so any unicode has a path to IDs

### Special tokens are not words

| Token | Job |
|---|---|
| `<pad>` | fill a batch to the same length. Model must *ignore* these (mask). |
| `<unk>` | leftover unknown. Byte-level BPE almost never needs it. |
| `<bos>` / `<eos>` | begin / end of sequence |
| `<\|user\|>`, `<<SYS>>`, etc. | chat template. Wrong template = the model "gets dumber." |

Padding IDs still occupy the embedding table and the sequence. They must
be masked in attention or the model attends to fake tokens.

---

## 5. Encode / decode pitfalls

These show up in production more than in papers.

1. **Leading spaces.** GPT-2 style: `" Hello"` is often one token, `"Hello"`
   another. Prompt formatting changes token IDs.
2. **Trailing whitespace** can glue to the next token or become its own.
3. **Detokenization.** Naive `"".join` vs `" ".join` — BPE pieces already
   contain the spaces (as `Ġ` in GPT-2).
4. **Multilingual tax.** English `"hello"` = 1 token. The same meaning in
   another script may be 5–15 tokens. Cost and quality follow.
5. **Code.** Indentation, operators, identifiers. A model with a code-aware
   tokenizer spends fewer tokens on Python.
6. **Numbers.** `1234` might be `123`+`4` or `12`+`34` or one token.
   Arithmetic failures are sometimes tokenizer failures.
7. **Never mix tokenizers.** Decode GPT-4 IDs with a Llama tokenizer and
   you get nonsense, not a translation.

---

## 6. Why this is the first lesson

Everything downstream is measured in tokens:

- **Context window** is tokens, not words or pages
- **API bills** are tokens
- **Attention compute** is O(seq_len²)
- **Embedding table** is `vocab_size × d_model` parameters
  (a 128k vocab with d=4096 is already ~0.5B parameters)

If you do not understand tokenization you will misread every later number.

---

## 7. spaCy vs LLM tokenizers (your existing file)

`tokenization/text-tokens.py` does this:

```python
nlp = spacy.load("en_core_web_sm")
[(token.text, token.is_alpha, token.is_digit, token.is_punct) for token in nlp(text)]
```

That answers: "what are the words, and which are punctuation?"

An LLM tokenizer answers: "what IDs did *this* model train on?"

Keep spaCy for classical NLP. For anything that talks to an LLM, use
**that model's** tokenizer (`tiktoken` for OpenAI, `AutoTokenizer` for HF,
the GGUF metadata for llama.cpp).

We copied the idea into `code/02_spacy_contrast.py` so the contrast lives
inside the lesson.

---

## 8. How you will do this again in later tracks

```python
# Hugging Face (Track 3)
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B")
ids = tok.encode("Hello, world")
text = tok.decode(ids)

# OpenAI-compatible (Track 4)
import tiktoken
enc = tiktoken.get_encoding("o200k_base")  # GPT-4o family
ids = enc.encode("Hello, world")
```

Same job. Different files on disk. Same mental model you are building today.

---

## Common mistakes

- Counting words and calling them tokens
- Using spaCy / `str.split` to budget an LLM context window
- Fine-tuning with a different tokenizer than the base model
- Forgetting the chat template
- Assuming 1 token ≈ 4 characters as a law (it is an English *average*)

## Done when

You can:

1. Train a small BPE and encode a sentence the model never saw
2. Explain OOV and why byte-level BPE almost never has it
3. Look at two tokenizations of the same text and say which model will
   pay more and why
4. Finish [assignment.md](assignment.md)

## Next

Embeddings: those IDs become vectors.
[Lesson 1.2](../02-embeddings/README.md)
