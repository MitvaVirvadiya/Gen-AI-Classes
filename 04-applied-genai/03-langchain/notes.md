# LangChain

## One-sentence truth

LangChain is a large toolbox of integrations (LLMs, vector DBs, loaders)
and a way to compose them. It is not required to build RAG or agents.

## Do this again (mental model)

```
Document loaders → splitters → vectorstore
ChatModel + prompt template + output parser
Tools → Agent  (prefer LangGraph for anything with a loop)
```

LCEL (`prompt | model | parser`) is the modern composition style.

---

## Use it when

- you want a connector you do not want to write (20 vector DBs, etc.)
- you are prototyping and will throw the code away

## Do not use it when

- you cannot explain the equivalent 80-line vanilla version
- you need to debug a silent prompt mutation
- the graph has cycles, retries, human approval → that is LangGraph

## How we will learn it

After vanilla RAG. We re-implement the same notebook in LangChain and
list what we gained vs what we can no longer see.
