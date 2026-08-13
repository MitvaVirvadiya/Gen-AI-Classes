# LlamaIndex

## One-sentence truth

LlamaIndex is data-first: ingest messy documents, build indexes
(vector, keyword, knowledge graph), and query them. Stronger than
LangChain when the pain is *data*, not *orchestration*.

## Do this again

```
documents = SimpleDirectoryReader("notes/").load_data()
index = VectorStoreIndex.from_documents(documents)
engine = index.as_query_engine()
engine.query("What is BPE?")
```

Under the hood: chunk, embed, retrieve, prompt — Lesson 4.2.

---

## Vocabulary

- **Node** — a chunk with metadata
- **Index** — a way to retrieve nodes
- **Query engine** — retrieve + synthesize
- **Retriever** — just the retrieve half (compose your own generate)

## Use it when

- lots of PDFs, HTML, mixed corpora
- you want index types beyond "one big vector store"

## Use LangGraph / raw code when

- the control flow is the product (agents, approvals, multi-step tools)

They are not enemies. LlamaIndex for retrieval, your own loop or
LangGraph for the agent.
