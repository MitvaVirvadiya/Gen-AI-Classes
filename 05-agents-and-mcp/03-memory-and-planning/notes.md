# Memory, planning, loops

## One-sentence truth

The context window *is* working memory. Everything else (summaries,
vector recall, files) is a tool that writes back into that window.

## Do this again

| Kind | Mechanism | Use |
|---|---|---|
| Short-term | the message list | current task |
| Summary | LLM compresses old turns | long chats |
| Episodic | vector store of past Q&A | "we did this last week" |
| Scratchpad | a notes tool the agent writes to | multi-step plans |

Do not start with a "memory framework." Start with: what should be in
the next prompt?

---

## Planning

- **No planner:** ReAct, one step at a time. Usually enough.
- **Plan-then-act:** write a checklist, then execute. Better for
  known multi-step jobs
- **Reflection:** after a tool error, ask "what went wrong" before retry

Max steps + a budget (tokens, dollars, seconds) are part of the plan,
not extras.
