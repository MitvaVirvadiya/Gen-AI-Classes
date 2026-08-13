# Compression (not quantization)

## One-sentence truth

Quantization shrinks *bits per weight*. Compression here means *fewer
weights*: distillation, pruning, smaller architectures.

## Do this again

| Method | Idea | You will meet it as |
|---|---|---|
| **Distillation** | student mimics teacher logits / hidden states | DistilBERT, tiny Llama distillations |
| **Pruning** | delete weights or heads that barely matter | less common for modern LLMs |
| **Width/depth shrink** | train a smaller cousin | Gemma-2B vs 27B, Qwen-0.5B |
| **MoE** | many experts, few active per token | Mixtral — compress *compute*, not disk |

---

## Distillation, the useful one

```
teacher (frozen, big) produces logits on a corpus
student (small) trains to match those logits  +  the real next-token loss
```

The student learns a smoother target than hard labels. Works best when
you have a lot of unlabeled text and a strong teacher.

## When to bother

- you need on-device or a tight latency budget
- you already quantized and it is still too big
- you do not have the data/compute to train small from scratch

Most builders should **pick a smaller trained model** (0.5B–3B) before
they invent a distillation pipeline.

## ChatGPT list note

Steps 11 and 12 on that list were one blob. We split them: bits vs
structure. Do not do both blindly on day one.
