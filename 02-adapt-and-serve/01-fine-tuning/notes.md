# Fine-tuning (SFT)

## One-sentence truth

Supervised fine-tuning continues next-token training, but on
**instruction → response** pairs (plus a chat template), so a base
model starts behaving like a product.

## Do this again

```
messages = [
  {role: system, content: "..."},
  {role: user,   content: "..."},
  {role: assistant, content: "..."},   # this is what we train on
]
tokens = tokenizer.apply_chat_template(messages)
# loss only on assistant tokens, not on the user prompt
```

Same loop as Lesson 1.9. Different data. Mask the prompt.

---

## Why SFT exists

A base model completes text. Users want it to *answer*. SFT shows
thousands to millions of (prompt, good answer) examples. The weights
move just enough to prefer that format.

## What goes wrong

- **Catastrophic forgetting:** too many steps / too high LR and the
  model loses pretrain knowledge
- **Chat template mismatch:** train with one template, serve with another
- **Training on the prompt:** model learns to copy the question
- **Garbage data:** SFT on bad answers teaches bad answers. Data > LR

## Full FT vs PEFT

Full FT updates every weight. Best quality ceiling, expensive
(Lesson 1.8: Adam state). Next lesson is how to avoid that.

## When we lab this

Track 3, with `trl.SFTTrainer` on a tiny instruction set. Not now.
