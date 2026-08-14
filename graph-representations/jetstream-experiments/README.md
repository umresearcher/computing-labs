# Graph Representation Experiments Using Jetstream2

## Purpose

These experiments were developed using Jetstream2
to explore graph representations, graph analytics,
and educational activities based on the SNAP Facebook graph.

The materials complement the public Streamlit lab:

https://graph-representations-umflint.streamlit.app/

and can serve as examples for student projects in
Data Structures, Database Systems, and related courses.

## Folder Structure

```text
scripts/
├── utilities/
├── benchmarks/
└── investigations/

results/
    Markdown reports describing experimental results.

figures/
    Generated visualizations.

data/
    Facebook graph dataset.
```

### Dataset

These experiments use the SNAP Facebook social network dataset.

File:

```text
data/facebook_combined.txt
```

## Benchmark Studies

1. Neighbor Lookup
2. Common Neighbors
3. Connected to All Selected Nodes
4. k-Hop Reachability

## Graph Investigations

5. Degree Analysis
6. Influencer Analysis
7. Central Nodes
8. Community Detection
9. Bridge Nodes
10. Small-World Analysis

## Running the Code

All commands should be executed from the directory:

```text
graph-representations/jetstream-experiments
```

### Installing Required Packages

```bash
pip install pandas duckdb networkx
```

### Activate the Virtual Environment

Linux / Mac:

```bash
source venv/bin/activate
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Running Individual Benchmarks

For example, to run the Common Neighbors benchmark:

```bash
python -m scripts.benchmarks.benchmark_common_neighbors
```

Other available benchmarks include:

```bash
python -m scripts.benchmarks.benchmark_neighbors
python -m scripts.benchmarks.benchmark_common_neighbors
python -m scripts.benchmarks.benchmark_connected_to_all
python -m scripts.benchmarks.benchmark_reachability
```

---

## Running Individual Investigations

For example, to run the Community Detection investigation:

```bash
python -m scripts.investigations.investigate_communities
```

Other available investigations include:

```bash
python -m scripts.investigations.investigate_degrees
python -m scripts.investigations.investigate_influencers
python -m scripts.investigations.investigate_central_nodes
python -m scripts.investigations.investigate_communities
python -m scripts.investigations.investigate_bridge_nodes
python -m scripts.investigations.investigate_small_world
```

---

## Running All Benchmarks

```bash
python -m scripts.run_benchmarks
```

---

## Running All Investigations

```bash
python -m scripts.run_investigations
```

---

## Running Everything

```bash
python -m scripts.run_all
```

This executes all benchmarks and all investigations.

## Experimental Results

The reports generated from the experiments are available in:

results/README.md

### Educational Use

These experiments were developed to support instruction in:

- Data Structures
- Database Systems
- Graph Analytics

Students may reproduce the experiments, modify the code, and develop their own investigations using real-world graph data.

