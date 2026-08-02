---
layout: wiki
title: "Bioinformatics Data Science"
summary: "Bioinformatics data science connects lab data with sequencing analysis, network modeling, ML workflows, and open-source tools."
related:
  - Data Science
  - Machine Learning
  - Open Source
  - Reproducibility
  - Graph Data Science
  - Data Pipelines
---

Bioinformatics data science is [[data science]]
applied to biological data. Lab work produces samples, sequencing output, and
biological questions. Bioinformatics turns them into data structures, models,
reports, and reusable tools.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

Bioinformatics data-science work includes sequencing data and metagenomic
abundance tables. It also includes microbial association networks, knowledge
graphs, and reproducible scientific tooling. That work connects bioinformatics
to [[machine learning]] and [[open source]]. It also depends on
[[reproducibility]], [[graph data science]], and [[data pipelines]].
[[cite:learning-machine-learning-self-taught-bioinformatics=>Self-Taught Bioinformatics]]
[[cite:from-biology-to-machine-learning-data-science-portfolio-open-source-computer-vision-transformers=>From Biology to ML]]

A useful non-biological comparison is
[[astroinformatics-scientific-data-pipelines=>astroinformatics scientific data pipelines]]:
both fields keep instrument or experiment context attached to features before a
model or analysis claim. That context is part of what makes the claim credible.
[[cite:from-radio-astronomy-to-machine-learning-and-data-engineering@15:30=>From Radio Astronomy to Applied ML]]

## Bioinformatics Data Science in Practice

Bioinformatics takes biological information generated in experiments and uses
exploration, analysis, software, and modeling to interpret it. Computational
analysis can reduce the number of lab experiments by proposing better candidates
to test, but it doesn't replace wet-lab validation.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

That makes bioinformatics data science close to ordinary
[[data science]], but the biological context changes the meaning of each
feature. DNA segments, abundance counts, and protein structures are examples.
Biomarkers and microbial associations are also features that need biological
context. Each feature has to stay tied to the experiment that produced it and
the biological question it supports.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]
[[cite:from-biology-to-machine-learning-data-science-portfolio-open-source-computer-vision-transformers=>From Biology to ML]]

## Different Routes Into the Work

Bioinformatics data science has different entry points, not one fixed career
sequence. One route starts from biotechnology and wet-lab context, then adds
software and package ecosystems. It also adds graph analysis and reporting tools
for biological data.
Another route starts from independent study, papers, datasets, and project-first
[[machine learning]] practice. A third route starts from biology and statistics,
then moves into ML engineering and healthcare prediction.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]
[[cite:learning-machine-learning-self-taught-bioinformatics=>Self-Taught Bioinformatics]]
[[cite:from-biology-to-machine-learning-data-science-portfolio-open-source-computer-vision-transformers=>From Biology to ML]]

The boundary differs by project. Some bioinformatics work is closer to
scientific computing and [[data pipelines]]. Some is closer to ML portfolio
work. Some becomes
[[healthcare-ml-validation-and-adoption=>healthcare ML validation and adoption]]
when the target is a clinical outcome.

Isabella Bicalho's INRIA work used biomarkers from a blood draw to predict
lung-cancer patient response to immunotherapy. That puts biology-to-ML work
beside clinical validation rather than generic tabular prediction.
[[cite:from-biology-to-machine-learning-data-science-portfolio-open-source-computer-vision-transformers@11:14=>From Biology to ML]]

## Wet Lab and Dry Lab Boundaries

The wet-lab and dry-lab boundary starts with where the data comes from. Wet-lab
work means physical experiments with samples, instruments, and test tubes. Dry
lab work is computational. The scientist or engineer works with data, pipelines,
simulations, and software.

Lab teams test vaccines, compounds, or biological
mechanisms. Computational analysis helps narrow what the lab should test next.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

That boundary shapes career paths. A self-taught path can combine the OSSU open
curriculum, ML Zoomcamp, PubMed and Google Scholar dataset discovery, and
project-first learning. The frog-toxicity project in the self-learning episode
shows how a biological question can become an ML workflow with notebooks,
Docker, deployment practice, and model evaluation.
[[cite:learning-machine-learning-self-taught-bioinformatics=>Self-Taught Bioinformatics]]

A biology-first path can move through statistics, bioinformatics, and then ML
engineering. The biology-to-ML episode connects that path to
[[career transitions in data]] and to clinical prediction work, where the useful
skill isn't only model training. The harder translation is from biology to
features, outcomes, validation questions, and a decision that a lab or medical
team can look at.
For researchers making the same translation outside a biological title,
[[academic-researcher-to-data-science=>Researcher to Data Science]] is the
adjacent career path.
[[cite:from-biology-to-machine-learning-data-science-portfolio-open-source-computer-vision-transformers=>From Biology to ML]]

## From Sequencing to Analysis

Sequencing is the input side of many bioinformatics workflows. Genomic data is
represented as DNA sequences made from adenine, guanine, cytosine, and thymine.
A sequencing workflow reads DNA from an environmental or biological sample and
breaks it into small pieces. It then decodes the nucleotide order, assembles the
pieces, and compares the result with databases or a reference genome.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

That turns a physical sample into analyzable data. The downstream work can look
like familiar data science because it includes exploration, matching, and
feature interpretation. It also includes modeling and comparison against known
references.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

The biological stakes change the meaning of the features. A DNA segment may be
tied to genes, proteins, or population markers. It may also be tied to health
traits or organisms observed in a mixed sample. The analysis has to preserve the
connection between the computational result and the underlying biology.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

## Metagenomics and Abundance Tables

Metagenomics is the clearest pipeline example because it turns raw biological
material into analytical tables. The workflow studies DNA from environmental
samples rather than from one organism. A lake, soil sample, or wastewater
treatment plant can contain many microorganisms. The analysis has to decode
mixed DNA and reconstruct the genomes or organism signals inside it.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

In the wastewater treatment microbiome project, the working data takes the form
of abundance tables. Rows represent microorganisms, columns represent samples,
and values count how often each organism appears. Those tables make the work
recognizable to a data scientist. The project combines datasets from multiple
studies, categorizes them by biome, and analyzes patterns across samples.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

## Microbiome Network Inference

The microbiome project moves from tabular analysis into
[[graph data science]]. Microbial association networks are inferred from
co-abundance patterns. If two microorganisms often appear together in similar
abundance, the workflow creates a possible association between them.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

CC Lasso is the method used in that project to infer potential microorganism
interactions. The output includes correlation values between microorganism
pairs, thresholding, and positive or negative associations. A positive
association can suggest coexistence, while a negative association can suggest
that one organism appears when another doesn't. Geography, sampling, and
biological context still affect the interpretation.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

The inferred network can then become a knowledge graph. MCW2 Graph is an
open-source knowledge graph where microorganisms are nodes and inferred
co-abundance patterns are edges. Extra metadata describes metabolites, biomes,
and biological processes. Readers can explore the data in a Streamlit app or
download raw CSV files. They can also open the graph in Neo4j and run graph
algorithms such as clustering or centrality analysis.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

## Open-Source Computational Biology Tools

The tooling discussion shows why [[open source]]
is part of the bioinformatics data science workflow rather than an add-on. MCW2
Graph and VueGen are the main examples. VueCore and Viewer also appear as tools
for exploring, reporting, and visualizing biological data.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

VueGen is the reporting example. It's a Python package that reads a structured
directory containing tables, plots, network data, or HTML files. It then
generates static documents, presentations, and Streamlit apps.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

Under the hood, the tool uses Quarto and Streamlit rather than LLM
interpretation. That matters for
[[reproducibility]] because the
report is generated from explicit files, paths, and descriptions. It also uses
YAML metadata and renderable project structure.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

The package ecosystem affects what bioinformatics data scientists build with.
Bioconda and Bioconductor are biology-oriented package ecosystems. R still has a
larger bioinformatics community, while more work is moving to Python. Some
scientific packages are created by scientists who aren't trained software
developers. Scaling or adapting them can require reading source code, extending
the package, or contacting maintainers.
[[cite:bioinformatics-worflows-tools-and-data-science=>Bioinformatics Workflows]]

## Learning and Portfolio Work

Bioinformatics learning is project-driven in the self-taught episode. The path
starts with enough programming, statistics, and ML to work through real
datasets. It then uses research papers, PubMed, Google Scholar, and citation
trails to choose projects. A useful portfolio project connects a biological
question to data preparation, model training, evaluation, and deployment
practice.
[[cite:learning-machine-learning-self-taught-bioinformatics=>Self-Taught Bioinformatics]]

Open-source work can also turn domain knowledge into visible ML experience. The
biology-to-ML episode links biology and bioinformatics with computer vision,
transformers, documentation, and community contribution. That path matters for
bioinformatics data science because many useful projects sit between science,
software, and communication rather than inside a single discipline.
[[cite:from-biology-to-machine-learning-data-science-portfolio-open-source-computer-vision-transformers=>From Biology to ML]]

## Related Pages

Neighboring pages cover the general data, ML, open-source, and graph concepts
that recur in bioinformatics data-science work.

- [[Data Science]] for analysis and
  modeling in a broader setting.
- [[Machine Learning]] for
  prediction, evaluation, and model-driven workflows.
- [[Open Source]] for public tools,
  package ecosystems, documentation, and contribution work.
- [[Reproducibility]] for rerunnable
  analysis, reports, environments, and metadata.
- [[Graph Data Science]] for microbial
  networks, graph algorithms, and knowledge-graph enrichment.
- [[Data Pipelines]] for movement,
  transformation, publication, and rerun patterns behind biological analysis.
- [[astroinformatics-scientific-data-pipelines=>Astroinformatics Scientific Data Pipelines]]
  for astronomy data pipelines where source matching also depends on scientific
  measurement context.
