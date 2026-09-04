---
title: "Chunking for Longer Texts — LLM Zoomcamp Module 7"
summary: "<a href="https://www.youtube.com/watch?v=tyBRP_WewXA&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">"
related_course:
  - llmz-module-07
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 7: End-to-End Project](/course-wiki/llmz-module-07/) › Chunking for Longer Texts

## Notes

# Chunking for Longer Texts

<a href="https://www.youtube.com/watch?v=tyBRP_WewXA&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R">
  
</a>

Our FAQ data is well-structured: each document is a question-answer
pair. But what if your data is articles, transcripts, or slide
decks? You need to chunk it into pieces that are the right size
for embedding and retrieval.

## Multiple articles

If you have multiple articles (blog posts, wiki pages, etc.

):

1. Assign each article a document ID
2. Split each article into chunks
3. Give each chunk a unique chunk ID (e.g., `doc_id_1`, `doc_id_2`)
4. Evaluate retrieval with separate Hit Rate for both document ID
   and chunk ID
5. Tune chunk size using RAG evaluation metrics

```json
{
  "doc_id": "abc123",
  "chunk_id": "abc123_1",
  "text": "first paragraph of the article..."
}
```

## Single article or transcript

If you have one long piece of content (a YouTube transcript, a
PDF, etc.

):

1. Split it into chunks
2. Evaluate the same way as multiple articles
3. You can use `youtube-transcript-api` to get transcripts
   programmatically

## Book or very long content

For books and other long-form content, apply this strategy:

1. Treat each chapter or section as a separate document
2. Experiment with different chunking strategies
3. Use LLM-as-a-Judge to compare approaches

## Images and slides

Visual content can be processed as follows:

1. Describe images using an LLM like GPT-4o-mini
2. Each image is a separate document
3. For slide decks: deck = document, slide = chunk
4. You can also use CLIP embeddings for direct image search

## Smart chunking with LLMs

Instead of splitting by character count or paragraph breaks, you
can use an LLM to find logical boundaries:

1. Give the LLM the full text and ask it to split into logical
   blocks
2. Then ask it to name each block
3. Each block becomes a chunk you can index and search

This approach, sometimes called "semantic chunking" or "logical
chunking," often produces better chunks than fixed-size splitting
because the chunks map to meaningful topics.

You can see a detailed summary of content processing approaches
in [content-processing-summary.md](content-processing-summary.md).

## Key concepts

- [Trading Strategy](/course-wiki/trading-strategy/)
- [LLM Evaluation](/course-wiki/llm-evaluation/)

## Related notes

- [llmz-m01-building-the-prompt](/course-wiki/llmz-m01-building-the-prompt/)
- [llmz-m02-embeddings](/course-wiki/llmz-m02-embeddings/)
- [llmz-m02-next-steps](/course-wiki/llmz-m02-next-steps/)
- [llmz-m04-agent-evaluation](/course-wiki/llmz-m04-agent-evaluation/)
- [llmz-m04-evaluation](/course-wiki/llmz-m04-evaluation/)
- [llmz-m04-generating-ground-truth-data](/course-wiki/llmz-m04-generating-ground-truth-data/)
- [llmz-m04-generating-ground-truth-for-all-documents](/course-wiki/llmz-m04-generating-ground-truth-for-all-documents/)
- [llmz-m04-generating-rag-answers](/course-wiki/llmz-m04-generating-rag-answers/)
- [llmz-m04-llm-as-a-judge](/course-wiki/llmz-m04-llm-as-a-judge/)
- [llmz-m04-next-steps](/course-wiki/llmz-m04-next-steps/)
- [llmz-m04-rag-and-agent-evaluation](/course-wiki/llmz-m04-rag-and-agent-evaluation/)
- [llmz-m04-search-evaluation](/course-wiki/llmz-m04-search-evaluation/)
- [llmz-m04-search-evaluation-metrics](/course-wiki/llmz-m04-search-evaluation-metrics/)
- [llmz-m04-search-parameter-tuning](/course-wiki/llmz-m04-search-parameter-tuning/)
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-document-reranking](/course-wiki/llmz-m06-document-reranking/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-interface-and-ingestion-pipeline](/course-wiki/llmz-m07-interface-and-ingestion-pipeline/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=tyBRP_WewXA&list=PL3MmuxUbc_hIB4fSqLy_0AfTjVLpgjV3R)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/07-project-example/07-chunking.md)
