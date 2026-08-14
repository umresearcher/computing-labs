# Experiment 2: Common Neighbors

## Dataset

Facebook Graph

- Nodes: 4039
- Edges: 88234

## Nodes

107

1684

Number of Common Neighbors: 14

---

## Median Runtime (50 runs)

Adjacency List   : 0.0000332783 seconds

Adjacency Matrix : 0.0003115251 seconds

SQL              : 0.0398841829 seconds

---

## Relative Performance

Adjacency Matrix was 9.4× slower than the Adjacency List.

SQL was 1,198.5× slower than the Adjacency List.

SQL was 128.0× slower than the Adjacency Matrix.

---

## Observations

1. The adjacency list was the fastest representation for finding common neighbors.

2. The adjacency matrix was approximately 9 times slower than the adjacency list.

3. The SQL edge-table representation was substantially slower than both graph-oriented representations.

4. The performance gap between adjacency lists and adjacency matrices was much smaller than for the Neighbor Lookup experiment.

5. The results suggest that the impact of graph representation depends strongly on the operation being performed. A representation that performs well for one operation may not provide the same advantage for another.