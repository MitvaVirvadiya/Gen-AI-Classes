# When to use which

## One-sentence truth

Default: raw OpenAI-compatible API + your own 80-line RAG. Add a
library when it deletes code you would hate to maintain.

## Cheat sheet

| Job | Reach for |
|---|---|
| Learn / debug | vanilla Python (this course) |
| Chat completion | OpenAI-compatible client (Ollama, vLLM, Groq, ...) |
| Lots of document formats + indexes | LlamaIndex |
| Lots of vendor integrations, linear chains | LangChain |
| Loops, tools, humans, persistence | LangGraph |
| Standard tool interface across apps | MCP (Track 5) |
| Change the model's *behavior permanently* | SFT / LoRA, not a longer prompt |
| Facts that change daily | RAG, not SFT |

## Anti-patterns

- installing LangChain to call one API
- fine-tuning to add knowledge that belongs in a database
- agents for a question a retrieve+generate would answer
- three frameworks in one repo "in case"

## The course rule

We implement each idea naked first. Frameworks are optional clothes.
