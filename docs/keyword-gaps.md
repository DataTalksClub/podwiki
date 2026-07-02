# Keyword Gap Analysis

Source: `.tmp/ubersuggest_Current_Queries.csv` (1000 keywords). Coverage checked with the local Zerosearch index against podwiki `_wiki/` and the main site (articles, courses, books, tools, people, podcast). GAP = not covered by podwiki AND not owned by the main site.

How to act on this (see CONTENT_GUIDE.md):
- Only create a page if it is groundable in our podcast/book content (GAP_GROUNDED). We repurpose what guests and book authors said; we do not invent.
- Never duplicate a main-site article, course, or book landing page (MAIN/BRAND/BOOK_INTENT route to the main site).
- BOOK_INTENT (pdf/download) queries: link the intent to the main site's book page. On the wiki, fold a book author's podcast points into the relevant TOPIC hub instead of making a competing book page.
- BM25 has no stemming, so singular/plural variants cluster separately; prefer merging doorway pages over creating new ones.

## GAP_GROUNDED — Gaps to create: podcast/book-groundable, not main-owned: 7

## GAP_UNGROUNDED — Gaps with no podcast/book grounding — cannot create here: 278

## COVERED — Already covered by a podwiki wiki page: 67

## MAIN — Owned by the main website — do NOT duplicate here: 313

## BRAND — Branded/navigational — main site owns: 113

## BOOK_INTENT — Book download intent that maps to a book we summarize: 204

## NOISE — Download intent with no matching book — not wiki content: 18

### Book-intent opportunities (key-ideas pages, never PDFs)
  - build a large language model from scratch pdf  (vol 720) -> _books:20241017-build-large-language-model-from-scratch
  - ace the data science interview pdf  (vol 480) -> _books:20211115-ace-the-data-science-interview
  - machine learning system design interview pdf  (vol 480) -> _books:20210208-ml-design-patterns
  - designing machine learning systems pdf  (vol 320) -> _books:20220627-designing-machine-learning-systems
  - fundamentals of data engineering pdf  (vol 260) -> _books:20220815-fundamentals-of-data-engineering
  - build a large language model from scratch pdf github  (vol 170) -> _books:20241017-build-large-language-model-from-scratch
  - build llm from scratch pdf  (vol 110) -> _books:20241017-build-large-language-model-from-scratch
  - llm engineer's handbook pdf  (vol 110) -> _books:20241104-llm-engineer-s-handbook
  - build a large language model pdf  (vol 90) -> _books:20241017-build-large-language-model-from-scratch
  - grokking machine learning pdf  (vol 90) -> _books:20210809-grokking-machine-learning
  - llm engineer handbook pdf  (vol 90) -> _books:20241104-llm-engineer-s-handbook
  - llm engineers handbook pdf  (vol 90) -> _books:20241104-llm-engineer-s-handbook
  - natural language processing with transformers pdf  (vol 90) -> _books:20210419-transformers-for-natural-language-processing
  - designing data-intensive applications epub  (vol 70) -> _books:20210308-designing-data-intensive-applications
  - essential math for data science pdf  (vol 70) -> _books:20220829-essential-math-for-data-science
  - ace the data science interview pdf github  (vol 50) -> _books:20211115-ace-the-data-science-interview
  - build a large language model from scratch sebastian raschka pdf  (vol 50) -> _books:20241017-build-large-language-model-from-scratch
  - download ace the data science interview pdf free download  (vol 50) -> _books:20211115-ace-the-data-science-interview
  - practical mlops pdf  (vol 50) -> _books:20210830-practical-mlops
  - ace data science interview pdf  (vol 40) -> _books:20211115-ace-the-data-science-interview
  - ace the data science interview free pdf  (vol 40) -> _books:20211115-ace-the-data-science-interview
  - build a large language model from scratch pdf download  (vol 40) -> _books:20241017-build-large-language-model-from-scratch
  - fundamentals of data engineering pdf free download  (vol 40) -> _books:20220815-fundamentals-of-data-engineering
  - grokking deep learning pdf  (vol 40) -> _books:20210517-grokking-deep-reinforcement-learning
  - the kaggle book pdf  (vol 40) -> _books:20220919-kaggle-book
  - ace the data science interview book pdf  (vol 30) -> _books:20211115-ace-the-data-science-interview
  - build a large language model from scratch free pdf  (vol 30) -> _books:20241017-build-large-language-model-from-scratch
  - build a llm from scratch pdf  (vol 30) -> _books:20241017-build-large-language-model-from-scratch
  - designing machine learning systems pdf free download  (vol 30) -> _books:20220627-designing-machine-learning-systems
  - effective pandas pdf  (vol 30) -> _books:20220131-effective-pandas
  - fundamentals of data engineering joe reis pdf  (vol 30) -> _books:20220815-fundamentals-of-data-engineering
  - grokking machine learning pdf github  (vol 30) -> _books:20210809-grokking-machine-learning
  - interpretable machine learning with python pdf  (vol 30) -> _books:20210719-interpretable-machine-learning-with-python
  - llm engineers handbook pdf github  (vol 30) -> _books:20241104-llm-engineer-s-handbook
  - machine learning engineering with python pdf  (vol 30) -> _books:20220117-machine-learning-engineering-with-python
  - machine learning for algorithmic trading stefan jansen pdf  (vol 30) -> _books:20210222-ml-algotrading-2ed
  - machine learning system design interview pdf download  (vol 30) -> _books:20210208-ml-design-patterns
  - ace the data science interview pdf download free  (vol 20) -> _books:20211115-ace-the-data-science-interview
  - ace the data science interview pdf free download  (vol 20) -> _books:20211115-ace-the-data-science-interview
  - build a large language model from scratch pdf free  (vol 20) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model sebastian raschka pdf  (vol 20) -> _books:20241017-build-large-language-model-from-scratch
  - build an llm from scratch pdf  (vol 20) -> _books:20241017-build-large-language-model-from-scratch
  - build large language model from scratch pdf  (vol 20) -> _books:20241017-build-large-language-model-from-scratch
  - building a large language model from scratch pdf  (vol 20) -> _books:20241017-build-large-language-model-from-scratch
  - essential math for data science pdf free download  (vol 20) -> _books:20220829-essential-math-for-data-science
  - llm engineer's handbook pdf download  (vol 20) -> _books:20241104-llm-engineer-s-handbook
  - machine learning system design interview book pdf  (vol 20) -> _books:20210208-ml-design-patterns
  - mastering machine learning algorithms 2nd edition giuseppe bonaccorso pdf  (vol 20) -> _books:20210125-mastering-ml-algorithms-2ed
  - python feature engineering cookbook pdf  (vol 20) -> _books:20210920-python-feature-engineering-cookbook
  - snowflake the definitive guide pdf  (vol 20) -> _books:20230123-snowflake-definitive-guide
  - snowflake: the definitive guide pdf  (vol 20) -> _books:20230123-snowflake-definitive-guide
  - transformers for natural language processing 2nd edition pdf free download  (vol 20) -> _books:20210419-transformers-for-natural-language-processing
  - a visual introduction to deep learning pdf  (vol 10) -> _books:20220214-a-visual-introduction-to-deep-learning
  - ace the data science interview nick singh pdf free download  (vol 10) -> _books:20211115-ace-the-data-science-interview
  - ai and machine learning for coders pdf free download  (vol 10) -> _books:20210412-ai-and-machine-learning-for-coders
  - analytics engineering with sql and dbt pdf  (vol 10) -> _books:20231106-analytics-engineering-with-sql-and-dbt
  - andrew jones driving data quality with data contracts pdf  (vol 10) -> _books:20230807-driving-data-quality-with-data-contracts
  - andrew p mcmahon machine learning engineering with python pdf  (vol 10) -> _books:20220117-machine-learning-engineering-with-python
  - angelica lo duca comet for data science pdf  (vol 10) -> _books:20221107-comet-for-data-science
  - build a large language model from scratch book pdf  (vol 10) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model from scratch book pdf download  (vol 10) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model from scratch pdf github download  (vol 10) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model from scratch pdf github free  (vol 10) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model from scratch pdf reddit  (vol 10) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model pdf github  (vol 10) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model sebastian raschka pdf download  (vol 10) -> _books:20241017-build-large-language-model-from-scratch
  - build an llm from scratch book pdf  (vol 10) -> _books:20241017-build-large-language-model-from-scratch
  - build large language models from scratch pdf  (vol 10) -> _books:20241017-build-large-language-model-from-scratch
  - build llm from scratch book pdf  (vol 10) -> _books:20241017-build-large-language-model-from-scratch
  - building large language models from scratch pdf  (vol 10) -> _books:20241017-build-large-language-model-from-scratch
  - comet for data science angelica lo duca pdf  (vol 10) -> _books:20221107-comet-for-data-science
  - comet for data science angelica lo duca pdf free download  (vol 10) -> _books:20221107-comet-for-data-science
  - comet for data science epub  (vol 10) -> _books:20221107-comet-for-data-science
  - data analysis with python and pyspark pdf  (vol 10) -> _books:20211025-data-analysis-with-python-and-pyspark
  - data engineering fundamentals pdf  (vol 10) -> _books:20220815-fundamentals-of-data-engineering
  - data engineering with apache spark delta lake and lakehouse pdf  (vol 10) -> _books:20220314-data-engineering-with-apache-spark-delta-lake-and-lakehouse
  - data governance the definitive guide pdf  (vol 10) -> _books:20210524-data-governance-the-definitive-guide
  - data governance: the definitive guide pdf  (vol 10) -> _books:20210524-data-governance-the-definitive-guide
  - data governance: the definitive guide pdf github  (vol 10) -> _books:20210524-data-governance-the-definitive-guide
  - denis rothman transformers for natural language processing 2nd edition pdf  (vol 10) -> _books:20210419-transformers-for-natural-language-processing
  - designing machine learning systems by chip huyen pdf download  (vol 10) -> _books:20220627-designing-machine-learning-systems
  - designing machine learning systems chip huyen pdf free download  (vol 10) -> _books:20220627-designing-machine-learning-systems
  - download ace the data science interview pdf github  (vol 10) -> _books:20211115-ace-the-data-science-interview
  - driving data quality with data contracts andrew jones pdf  (vol 10) -> _books:20230807-driving-data-quality-with-data-contracts
  - driving data quality with data contracts pdf  (vol 10) -> _books:20230807-driving-data-quality-with-data-contracts
  - engineering mlops emmanuel raj pdf  (vol 10) -> _books:20210705-engineering-mlops
  - essential math for data science book pdf  (vol 10) -> _books:20220829-essential-math-for-data-science
  - essential math for data science thomas nield pdf  (vol 10) -> _books:20220829-essential-math-for-data-science
  - essential math for data science thomas nield pdf download  (vol 10) -> _books:20220829-essential-math-for-data-science
  - essential math for data science thomas nield pdf free download  (vol 10) -> _books:20220829-essential-math-for-data-science
  - fundamentals of data engineering book download  (vol 10) -> _books:20220815-fundamentals-of-data-engineering
  - fundamentals of data engineering epub  (vol 10) -> _books:20220815-fundamentals-of-data-engineering
  - fundamentals of data engineering joe reis pdf free download  (vol 10) -> _books:20220815-fundamentals-of-data-engineering
  - generative ai with python and tensorflow 2 pdf  (vol 10) -> _books:20211108-generative-ai-with-python-and-tensorflow-2
  - generative ai with python and tensorflow 2 pdf download  (vol 10) -> _books:20211108-generative-ai-with-python-and-tensorflow-2
  - generative ai with python and tensorflow 2 pdf download free  (vol 10) -> _books:20211108-generative-ai-with-python-and-tensorflow-2
  - generative ai with python and tensorflow 2 pdf free download  (vol 10) -> _books:20211108-generative-ai-with-python-and-tensorflow-2
  - generative ai with python and tensorflow 2 raghav bali pdf  (vol 10) -> _books:20211108-generative-ai-with-python-and-tensorflow-2
  - gpt-3 sandra kublik pdf  (vol 10) -> _books:20230306-gpt-3
  - grokking machine learning book pdf  (vol 10) -> _books:20210809-grokking-machine-learning
  - grokking machine learning by luis serrano pdf  (vol 10) -> _books:20210809-grokking-machine-learning
  - grokking machine learning luis serrano pdf  (vol 10) -> _books:20210809-grokking-machine-learning
  - grokking machine learning pdf download  (vol 10) -> _books:20210809-grokking-machine-learning
  - grokking machine learning pdf github free download  (vol 10) -> _books:20210809-grokking-machine-learning
  - hands on data analysis with pandas pdf  (vol 10) -> _books:20220718-hands-on-data-analysis-with-pandas
  - hands-on data analysis with pandas 2nd edition pdf  (vol 10) -> _books:20220718-hands-on-data-analysis-with-pandas
  - hands-on data analysis with pandas 2nd edition pdf free download  (vol 10) -> _books:20220718-hands-on-data-analysis-with-pandas
  - hands-on data analysis with pandas 2nd edition stefanie molin pdf  (vol 10) -> _books:20220718-hands-on-data-analysis-with-pandas
  - hands-on data analysis with pandas pdf  (vol 10) -> _books:20220718-hands-on-data-analysis-with-pandas
  - interpretable machine learning molnar pdf  (vol 10) -> _books:20220411-interpretable-machine-learning
  - interpretable machine learning with python pdf free download  (vol 10) -> _books:20210719-interpretable-machine-learning-with-python
  - interpretable machine learning with python serg masís pdf  (vol 10) -> _books:20210719-interpretable-machine-learning-with-python
  - konrad banachewicz the kaggle book pdf  (vol 10) -> _books:20220919-kaggle-book
  - llm engineer handbook pdf download  (vol 10) -> _books:20241104-llm-engineer-s-handbook
  - llm engineer's handbook download  (vol 10) -> _books:20241104-llm-engineer-s-handbook
  - llm engineer's handbook filetype pdf  (vol 10) -> _books:20241104-llm-engineer-s-handbook
  - llm engineer's handbook free download  (vol 10) -> _books:20241104-llm-engineer-s-handbook
  - llm engineer's handbook free pdf  (vol 10) -> _books:20241104-llm-engineer-s-handbook
  - llm engineer's handbook packt pdf  (vol 10) -> _books:20241104-llm-engineer-s-handbook
  - llm engineer's handbook pdf free  (vol 10) -> _books:20241104-llm-engineer-s-handbook
  - llm engineer's handbook pdf free download  (vol 10) -> _books:20241104-llm-engineer-s-handbook
  - llm engineering handbook pdf  (vol 10) -> _books:20241104-llm-engineer-s-handbook
  - llm engineers handbook pdf download  (vol 10) -> _books:20241104-llm-engineer-s-handbook
  - llm engineers handbook pdf free  (vol 10) -> _books:20241104-llm-engineer-s-handbook
  - machine learning engineering with mlflow pdf  (vol 10) -> _books:20220117-machine-learning-engineering-with-python
  - machine learning engineering with python andrew mcmahon pdf  (vol 10) -> _books:20220117-machine-learning-engineering-with-python
  - machine learning engineering with python andrew p mcmahon pdf  (vol 10) -> _books:20220117-machine-learning-engineering-with-python
  - machine learning for algorithmic trading by stefan jansen pdf  (vol 10) -> _books:20210222-ml-algotrading-2ed
  - machine learning for algorithmic trading stefan jansen pdf download  (vol 10) -> _books:20210222-ml-algotrading-2ed
  - machine learning for algorithmic trading stefan jansen pdf free download  (vol 10) -> _books:20210222-ml-algotrading-2ed
  - machine learning system design interview download  (vol 10) -> _books:20210208-ml-design-patterns
  - machine learning system design interview epub  (vol 10) -> _books:20210208-ml-design-patterns
  - machine learning system design valerii babushkin pdf  (vol 10) -> _books:20210208-ml-design-patterns
  - machine learning using tensorflow cookbook konrad banachewicz pdf  (vol 10) -> _books:20210503-machine-learning-using-tensorflow-cookbook
  - machine learning using tensorflow cookbook pdf  (vol 10) -> _books:20210503-machine-learning-using-tensorflow-cookbook
  - managing machine learning projects pdf  (vol 10) -> _books:20221010-managing-machine-learning-projects
  - mastering machine learning algorithms pdf  (vol 10) -> _books:20210125-mastering-ml-algorithms-2ed
  - o'reilly essential math for data science pdf  (vol 10) -> _books:20220829-essential-math-for-data-science
  - practical mlops book pdf  (vol 10) -> _books:20210830-practical-mlops
  - practical mlops by noah gift and alfredo deza pdf  (vol 10) -> _books:20210830-practical-mlops
  - practical mlops noah gift pdf  (vol 10) -> _books:20210830-practical-mlops
  - practical mlops o'reilly pdf  (vol 10) -> _books:20210830-practical-mlops
  - production ready data science pdf  (vol 10) -> _books:20250728-production-ready-data-science
  - python feature engineering cookbook soledad galli pdf  (vol 10) -> _books:20210920-python-feature-engineering-cookbook
  - sandra kublik gpt-3 pdf  (vol 10) -> _books:20230306-gpt-3
  - sebastian raschka llm from scratch pdf  (vol 10) -> _books:20241017-build-large-language-model-from-scratch
  - snowflake definitive guide pdf  (vol 10) -> _books:20230123-snowflake-definitive-guide
  - snowflake: the definitive guide pdf free download  (vol 10) -> _books:20230123-snowflake-definitive-guide
  - snowflake: the definitive guide pdf github  (vol 10) -> _books:20230123-snowflake-definitive-guide
  - software mistakes and tradeoffs pdf  (vol 10) -> _books:20210906-software-mistakes-and-tradeoffs
  - stefan jansen machine learning for algorithmic trading pdf  (vol 10) -> _books:20210222-ml-algotrading-2ed
  - the coding career handbook pdf  (vol 10) -> _books:20210510-the-coding-career-handbook
  - the kaggle book konrad banachewicz pdf free download  (vol 10) -> _books:20220919-kaggle-book
  - the kaggle book pdf github  (vol 10) -> _books:20220919-kaggle-book
  - the practitioner's guide to graph data pdf  (vol 10) -> _books:20210405-the-practitioners-guide-to-graph-data
  - tiny python projects pdf  (vol 10) -> _books:20210426-tiny-python-projects
  - tiny python projects pdf free download  (vol 10) -> _books:20210426-tiny-python-projects
  - transformers for natural language processing pdf free download  (vol 10) -> _books:20210419-transformers-for-natural-language-processing
  - understanding etl pdf  (vol 10) -> _books:20240415-understanding-etl
  - "transformers for natural language processing 2nd edition denis rothman pdf  (vol 10) -> _books:20210419-transformers-for-natural-language-processing
  - build a large language model (from scratch pdf  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch pdf github)  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch pdf)  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch sebastian raschka pdf github)  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) .pdf  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) book pdf  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) by sebastian raschka pdf  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) download  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) epub  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) free download  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) free pdf  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) pdf  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) pdf download  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) pdf drive  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) pdf free  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) pdf free download  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) pdf free download github  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) pdf github  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) pdf reddit  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) sebastian raschka pdf  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch) sebastian raschka pdf download  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model (from scratch)pdf  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - build a large language model from scratch pdf free download github  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - data-centric machine learning with python epub  (vol 0) -> _books:20240408-data-centric-machine-learning-with-python
  - data-centric machine learning with python manmohan gosada pdf  (vol 0) -> _books:20240408-data-centric-machine-learning-with-python
  - data-centric machine learning with python manmohan gosada pdf free download  (vol 0) -> _books:20240408-data-centric-machine-learning-with-python
  - fundamentals of data engineering by joe reis pdf  (vol 0) -> _books:20220815-fundamentals-of-data-engineering
  - fundamentals of data engineering epub download  (vol 0) -> _books:20220815-fundamentals-of-data-engineering
  - fundamentals of data engineering: plan and build robust data systems pdf  (vol 0) -> _books:20220815-fundamentals-of-data-engineering
  - gpt-3 sandra kublik pdf free download  (vol 0) -> _books:20230306-gpt-3
  - interpretable machine learning (third edition) pdf  (vol 0) -> _books:20220411-interpretable-machine-learning
  - interpretable machine learning with python serg mass pdf  (vol 0) -> _books:20210719-interpretable-machine-learning-with-python
  - interpretable machine learning with python serg mass pdf free download  (vol 0) -> _books:20210719-interpretable-machine-learning-with-python
  - llm engineer’s handbook mr. paul iusztin pdf  (vol 0) -> _books:20241104-llm-engineer-s-handbook
  - llm engineer’s handbook mr. paul iusztin pdf free download  (vol 0) -> _books:20241104-llm-engineer-s-handbook
  - llm engineer’s handbook pdf  (vol 0) -> _books:20241104-llm-engineer-s-handbook
  - llm engineer’s handbook pdf free download  (vol 0) -> _books:20241104-llm-engineer-s-handbook
  - mr. paul iusztin llm engineer’s handbook pdf  (vol 0) -> _books:20241104-llm-engineer-s-handbook
  - natural language processing with transformers free pdf  (vol 0) -> _books:20210419-transformers-for-natural-language-processing
  - serg mass interpretable machine learning with python pdf  (vol 0) -> _books:20210719-interpretable-machine-learning-with-python
  - the llm engineering handbook by paul iusztin and maxime labonne pdf  (vol 0) -> _books:20241104-llm-engineer-s-handbook
  - understanding etl data pipelines for modern data architectures pdf  (vol 0) -> _books:20240415-understanding-etl
  - "build a large language model from scratch book by sebastian raschka pdf  (vol 0) -> _books:20241017-build-large-language-model-from-scratch
  - & wall street pdf"  (vol 0) -> _books:20210322-street-coder

## GAP clusters (min volume 20) — 5 keywords

### data  (3 keywords, total vol 8170)
  - data intensive applications  (vol 8100, SEO diff 37, ground: _books:20210308-designing-data-intensive-applications~10.1)
  - data science expert  (vol 50, SEO diff 35, ground: _podcast:data-science-manager-vs-expert-hiring-guide~11.7)
  - data scientist to data engineer  (vol 20, SEO diff 11, ground: _podcast:big-data-engineer-vs-data-scientist~10.9)

### bootcamp  (1 keywords, total vol 30)
  - analytics engineering bootcamp  (vol 30, SEO diff 37, ground: _podcast:get-data-analytics-and-data-engineering-job~10.3)

### software  (1 keywords, total vol 20)
  - ml software development  (vol 20, SEO diff 13, ground: _books:20251006-software-development-at-rocket-speed~11.3)

