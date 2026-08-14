# Experiment 4: Connected to All Selected Nodes

## Dataset

Facebook Graph

- Nodes: 4039
- Edges: 88234

## Selected Nodes

0

1

Nodes Connected to All Selected Nodes: 16

---

## Median Runtime (50 runs)

Adjacency List   : 0.0000076245 seconds

Adjacency Matrix : 0.0004593239 seconds

SQL              : 0.0255346897 seconds

---

## Relative Performance

Adjacency Matrix was 60.2× slower than the Adjacency List.

SQL was 3,349.0× slower than the Adjacency List.

SQL was 55.6× slower than the Adjacency Matrix.

---

## Observations

1. The adjacency list was the fastest representation for finding nodes connected to all selected nodes.

2. The adjacency matrix was approximately 60 times slower than the adjacency list.

3. The SQL edge-table representation was substantially slower than both graph-oriented representations.

4. This operation generalizes the Common Neighbors problem by intersecting the neighbor sets of multiple selected nodes.

5. The results again demonstrate that graph-oriented representations are particularly effective for intersection-based operations on sparse graphs.

6. For this operation, the performance ordering was:

   Adjacency List < Adjacency Matrix < SQL Edge Table
