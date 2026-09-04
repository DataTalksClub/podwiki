---
title: "Search Parameter Tuning — LLM Zoomcamp Module 4"
summary: "--- video_url: 'https://www.youtube.com/watch?v=rSBSS_kCYN0&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv' --- # Search Parameter Tuning"
related_course:
  - llmz-module-04
---

[LLM Zoomcamp](/course-wiki/llm-zoomcamp/) › [Module 4: Evaluation](/course-wiki/llmz-module-04/) › Search Parameter Tuning

## Notes

---
video_url: "https://www.youtube.com/watch?v=rSBSS_kCYN0&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv"
---
# Search Parameter Tuning

In the previous lesson, we defined Hit Rate, MRR, and the `evaluate`
function. Now we can use them to tune search parameters.

Instead of guessing which settings are better, we measure them on the
ground truth dataset.

So far we've boosted `question` to 3.0. The idea was that a query should
match the FAQ question. That kind of match should count for more than
matching the answer text. It sounds reasonable. But it's a guess, and now
we can check it against data instead of trusting it.

This is the main benefit of offline evaluation. We change one parameter,
run the same questions again, and see whether the metric moves. The
dataset stays fixed, so the comparison is fair.

## Trying different boosts

Start with a search function where the question boost is configurable:

```python
def search_boost(query, question_boost):
    boost_dict = {"question": question_boost, "section": 0.5}

    return index.search(
        query,
        num_results=5,
        boost_dict=boost_dict,
    )
```

Evaluate several boost values:

```python
for boost in [0.5, 1.0, 3.0, 5.0, 10.0]:
    result = evaluate(
        ground_truth,
        lambda query, boost=boost: search_boost(query, boost)
    )
    print(f"boost={boost}: {result}")
```

For the data we prepared on May 29, 2026, this gives:

```python
boost=0.5: {'hit_rate': 0.9113924050632911, 'mrr': 0.800548523206751}
boost=1.0: {'hit_rate': 0.9240506329113924, 'mrr': 0.8139240506329113}
boost=3.0: {'hit_rate': 0.8987341772151899, 'mrr': 0.7693248945147676}
boost=5.0: {'hit_rate': 0.8708860759493671, 'mrr': 0.7401265822784809}
boost=10.0: {'hit_rate': 0.8582278481012658, 'mrr': 0.7122362869198313}
```

Increasing the question boost makes the metrics worse, not better. The
best value here is `1.0`, no boost at all. That's already the opposite of
what the intuition predicted.

But this is only one parameter. We can also tune `answer` and `section`
together with `question`.

Define a search function with all three boosts:

```python
def search_boosts(query, question_boost, answer_boost, section_boost):
    boost_dict = {
        "question": question_boost,
        "section": section_boost,
        "answer": answer_boost,
    }

    return index.search(
        query,
        num_results=5,
        boost_dict=boost_dict,
    )
```

Now do a small grid search:

```python
results = []

for question_boost in [1.0, 2.0, 5.0]:
    for answer_boost in [1.0, 2.0, 4.0, 10.0]:
        for section_boost in [0.1, 0.2, 0.5]:
            print(
                f"Evaluating question_boost={question_boost},"
                f" answer_boost={answer_boost},"
                f" section_boost={section_boost}..."
            )
            result = evaluate(
                ground_truth,
                lambda query, question_boost=question_boost, answer_boost=answer_boost, section_boost=section_boost: search_boosts(
                    query,
                    question_boost,
                    answer_boost,
                    section_boost
                )
            )

            results.append({
                "question": question_boost,
                "answer": answer_boost,
                "section": section_boost,
                "hit_rate": result["hit_rate"],
                "mrr": result["mrr"],
            })
```

Sort by MRR:

```python
df_results = pd.DataFrame(results)
df_results.sort_values("mrr", ascending=False).head(10)
```

For the same data, the best rows are:

```text
question  answer  section  hit_rate  mrr
1.0       2.0     0.1      0.975     0.885
2.0       4.0     0.2      0.975     0.885
5.0       10.0    0.5      0.975     0.885
5.0       10.0    0.2      0.975     0.884
5.0       10.0    0.1      0.975     0.884
2.0       4.0     0.1      0.975     0.884
2.0       4.0     0.5      0.977     0.884
1.0       2.0     0.2      0.977     0.884
1.0       2.0

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
- [llmz-m05-built-in-judge](/course-wiki/llmz-m05-built-in-judge/)
- [llmz-m05-capturing-metrics](/course-wiki/llmz-m05-capturing-metrics/)
- [llmz-m05-monitoring](/course-wiki/llmz-m05-monitoring/)
- [llmz-m05-next-steps](/course-wiki/llmz-m05-next-steps/)
- [llmz-m05-user-feedback](/course-wiki/llmz-m05-user-feedback/)
- [llmz-m06-best-practices-for-rag](/course-wiki/llmz-m06-best-practices-for-rag/)
- [llmz-m06-document-reranking](/course-wiki/llmz-m06-document-reranking/)
- [llmz-m07-chunking-for-longer-texts](/course-wiki/llmz-m07-chunking-for-longer-texts/)
- [llmz-m07-content-processing-cases-and-steps](/course-wiki/llmz-m07-content-processing-cases-and-steps/)
- [llmz-m07-end-to-end-project-example](/course-wiki/llmz-m07-end-to-end-project-example/)
- [llmz-m07-evaluating-rag](/course-wiki/llmz-m07-evaluating-rag/)
- [llmz-m07-evaluating-retrieval](/course-wiki/llmz-m07-evaluating-retrieval/)
- [llmz-m07-monitoring-and-containerization](/course-wiki/llmz-m07-monitoring-and-containerization/)
- [llmz-m07-summary-and-closing-remarks](/course-wiki/llmz-m07-summary-and-closing-remarks/)

## Sources

- [Video](https://www.youtube.com/watch?v=rSBSS_kCYN0&list=PL3MmuxUbc_hLZFNgSad56pDBKK8KO0XIv)
- [Lesson file](https://github.com/llm-zoomcamp/blob/main/llm-zoomcamp/cohorts/2026/04-evaluation/06-search-tuning.md)
