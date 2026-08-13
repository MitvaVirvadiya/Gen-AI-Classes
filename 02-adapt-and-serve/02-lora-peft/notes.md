# LoRA / PEFT

## One-sentence truth

LoRA freezes the pretrained matrix `W` and trains two skinny matrices
`A, B` such that `W' = W + B A`. You store and share `B A`, not a new 14 GB file.

## Do this again

```
# W is (d × d), frozen
# A is (r × d), B is (d × r), r = 8 or 16 typically
h = x @ W + scale * (x @ A.T @ B.T)     # conceptually W + B A
```

PEFT = the family name (LoRA, QLoRA, adapters, prefix-tune, ...).
LoRA is the one you will actually use.

---

## Why this works

The update needed to specialize a giant model is often **low rank**.
You do not need to move all 7B numbers to teach it your JSON format.

Practical effects:

- train on a consumer GPU (especially **QLoRA**: 4-bit frozen base + LoRA)
- one base + many adapters (one per task / customer)
- merge adapters back into `W` at ship time if you want a single file

## Knobs

| Knob | Typical | Meaning |
|---|---|---|
| `r` | 8–64 | rank. bigger = more capacity, more overfit risk |
| `alpha` | 16–32 | scale = alpha/r |
| target modules | `q_proj, v_proj` or all linear | where to attach |
| dropout | 0–0.1 | regularize the adapter |

## QLoRA

Load the base in 4-bit (bitsandbytes / AWQ), keep it frozen, train LoRA
in 16-bit. This is how people fine-tune 7B–70B on one card.

## When we lab this

Track 3 with `peft` + `trl`. You will attach a LoRA, train 50 steps,
save a 20 MB adapter, load it back.
