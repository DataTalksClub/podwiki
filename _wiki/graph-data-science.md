---
layout: wiki
title: "Graph Data Science"
summary: "Graph data science applies graph algorithms and ML to nodes, edges, paths, centrality, similarity, and domain workflows."
related:
  - Knowledge Graph vs Vector Search
  - Graph RAG vs Vector RAG
  - Simulation and Digital Twins
  - Vector Databases
  - Embeddings
  - Bioinformatics Data Science
  - Retrieval-Augmented Generation
  - Recommendation Systems
  - Search
  - Information Retrieval
  - Machine Learning Portfolio Projects
  - Freelance Data and ML Careers
  - Tools
  - Machine Learning
---

Graph data science applies [[machine-learning=>machine learning]] and graph
algorithms to data represented as nodes and edges. It fits domains where the
relationships matter. In the podcast evidence, those relationships include
vehicle parts connected through [[simulation-and-digital-twins=>crash simulation]]
structure. They also include sibling vehicle designs linked by engineering
changes and microorganisms connected through co-abundance structures in
[[bioinformatics-data-science=>bioinformatics data science]].
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@18:27=>Automotive Knowledge Graphs]]
[[cite:bioinformatics-worflows-tools-and-data-science@20:10=>Bioinformatics Workflows]]

The useful boundary is computation. A [[knowledge-graph-vs-vector-search=>knowledge graph]]
can store the entities, properties, and typed relations. Graph data science
starts when a team computes over that structure or over an extracted subgraph.
That work includes similarity and path analysis. It can also include clustering,
centrality, link prediction, and graph visualization.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@26:15=>Computational Graphs]]
[[cite:bioinformatics-worflows-tools-and-data-science@39:13=>Graph Algorithms]]

Keep retrieval separate from analytics because graph retrieval returns nodes
and edges, plus paths, neighborhoods, or query results. [[vector-databases=>Vector retrieval]]
returns nearby chunks or records from [[embeddings]]. When teams turn those
results into LLM context, the question belongs with
[[graph-rag-vs-vector-rag=>Graph RAG vs Vector RAG]] and
[[retrieval-augmented-generation=>Retrieval-Augmented Generation]], not only with
graph analytics.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@38:10=>KG Semantics]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@42:49=>Vector RAG Retrieval]]

## Knowledge Graphs Store Domain Semantics

A knowledge graph stores what the domain knows about entities and relations. In
the automotive R&D discussion, the graph can connect vehicles and parts. It can
also connect sensors and release year. It can connect upper body, platform,
requirements, and simulation outcomes. Engineers can query related cars,
related parts, and simulation context before they extract a smaller graph for
computation.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@18:27=>Automotive Knowledge Graphs]]
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@25:46=>Graph Queries]]

The same storage role appears in wastewater microbiome work. Sebastian Ayala
Ruano describes MCW2 Graph as a knowledge graph for the wastewater treatment
microbiome. Researchers infer microbial association networks from abundance
relationships, then enrich the graph with metadata such as metabolites, biomes, and
biological processes.
[[cite:bioinformatics-worflows-tools-and-data-science@03:53=>Wastewater Microbiome KG]]
[[cite:bioinformatics-worflows-tools-and-data-science@37:03=>MCW2 Graph]]

This storage layer is related to [[tools=>tools]] and data modeling, but it's
not the same as graph analytics. A graph database can answer relation queries.
Graph data science computes structures or predictions over the graph.
[[knowledge-graph-vs-vector-search=>Knowledge Graph vs Vector Search]] covers
that storage and retrieval substrate in more detail.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@24:41=>Knowledge Graph vs GDS]]

## Graph Analytics Computes Over Structure

Graph analytics answers questions about neighborhoods, paths, groups, and
important nodes. In crash simulation analysis, weighted graphs and visualization
help engineers compare more than 300 simulations. The graph can also reveal
commonly involved parts, simulation clusters, and the main load path through
connected vehicle parts.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@22:11=>Load Path Detection]]

Anahita Pakiman separates the full automotive knowledge graph from the smaller
computational graph used for graph data science. The knowledge graph can hold
many simulations and market vehicles. The analytics graph can be a focused
NetworkX-style graph made from selected simulations and parts. Teams can then
use it for similarity analysis, longest-path analysis, visualization, and
structure discovery.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@26:15=>Computational Graphs]]
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@27:16=>Focused Graph Analytics]]

Bioinformatics gives the scientific version. Abundance tables start as rows of
microorganisms and columns of samples. Researchers infer co-abundance edges from
correlations and thresholds. They then run clustering or centrality analysis
over the inferred edges plus metadata in Neo4j.
[[cite:bioinformatics-worflows-tools-and-data-science@20:10=>Abundance Tables]]
[[cite:bioinformatics-worflows-tools-and-data-science@24:31=>Network Inference]]
[[cite:bioinformatics-worflows-tools-and-data-science@39:13=>Clustering and Centrality]]

## Graph Machine Learning Uses Relationships

Graph machine learning in these podcast examples focuses on similarity and
prediction over connected structures. The automotive episode uses SimRank to
rank related simulations when engineers don't have a direct human ranking of
simulation similarity. The graph can take one simulation as input and return
related analyses by graph similarity.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@28:55=>SimRank Similarity]]

The supervised evidence is narrower. Anahita describes simulation relationships
through a development tree where physical design changes, such as a thickness
change or an added hole, connect sibling simulations. The learning problem tries
to transfer behavior between sibling vehicles and predict absorption levels from
those relationships.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@18:27=>Sibling Vehicle Prediction]]

Graph ML can also help retrieval choose which graph context to look at. If
similarity, link prediction, or edge scores select nodes and relations for an
LLM prompt, the work has crossed into
[[graph-rag-vs-vector-rag=>Graph RAG vs Vector RAG]].
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@33:56=>Graph Data Science for RAG]]

## Edge Quality Controls Trust

The episodes don't treat every graph as automatically better than a table. In
automotive simulation work, many vehicle properties can still fit rows and
columns. Edges help when they encode real relationships. The automotive examples
include platform and upper-body structure, sibling vehicles, and physical design
changes. They also include connected parts and simulation context.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@20:32=>Graph vs Tables]]
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@22:11=>Graph Load Paths]]

Bioinformatics has a different trust problem because co-abundance edges come
from correlation values and thresholds. Positive correlations can suggest
coexistence, and negative correlations can suggest that one microorganism
appears when another doesn't. Sebastian cautions that these correlations may
have biological interpretations, but teams should treat them carefully. Sampling
geography can affect what appears in the graph.
[[cite:bioinformatics-worflows-tools-and-data-science@25:22=>Correlation Thresholds]]
[[cite:bioinformatics-worflows-tools-and-data-science@26:30=>Sampling Geography]]

Graph content generated by an LLM adds another trust boundary. The automotive
discussion warns that extracting a large knowledge graph from text with an LLM
can be hard to validate. Teams still need controlled graph-building and
verification when analytics or downstream retrieval depends on the graph.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@42:42=>LLM Graph Verification]]

## Graph Retrieval Returns Relations

Graph retrieval uses graph structure as the retrieval unit. It can return a
node, a typed relation, or a path. It can also return a neighborhood or a
Cypher-derived result. In the automotive R&D episode, a knowledge graph can
preserve chapter order and containment. It can also preserve page-to-chapter
links and domain relations that a prompt can use as structured context.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@38:10=>KG Semantics]]

That's different from graph analytics. Analytics asks what the graph reveals
through paths, clusters, centrality, or similarity. Retrieval asks which graph
facts should be returned for a query or placed in an LLM prompt. Cypher-style
queries are one route from stored graph semantics to retrieved context.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@39:56=>Cypher Retrieval]]

Use [[knowledge-graph-vs-vector-search=>Knowledge Graph vs Vector Search]] when
the design question is whether explicit relations or vector similarity should
drive retrieval. Use [[graph-rag-vs-vector-rag=>Graph RAG vs Vector RAG]] when
the retrieved graph facts, paths, or chunks become prompt evidence.

## Vector Retrieval Returns Similar Items

Vector retrieval starts from [[embeddings]], not explicit graph edges, and Atita
Arora's search discussion describes the RAG flow. Teams split transcripts into
chunks, embed the chunks, and store them in a vector database or search engine.
At query time, they embed the user query, retrieve nearby chunks, and put those
chunks into the prompt with references.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@38:24=>Chunking and Embeddings]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@42:49=>Vector Retrieval]]

Vector retrieval is retrieval work, not graph data science. It helps when the
system needs semantically similar passages, products, images, or sessions. It
can also retrieve records. It doesn't automatically preserve chapter order,
parent-child containment, typed edges, or provenance paths unless the system
adds that structure elsewhere.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@38:10=>Vector Chunks vs KG Relations]]
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@52:07=>Vector Recommendations]]

The practical split follows the retrieval failure. Improve vector retrieval when
the system misses semantically related material or retrieves too little context.
Add graph retrieval when the answer depends on relation types, graph paths, or
hierarchy. It also helps when the answer depends on constraints or provenance.
[[search=>Search]], [[information-retrieval=>Information Retrieval]], and
[[vector-databases=>Vector Databases]] cover the vector side of that stack.
[[cite:modern-search-systems-vector-databases-llms-semantic-retrieval@47:31=>Vector Similarity Context]]

## Domain Workflows

Automotive R&D uses graph data science when simulations, vehicle structures, and
engineering changes form a connected system. Semantic reporting helps engineers
compare costly crash simulation results. Graph analysis adds relationship
analysis across simulations, load-path detection, and similarity ranking for
related analyses.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@15:58=>Automotive Graph Motivation]]
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@22:11=>Crash Simulation Analytics]]
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@28:55=>Simulation Similarity]]

Bioinformatics uses graph data science when biological entities interact or
co-occur. Microbial association networks turn metagenomic abundance tables into
graphs. Researchers can then look for microbial communities involved in
pathways or biological processes. They can still expose raw CSV files, web
visualizations, Neo4j dumps, and reports for reproducible scientific work.
[[cite:bioinformatics-worflows-tools-and-data-science@37:33=>Microbial Communities]]
[[cite:bioinformatics-worflows-tools-and-data-science@38:31=>Bioinformatics Graph Tooling]]

Product and portfolio work has narrower evidence in this archive. A freelance
ML example mentions automating knowledge graph generation for a recommendation
system with insurance applications. That connects graph construction to
[[Recommendation Systems]],
[[Machine Learning Portfolio Projects]], and
[[freelance-data-and-ml-careers=>Freelance Data and ML Careers]] when the
product needs explicit relationships. It doesn't establish a full graph
analytics workflow.
[[cite:from-biology-to-machine-learning-data-science-portfolio-open-source-computer-vision-transformers=>From Biology to ML]]

## Tooling Patterns

The graph data science examples rely on ordinary [[tools=>tools]] as much as
algorithms. Automotive work uses Neo4j for the larger knowledge graph and
extracts smaller NetworkX-style graphs for analytics. Bioinformatics work uses
Streamlit, CSV exports, Neo4j dumps, and report-generation tooling so
researchers can look at raw data and graph outputs.
[[cite:knowledge-graphs-and-llms-for-automotive-rnd@26:15=>NetworkX Graph Analytics]]
[[cite:bioinformatics-worflows-tools-and-data-science@38:31=>Streamlit and Neo4j]]

## Related Pages

Graph work crosses retrieval systems, vector search, and domain modeling.

- [[knowledge-graph-vs-vector-search=>Knowledge Graph vs Vector Search]] for the storage and retrieval boundary.
- [[graph-rag-vs-vector-rag=>Graph RAG vs Vector RAG]] for graph and vector context in LLM systems.
- [[simulation-and-digital-twins=>Simulation and Digital Twins]] for connected simulation and engineering examples.
- [[retrieval-augmented-generation=>Retrieval-Augmented Generation]] for the broader retrieval-plus-generation workflow.
- [[vector-databases=>Vector Databases]] and [[embeddings=>Embeddings]] for the vector retrieval side.
- [[bioinformatics-data-science=>Bioinformatics Data Science]] for the microbiome-network case.
- [[Recommendation Systems]] for graph construction in product recommendation work.
- [[Machine Learning Portfolio Projects]] and [[freelance-data-and-ml-careers=>Freelance Data and ML Careers]] for graph-based project positioning.
- [[search=>Search]] and [[information-retrieval=>Information Retrieval]] for retrieval systems that graph or vector methods can feed.
- [[tools=>Tools]] for the tooling layer around Neo4j, NetworkX, Streamlit, CSV exports, and generated reports.
- [[entity-resolution=>Entity Resolution]] for a neighboring entity-modeling problem that focuses on matching records before graph analysis or fraud review.
