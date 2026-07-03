---
layout: wiki
title: "Graph Data Science"
summary: "Graph data science uses nodes, edges, paths, similarity, clustering, centrality, and graph-aware machine learning to analyze relationship-heavy systems such as crash simulations, microbiomes, scientific papers, and knowledge-grounded LLM workflows."
related:
  - Knowledge Graph vs Vector Search
  - Graph RAG vs Vector RAG
  - Bioinformatics Data Science
  - Entity Resolution
  - Retrieval-Augmented Generation
  - Machine Learning
---

Graph data science applies data science and
[[machine-learning=>machine learning]]
methods to data represented as nodes and edges. In the DataTalks.Club podcast
archive, the clearest examples come from automotive R&D and
[[bioinformatics-data-science=>bioinformatics data science]]. Crash simulations
become connected structures for similarity, load-path, and behavior analysis.
Wastewater microbiome studies become microbial association networks enriched
into knowledge graphs.[[cite:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]][[cite:bioinformatics-worflows-tools-and-data-science|Bioinformatics Workflows in Practice]]

The useful boundary is between storing relationships and analyzing them. A
knowledge graph can preserve domain entities, metadata, and relations. Graph
data science takes a relevant subgraph from that structure. It then computes
over the subgraph with graph algorithms, similarity measures, visualization, or
predictive models.[[cite:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]

## Graph Representations

Graph representation starts when the relationship is part of the signal.
Automotive crash simulation work can connect vehicle structure with simulation
context. Engineers can then compare sibling vehicles and related analyses. That
structure can also connect physical changes with simulation outcomes. It keeps
crash behavior from being flattened into one experiment table.[[cite:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]

The graph isn't a replacement for every table. Many vehicle properties can be
expressed as rows and columns. The graph helps when teams need to look at
relationships across hundreds of simulations. It can also help teams find common
involved parts. The same structure can cluster similar simulations or detect the
main load path through a vehicle structure.[[cite:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]

Bioinformatics shows the same representation shift from another domain. A
wastewater microbiome workflow starts from abundance tables, where rows are
microorganisms and columns are samples, with counts as values. Co-abundance
relationships then become edges: if two microorganisms often appear together, the
workflow creates a possible association. Positive and negative correlations can
be kept after thresholding, with biological interpretation handled carefully
because geography and sampling can affect the relationship.[[cite:bioinformatics-worflows-tools-and-data-science|Bioinformatics Workflows in Practice]]

## Algorithms and Analytics

Graph analytics answer questions about neighborhoods, paths, groups, and
important nodes. In crash simulation analysis, weighted graphs and visualization
help compare large sets of simulations. They can show common parts and identify
the path that transfers load through connected vehicle parts during a
crash.[[cite:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]

The automotive workflow separates the full knowledge graph from the graph used
for computation. A team can keep many simulations and vehicle relationships in a
knowledge graph, then extract a focused NetworkX-style graph for graph data
science work. That smaller computational graph is where similarity analysis,
longest-path analysis, visualization, and relationship analysis happen.[[cite:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]

The microbiome workflow uses graph algorithms after network inference. MCW2
Graph represents microorganisms as nodes and co-abundance relationships as
edges. It then enriches the graph with metadata such as metabolites, biomes, and
biological processes. Users can explore the graph in a Streamlit application or
download CSV files. They can also open the Neo4j dump and run clustering or
centrality analysis over inferred experimental edges plus metadata.[[cite:bioinformatics-worflows-tools-and-data-science|Bioinformatics Workflows in Practice]]

## Graph Machine Learning

Graph machine learning in these episodes centers on similarity and prediction
over connected structures. The automotive example uses SimRank to rank related
simulations when there's no direct human ranking of simulation similarity. The
intuition is that items referenced by similar items are themselves similar. A
graph can then produce a related-analysis list from one input simulation.[[cite:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]

The supervised side has less evidence in these episodes. A small automotive
toy model used a development tree where simulations were connected by physical
design changes such as thickness changes or added holes. The graph edge encoded
the relation between simulations. The learning task tried to transfer behavior
between sibling vehicles and predict absorption levels from those
relationships.[[cite:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]

Graph data science also supports LLM grounding when the system needs to select
the most relevant node or relation before prompt construction. In that boundary
case, graph similarity and edge prediction can help choose graph context for an
LLM. The final answer still needs verification and source control.[[cite:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]

## Domain Use Cases

Automotive R&D uses graph data science when simulations, vehicle structures, and
engineering changes form a connected system. Semantic reporting helps teams
regenerate and compare costly crash simulation results. Graph analysis adds
relationship analysis across simulations. It also supports load-path detection
and similarity ranking for related analyses.[[cite:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]

Bioinformatics uses graph data science when biological entities interact or
co-occur. Microbial association networks turn metagenomic abundance tables into
graphs. The resulting knowledge graph helps researchers look for microbial
communities involved in pathways or biological processes. The same workflow
stays close to reproducible scientific tooling. Users can look at raw CSV files,
graph dumps, web views, and generated reports.[[cite:bioinformatics-worflows-tools-and-data-science|Bioinformatics Workflows in Practice]]

Machine learning portfolio and freelance work adds a practical product
boundary: knowledge graph automation can appear inside recommendation systems
and insurance applications. Other ML projects may remain image- or
transformer-centered instead of graph-centered. The graph choice depends on
whether the deliverable needs explicit relationships, not only a modern model
architecture.[[cite:from-biology-to-machine-learning-data-science-portfolio-open-source-computer-vision-transformers|From Biology to ML]]

## Boundaries with Knowledge Graphs and RAG

Graph data science isn't the same thing as a knowledge graph. A knowledge graph
models and stores entities plus relation types. It also stores metadata and
provenance. Graph data science computes over a graph or extracted subgraph. It
can find clusters and central nodes. It can also find similar simulations, load
paths, or predicted relationships.[[cite:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]][[cite:bioinformatics-worflows-tools-and-data-science|Bioinformatics Workflows in Practice]]

Graph data science is also separate from vector RAG. Vector RAG chunks text,
embeds it, and retrieves semantically similar passages. Graph RAG retrieves
graph structure such as entities and relations. It can also retrieve paths,
neighborhoods, and Cypher-derived context. Graph data science can support graph
RAG when similarity or edge prediction helps choose graph context. RAG still has
to package that context for an LLM and validate the generated answer.[[cite:knowledge-graphs-and-llms-for-automotive-rnd|Knowledge Graphs and LLMs for Automotive R&D]]

Use [[Knowledge Graph vs Vector Search]] for the storage and retrieval boundary.
Use [[Graph RAG vs Vector RAG]] for LLM context packaging and
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]] for the
broader retrieval-plus-generation workflow. Use
[[bioinformatics-data-science=>Bioinformatics Data Science]] for the
microbiome-network case and [[entity-resolution=>Entity Resolution]] for a
neighboring graph-shaped data product problem.

## Related Pages

Continue with these pages for neighboring retrieval, biology, and graph-shaped
data product topics.

- [[Knowledge Graph vs Vector Search]]
- [[Graph RAG vs Vector RAG]]
- [[Bioinformatics Data Science]]
- [[Entity Resolution]]
- [[Retrieval-Augmented Generation]]
