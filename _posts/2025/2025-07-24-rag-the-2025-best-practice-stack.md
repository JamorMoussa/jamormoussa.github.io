---
author: owner
title: "RAG: The 2025 Best-Practice Stack"
date: 2025-07-24
categories: [GenAI, "RAG"]
tags: []
description: A summary of the most effective RAG architecture and tooling in 2025, based on the latest best practices.
image:
  path: "assets/posts/rag-stack.png"
---

[▶️ Watch the talk on YouTube](https://www.youtube.com/watch?v=vf9emNxXWdA)

## Overview

This talk presents the 2025 best-practice stack for building RAG (Retrieval-Augmented Generation) applications using open-source tools. Key takeaways include:

- Core components: **Orchestration**, **Vector Databases**, **Enhanced Retrieval**, **Evaluation**
- Practical tips on chunking, retrieval, and data strategies
- A reference stack for scalable and accurate RAG pipelines


## What is RAG?

**RAG = Dense Vector Retrieval + In-Context Learning**

It augments language models with external knowledge by retrieving relevant context from your data. The typical flow:

1. **Retrieve**: Search your documents for relevant content
2. **Augment**: Add retrieved context to your prompt
3. **Generate**: Produce more accurate, grounded responses

![](assets/posts/rag-arch.png)
_**Figure: Basic RAG Architecture – Embeddings + In-Context Learning**_


## Key Insights from the Talk

1. Orchestration Framework
- **LangChain**: More flexible, better suited for complex workflows
- **LlamaIndex**: Simpler, often easier to start with

2. Vector Database
- **Qdrant**: High performance, scales well from small to millions of documents

3. Embedding Models
- Depends on your use case: language coverage, speed, and accuracy matter

4. Evaluation Framework
- **RAGAS**: Open-source tool for evaluating RAG pipelines

5. Reranking
- **Cohere Rerank** delivers best-in-class results for reordering retrieved chunks

6. Model Serving
- **Together AI**: Supports most popular open models with good latency/performance

7. Monitoring & Observability
- **LangSmith**: Powerful tool for LangChain-based pipelines (note: not open-source)


## Context Quality is Everything

The effectiveness of RAG depends on what we put **in context**:

- **Chunking**: Controls what gets retrieved
- **Metadata**: Helps rank or filter retrieved chunks
- **Retrieval Strategy**: Directly impacts generation quality

Example: If chunks come from books, metadata could include the title or author to improve context relevance.

> "As the retrieval goes, the generation goes."


## Final Tips

To improve RAG systems:

- Tune **chunk size**, **embedding model**, and **ranking**
- Leverage **metadata** to enhance relevance
- Optimize both **retrieval** and **in-context input**

