# Experiment 1: Neighbor Lookup

## Dataset

Facebook Graph

- Nodes: 4039
- Edges: 88234

## Start Node

107 (degree of 107 = 1045)

---

## Median Runtime (50 runs)

Adjacency List   : 0.0000001211 seconds
Adjacency Matrix : 0.0002785118 seconds
SQL              : 0.0158922712 seconds

---

## Observations

1. The adjacency list was the fastest representation for neighbor lookup.

2. The adjacency matrix was approximately 2,300 times slower than the adjacency list. For neighbor lookup, the matrix must scan an entire matrix row, while the adjacency list directly stores the node's neighbors.

3. The SQL edge-table representation was the slowest approach, requiring significantly more work to locate all edges involving the selected node.

4. For this operation, the performance ordering was:

   Adjacency List < Adjacency Matrix < SQL Edge Table
