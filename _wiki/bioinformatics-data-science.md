---
layout: wiki
title: "Bioinformatics Data Science"
summary: "Bioinformatics data science applies exploration, modeling, network analysis, and open-source software workflows to biological data from sequencing, metagenomics, and multi-omics experiments."
related:
  - Data Science
  - Machine Learning
  - Open Source
  - Reproducibility
  - Data Pipelines
---

Bioinformatics data science is [[data science]]
applied to biological data. In
[[podcast:bioinformatics-worflows-tools-and-data-science|Bioinformatics Workflows in Practice]],
[[person:sebastianayalaruano|Sebastian Ayala Ruano]]
defines the work as taking information generated in the lab. Bioinformatics
then uses exploration, analysis, and modeling to interpret results and make
predictions around biological systems.

The episode frames bioinformatics as a bridge between experimental biology and
computational work. It covers sequencing-to-analysis workflows, metagenomic
samples, and abundance tables. It also covers microbial association networks,
knowledge graphs, and scientific reporting. Visualization and open-source
package ecosystems make those workflows usable beyond one lab.

## Wet Lab and Dry Lab Boundaries

The boundary starts with where the data comes from. At 6:27 in
[[podcast:bioinformatics-worflows-tools-and-data-science|Bioinformatics Workflows in Practice]],
[[person:sebastianayalaruano|Sebastian Ayala Ruano]]
contrasts biotechnology experiments with bioinformatics analysis. Lab teams test
vaccines, compounds, or biological mechanisms. Computational analysis can reduce
the number of experiments by proposing better candidates for the lab to try.

At 8:23, the same episode distinguishes wet lab and dry lab work directly. Wet
lab work means physical experiments with samples, instruments, and test tubes.
Dry lab work is computational. The scientist or engineer works with data,
pipelines, simulations, and software.

Bioinformatics data science sits near
[[machine learning]] and
[[data pipelines]]. Its biological
context shapes the data model, validation, and interpretation.

[[person:aaishamuhammad|Aaisha Muhammad]] gives the
self-taught entry path in
[[podcast:learning-machine-learning-self-taught-bioinformatics|Teaching Yourself Bioinformatics and ML]].
She used the OSSU open curriculum, ML Zoomcamp, and a project-first approach to
build both bioinformatics and machine learning skills without formal coursework.
The episode covers resource evaluation, dataset-first project ideation through
PubMed and Google Scholar, and the transition from notebooks toward Docker and
deployment. Her capstone work on frog-toxicity prediction shows how a
self-directed learner can bridge biological questions with ML pipelines.

## From Sequencing to Analysis

Sequencing is the input side of many bioinformatics workflows. In the 12:35 and
15:30 parts of
[[podcast:bioinformatics-worflows-tools-and-data-science|Bioinformatics Workflows in Practice]],
[[person:sebastianayalaruano|Sebastian Ayala Ruano]]
explains genomic data as DNA sequences made from four nucleotides. The four are
adenine, guanine, cytosine, and thymine. A sequencing workflow reads DNA from an
environmental or biological sample. It breaks the DNA into small pieces, decodes
the order of nucleotides, assembles the pieces, and compares the result with
databases or a reference genome.

That turns a physical sample into analyzable data. The downstream work can look
like familiar data science because it includes exploration, matching, and
feature interpretation. It also includes modeling and comparison against known
references.

The biological stakes change the meaning of the features. A DNA segment may be
tied to genes, proteins, or population markers. It may also be tied to health
traits or organisms observed in a mixed sample.

## Metagenomics and Abundance Tables

Metagenomics is the episode's clearest pipeline example because it turns raw
biological material into analytical tables. At 17:56 in
[[podcast:bioinformatics-worflows-tools-and-data-science|Bioinformatics Workflows in Practice]],
[[person:sebastianayalaruano|Sebastian Ayala Ruano]]
describes metagenomics as studying DNA from environmental samples rather than
from one organism. Environmental samples may come from a lake, soil, or a
wastewater treatment plant. They may contain many microorganisms, so the
analysis must decode the mixed DNA and reconstruct the genomes or organism
signals inside it.

For Sebastian's wastewater treatment microbiome project, the working data took
the form of abundance tables. At 19:41 and 20:10, he describes rows as
microorganisms and columns as samples. Values are counts showing how often each
organism appears. Those tables make the workflow recognizable to a data
scientist. Datasets from multiple studies are combined, categorized by biome,
and analyzed for patterns across samples.

## Microbiome Network Inference

The microbiome project moves from tabular analysis into graph analysis. In
[[podcast:bioinformatics-worflows-tools-and-data-science|Bioinformatics Workflows in Practice]],
[[person:sebastianayalaruano|Sebastian Ayala Ruano]]
explains at 20:10 that microbial association networks are inferred from
co-abundance patterns. If two microorganisms often appear together in similar
abundance, the workflow creates a possible association between them.

At 24:31, Sebastian names CC Lasso as the method used in that project to infer
potential microorganism interactions. The output includes correlation values
between microorganism pairs, thresholding, and positive or negative
associations.

He's careful about interpretation because a positive association can suggest
coexistence, while a negative one can suggest that one organism appears when
another doesn't. Geography, sampling, and biological context still matter.

The network then becomes a knowledge graph. Around 36:20 and 38:31, Sebastian
describes MCW2 Graph as an open-source knowledge graph where microorganisms are
nodes and inferred co-abundance patterns are edges. Extra metadata describes
metabolites, biomes, and biological processes. Users can explore the data in a
Streamlit app or download raw CSV files. They can also open the graph in Neo4j
and run graph algorithms such as clustering or centrality analysis.

## Open-Source Computational Biology Tools

The tooling discussion shows why [[open source]]
is part of the bioinformatics data science workflow rather than an add-on. In
[[podcast:bioinformatics-worflows-tools-and-data-science|Bioinformatics Workflows in Practice]],
[[person:sebastianayalaruano|Sebastian Ayala Ruano]]
uses MCW2 Graph and VueGen as examples. He also names VueCore and Viewer. These
tools make biological data easier to explore, report, and visualize.

VueGen is the reporting example. At 40:00, Sebastian explains it as a Python
package that reads a structured directory. The directory can contain tables,
plots, network data, or HTML files. VueGen then generates static documents,
presentations, and Streamlit apps.

Under the hood, the tool uses Quarto and Streamlit rather than LLM
interpretation. That matters for
[[reproducibility]] because the
report is generated from explicit files, paths, and descriptions. It also uses
YAML metadata and renderable project structure.

The package ecosystem also shapes what bioinformatics data scientists build
with. At 42:29 and 50:25 in the same episode, Sebastian discusses Bioconda and
Bioconductor as biology-oriented package ecosystems. He notes that R still has a
larger bioinformatics community, while more work is moving to Python. He also
warns that some scientific packages are created by scientists who aren't trained
software developers. Because of that, scaling or adapting them can require
reading source code, extending the package, or contacting maintainers.

## Related Pages

Use these pages for the neighboring concepts named in the workflow.

- [[Data Science]] for analysis and
  modeling in a broader setting.
- [[Machine Learning]] for
  prediction, evaluation, and model-driven workflows.
- [[Open Source]] for public tools,
  package ecosystems, documentation, and contribution work.
- [[Reproducibility]] for rerunnable
  analysis, reports, environments, and metadata.
- [[Data Pipelines]] for movement,
  transformation, publication, and rerun patterns behind biological analysis.
