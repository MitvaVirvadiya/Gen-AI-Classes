# LangGraph

## One-sentence truth

LangGraph models an agent as a **state machine**: a typed state dict,
nodes that update it, edges (including cycles), checkpointing, and
human-in-the-loop.

## Do this again

```
State = {messages, files, next_action}
nodes: retrieve, call_llm, call_tool, ask_human
edges: if tool_call → call_tool → call_llm
       if done → END
checkpointer: resume after crash / after a human said "ok"
```

This is the right abstraction for anything that is not a straight
pipeline.

---

## Why it exists

LangChain agents hid the loop. Real products need:

- retries and branching
- durable state
- "stop and ask a human"
- time-travel / replay for debugging

## When we lab this

Track 5. One graph: user question → maybe retrieve → maybe tool → answer.
We will draw the graph on paper first.
