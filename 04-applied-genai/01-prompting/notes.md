# Prompting that is not folklore

## One-sentence truth

A prompt is the entire token prefix the model conditions on: system
rules, chat history, retrieved docs, tool schemas, and the user text.
"Prompt engineering" is designing that prefix on purpose.

## Do this again

```
[system]     who you are, tools you have, output contract
[retrieved]  only if RAG. labeled. "use or say you don't know"
[examples]   1–3 input/output pairs if the task is picky
[user]       the actual ask
[assistant]  (empty — generation starts here)
```

Always go through `apply_chat_template`. Hand-concatenating roles is
how models "get dumber."

---

## Techniques that actually exist

| Name | What it is |
|---|---|
| Few-shot | show the format, do not write an essay of rules |
| CoT | "think step by step" or a hidden scratchpad |
| Output contract | JSON schema / tool call, not "please return JSON" |
| Separation | delimit retrieved text so it is not instructions |

## What is folklore

- magical phrases that "unlock" the model
- 2,000-word system prompts nobody evals
- temperature as a substitute for a better prompt or better data

## Eval

Change one thing, run the 30-case set (Lesson 2.4). Prompting without
eval is journaling.
