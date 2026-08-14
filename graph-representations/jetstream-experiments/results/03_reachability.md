# Experiment 3: Reachability

## Dataset

Facebook Graph

- Nodes: 4039
- Edges: 88234

## Start Node

107

---

## k = 1

Reachable Nodes: 1046

| Representation | Median Runtime (sec) |
|---------------|----------------------|
| Adjacency List | 0.0001448279 |
| Adjacency Matrix | 0.0004475976 |
| SQL | 0.0252984995 |

Adjacency Matrix was 3.1× slower than the Adjacency List.

SQL was 174.7× slower than the Adjacency List.

SQL was 56.5× slower than the Adjacency Matrix.

---

## k = 2

Reachable Nodes: 2687

| Representation | Median Runtime (sec) |
|---------------|----------------------|
| Adjacency List | 0.0023129592 |
| Adjacency Matrix | 0.3172365215 |
| SQL | 0.0461337615 |

Adjacency Matrix was 137.2× slower than the Adjacency List.

SQL was 19.9× slower than the Adjacency List.

SQL was approximately 6.9× faster than the Adjacency Matrix.

---

## k = 3

Reachable Nodes: 3780

| Representation | Median Runtime (sec) |
|---------------|----------------------|
| Adjacency List | 0.0051189810 |
| Adjacency Matrix | 0.8331245745 |
| SQL | 0.0660609566 |

Adjacency Matrix was 162.8× slower than the Adjacency List.

SQL was 12.9× slower than the Adjacency List.

SQL was approximately 12.6× faster than the Adjacency Matrix.

---

## k = 4

Reachable Nodes: 3897

| Representation | Median Runtime (sec) |
|---------------|----------------------|
| Adjacency List | 0.0073753279 |
| Adjacency Matrix | 1.1957210191 |
| SQL | 0.0881870436 |

Adjacency Matrix was 162.1× slower than the Adjacency List.

SQL was 12.0× slower than the Adjacency List.

SQL was approximately 13.6× faster than the Adjacency Matrix.

---

## k = 5

Reachable Nodes: 4039

| Representation | Median Runtime (sec) |
|---------------|----------------------|
| Adjacency List | 0.0074858116 |
| Adjacency Matrix | 1.2269140936 |
| SQL | 0.1101992833 |

Adjacency Matrix was 163.9× slower than the Adjacency List.

SQL was 14.7× slower than the Adjacency List.

SQL was approximately 11.1× faster than the Adjacency Matrix.

---

## Observations

1. The adjacency-list representation consistently produced the fastest reachability queries.

2. The adjacency-matrix representation performed well for one-hop reachability but became significantly slower as the search expanded through the graph.

3. For k ≥ 2, DuckDB SQL reachability queries were consistently faster than the adjacency-matrix implementation.

4. Node 107 is highly central in the Facebook graph:
   - 1 hop reaches 1046 nodes.
   - 2 hops reaches 2687 nodes.
   - 3 hops reaches 3780 nodes.
   - 4 hops reaches 3897 nodes.
   - 5 hops reaches all 4039 nodes in the graph.

5. The results suggest that graph-representation tradeoffs depend strongly on the operation being performed. Adjacency lists were best for traversal, while SQL-based reachability was substantially more efficient than the adjacency-matrix implementation on this sparse real-world graph.