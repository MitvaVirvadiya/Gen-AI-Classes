# What an agent actually is

## One-sentence truth

An agent is not a clever system prompt. It is a loop: model proposes an
action → your code executes it → result goes back into the context →
repeat until a stop condition.

## Do this again

```
state = {messages: [user]}
while not done and steps < max:
    out = llm(state.messages, tools)
    if out.tool_calls:
        for call in out.tool_calls:
            result = run(call)
            state.messages.append(tool_result)
    else:
        return out.text
```

ReAct is this loop with a visible "thought" (optional). The thought is
not the agent. The loop is.

---

## Agent vs chatbot vs RAG

| | Tools | Loop | External data |
|---|---|---|---|
| Chatbot | no | no | only weights |
| RAG | maybe retrieve once | no | yes |
| Agent | yes | yes | yes, via tools |

## Why agents fail

- no max-step / no timeout (infinite tool use)
- tools that can do too much (unbounded shell)
- context bloat (every observation stuffed back)
- no eval (you cannot tell if the loop helped)

## When we lab this

A 40-line loop with two tools (`calculator`, `search_notes`) before we
touch LangGraph.
