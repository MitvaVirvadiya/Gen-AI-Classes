# MCP — Model Context Protocol

## One-sentence truth

MCP is a standard (JSON-RPC over stdio or HTTP) so a **host** (Cursor,
Claude Desktop, your agent) can talk to a **server** that exposes
tools, resources, and prompts — without writing a custom plugin per app.

## Do this again

```
Host (Grok / Cursor / your Python agent)
   │  MCP client
   │  initialize → list_tools → call_tool
   ▼
Server (you write this)
   tools:     functions with JSON schemas     (Lesson 5.2)
   resources: readable URIs (files, tickets)
   prompts:   reusable prompt templates
```

If you can write a function-calling tool, you can write an MCP server.
The protocol is the wrapper.

---

## Why it exists

Before MCP: every chat app reinvented "how do I give the model GitHub?"
After MCP: GitHub (or you) ships one server; any MCP client can use it.

## What we will build

A tiny server that exposes **this course repo** as:

- tool `search_notes(query)` — grep GLOSSARY / SEARCH-INDEX
- tool `read_lesson(path)`
- resource `curriculum://progress`

Then we connect it to a host and ask: "what should I study today?"

## Security

An MCP server is code the model can invoke. Same rules as tools:
least privilege, no unbounded shell, no secret leakage in resource URIs.

## Not MCP

- not a model
- not an agent by itself
- not a replacement for RAG or fine-tuning
