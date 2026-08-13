# tokenizers + datasets

## One-sentence truth

`tokenizers` is the fast Rust library behind HF tokenizers.
`datasets` is an on-disk, memory-mapped table with `.map()`.

## Do this again

```python
from datasets import load_dataset

ds = load_dataset("json", data_files="sft.jsonl", split="train")
ds = ds.map(tokenize_fn, batched=True, remove_columns=ds.column_names)
```

`tokenize_fn` must use the **same** tokenizer as the model you will train.

---

## Collators

A collator pads a list of variable-length examples into a rectangular
batch and builds `attention_mask`. Wrong pad token / wrong label mask
is the #1 silent SFT bug.

## Why not pandas

LLM datasets are large. `datasets` streams, caches Arrow, and plays
with `Trainer`. Use it.

## When we lab this

The SFT lesson: we will write a 50-row JSONL by hand, tokenize it,
and inspect `input_ids` vs `labels` before we touch `Trainer`.
