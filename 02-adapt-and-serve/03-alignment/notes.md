# Alignment (RLHF / DPO)

## One-sentence truth

SFT teaches "what a good answer looks like." Preference training teaches
"this answer is better than that one" so the model picks the style
humans (or a judge) preferred.

## Do this again (DPO, the one you might actually run)

```
data: prompt, chosen_response, rejected_response
loss: make π_θ(chosen|prompt) higher than π_θ(rejected|prompt)
      relative to a frozen reference model π_ref
```

No separate reward model. No PPO loop. That is why DPO displaced a lot
of RLHF in open-source.

---

## RLHF (the ChatGPT original)

1. SFT a base model
2. Humans rank answers → train a **reward model**
3. Optimize the policy with PPO to raise reward, with a KL penalty
   so it does not flee the SFT model

Powerful. Expensive. Unstable. You will not implement PPO this year
unless you choose to.

## What "aligned" is not

It is not "the model knows the truth." It is "the model prefers
answers that scored well on a preference dataset." Those preferences
can be wrong, political, or just "sound confident."

## When we need this

After you can SFT. For most product work, good SFT + good eval beats
a sloppy DPO run. We treat this as literacy, then a small DPO lab if
you still want it.
