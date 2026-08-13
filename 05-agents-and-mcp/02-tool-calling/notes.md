# Tool calling / function calling

## One-sentence truth

The model does not run your function. It emits a structured call
(name + JSON args). You run it, and you send the result back as the
next message.

## Do this again

```python
tools = [{
  "type": "function",
  "function": {
    "name": "get_weather",
    "description": "Current weather for a city",
    "parameters": {
      "type": "object",
      "properties": {"city": {"type": "string"}},
      "required": ["city"],
    },
  },
}]

resp = client.chat.completions.create(model=..., messages=..., tools=tools)
# if resp.choices[0].message.tool_calls: execute, append, call again
```

The schema *is* the prompt. Bad descriptions → bad calls.

---

## Design rules

- one tool, one job
- arguments: few, typed, no essays
- make failures return a string the model can read, not an exception
  that kills the process
- never expose a tool you would not let a stranger call

## This is the same idea as MCP

MCP is "tools + resources + prompts, over a standard protocol."
Learn function calling first. MCP is the socket.
