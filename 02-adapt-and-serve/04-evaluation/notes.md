# Evaluation

## One-sentence truth

If you cannot measure it, you did not improve it. Loss going down is
not a product metric.

## Do this again

Four layers, cheapest first:

1. **Unit checks** — tokenizer round-trip, chat template, JSON parses
2. **Held-out loss / perplexity** — same tokenizer only
3. **Automatic task metrics** — exact match, F1, pass@k for code,
   retrieval hit-rate for RAG
4. **Judge + humans** — LLM-as-judge with a rubric, then spot-check

Never skip 1. Do not start at 4.

---

## Benchmarks you will hear

MMLU, HellaSwag, GSM8K, HumanEval, MT-Bench, Arena. They are useful
*comparisons*, terrible as your only north star. They leak, they age,
they do not include your users.

For *your* app: 30–100 real prompts, expected properties, rerun on
every change. That private set is worth more than a public leaderboard.

## Hallucination

The model samples a fluent continuation. If the data (or RAG context)
does not support it, that is a hallucination. Eval it as:

- grounded? (supported by retrieved text)
- abstained when it should?
- citation attached?

Not as "vibes worse this week."

## When we lab this

Alongside any fine-tune and every RAG build. A `evals/` folder with
a JSONL of cases is part of the course, not extra credit.
