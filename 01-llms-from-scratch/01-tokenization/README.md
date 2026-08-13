# Lesson 1.1 — Tokenization

**Track:** 1 — LLMs from scratch
**Status:** class ready
**Time:** 90 minutes notes + labs, then the assignment
**Prerequisites:** none (Track 0 optional)

## What you will be able to do

- Explain why models do not read characters or words
- Encode and decode with a tokenizer you wrote (BPE)
- Compare word / char / BPE / tiktoken on the same sentence
- Say why your spaCy script is the wrong tool for LLM work
- Predict how tokenization changes cost, context length, and bugs

## Files

| File | Role |
|---|---|
| [notes.md](notes.md) | The lecture |
| [assignment.md](assignment.md) | Homework — do this before Lesson 1.2 |
| [code/01_why_tokenize.py](code/01_why_tokenize.py) | Bytes vs chars vs naive words |
| [code/02_spacy_contrast.py](code/02_spacy_contrast.py) | Your original idea, labeled honestly |
| [code/03_bpe_from_scratch.py](code/03_bpe_from_scratch.py) | Train BPE on a tiny corpus |
| [code/04_use_trained_bpe.py](code/04_use_trained_bpe.py) | Encode / decode with the merges you learned |
| [code/05_tiktoken_and_hf.py](code/05_tiktoken_and_hf.py) | How real models tokenize (optional deps) |
| [data/tiny_corpus.txt](data/tiny_corpus.txt) | What we train BPE on |

## How to take this class

```bash
cd "/Users/mitvavirvadiya/Developer/Code/Gen AI"
source .venv/bin/activate   # if you made one
python 01-llms-from-scratch/01-tokenization/code/01_why_tokenize.py
python 01-llms-from-scratch/01-tokenization/code/03_bpe_from_scratch.py
python 01-llms-from-scratch/01-tokenization/code/04_use_trained_bpe.py
# 05 needs: pip install tiktoken transformers
```

Then write answers in `assignment.md` under **My answers**.

## Next

[Lesson 1.2 — Embeddings](../02-embeddings/README.md)
