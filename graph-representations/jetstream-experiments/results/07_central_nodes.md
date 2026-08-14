# Investigation 3: Central Nodes

## Dataset

Facebook Graph

- Nodes: 4039
- Edges: 88234

---

## Goal

This investigation explores several different ways to identify important or influential nodes in a graph.

We compare:

1. **Degree**
2. **3-Hop Reachability**
3. **Closeness Centrality**

The goal is to determine whether all measures identify the same nodes as important.

---

## Definitions

### Degree

The degree of a node is the number of neighbors directly connected to that node.

A node with a high degree can directly reach many other nodes.

Example:

```text
Degree(node) = Number of direct neighbors
```

### 3-Hop Reachability

The 3-hop reachability of a node is the number of nodes that can be reached from the node using at most three edges.

A node with high reachability can potentially influence a large portion of the network through a small number of intermediate nodes.

Example:

```text
3-Hop Reachability(node)
=
Number of nodes reachable within 3 hops
```

### Closeness Centrality

Closeness centrality measures how close a node is to all other nodes in the graph.

A node is considered central if it can reach other nodes using relatively short paths.

Definition:

```text
Closeness(node)

=
1 / (average shortest-path distance
     from node to all other nodes)
```

Higher values indicate that a node is generally closer to the rest of the network.

---

## Computing the Measures

### Degree

For every node:

1. Retrieve its adjacency list.
2. Count the number of neighbors.

```text
Degree(node) = len(adj[node])
```

### 3-Hop Reachability

For every node:

1. Run Breadth-First Search (BFS).
2. Explore nodes up to distance 3.
3. Count all reachable nodes.

### Closeness Centrality

For every node:

1. Compute shortest-path distances to all other nodes.
2. Compute the average distance.
3. Take the reciprocal.

Nodes with smaller average distances obtain larger centrality values.

---

## Top 10 Nodes by Degree

| Rank | Node | Degree | Reach3 | Closeness |
|------|------|---------:|---------:|---------:|
| 1 | 107 | 1045 | 3780 | 0.459699 |
| 2 | 1684 | 792 | 3327 | 0.393606 |
| 3 | 1912 | 755 | 3238 | 0.350947 |
| 4 | 3437 | 547 | 2116 | 0.314413 |
| 5 | 0 | 347 | 3261 | 0.353343 |
| 6 | 2543 | 294 | 2278 | 0.291300 |
| 7 | 2347 | 291 | 1958 | 0.283408 |
| 8 | 1888 | 254 | 2687 | 0.321292 |
| 9 | 1800 | 245 | 2687 | 0.321599 |
| 10 | 1663 | 235 | 3261 | 0.339185 |

---

## Top 10 Nodes by 3-Hop Reachability

| Rank | Node | Degree | Reach3 | Closeness |
|------|------|---------:|---------:|---------:|
| 1 | 563 | 91 | 3833 | 0.393913 |
| 2 | 414 | 159 | 3833 | 0.369543 |
| 3 | 428 | 115 | 3833 | 0.394837 |
| 4 | 107 | 1045 | 3780 | 0.459699 |
| 5 | 1136 | 33 | 3780 | 0.356305 |
| 6 | 1687 | 43 | 3780 | 0.357250 |
| 7 | 376 | 133 | 3778 | 0.366558 |
| 8 | 566 | 85 | 3778 | 0.364967 |
| 9 | 353 | 102 | 3778 | 0.363097 |
| 10 | 420 | 34 | 3778 | 0.361019 |

---

## Top 10 Nodes by Closeness Centrality

| Rank | Node | Degree | Reach3 | Closeness |
|------|------|---------:|---------:|---------:|
| 1 | 107 | 1045 | 3780 | 0.459699 |
| 2 | 58 | 12 | 3262 | 0.397402 |
| 3 | 428 | 115 | 3833 | 0.394837 |
| 4 | 563 | 91 | 3833 | 0.393913 |
| 5 | 1684 | 792 | 3327 | 0.393606 |
| 6 | 171 | 22 | 3262 | 0.370493 |
| 7 | 348 | 229 | 3778 | 0.369916 |
| 8 | 483 | 231 | 3778 | 0.369848 |
| 9 | 414 | 159 | 3833 | 0.369543 |
| 10 | 376 | 133 | 3778 | 0.366558 |

---

## Observations

### Observation 1: Node 107 Is Important Under All Measures

Node 107 ranks near the top for:

- Degree
- Reachability
- Closeness Centrality

This suggests that node 107 occupies a highly influential position in the network.

### Observation 2: Degree and Influence Are Not Identical

Several nodes with relatively modest degrees appear near the top of the reachability rankings.

Examples:

| Node | Degree | Reach3 |
|------|---------:|---------:|
| 563 | 91 | 3833 |
| 428 | 115 | 3833 |
| 414 | 159 | 3833 |

These nodes outperform many higher-degree nodes when indirect influence is considered.

### Observation 3: Low-Degree Nodes Can Still Be Highly Central

Node 58 provides a particularly surprising result:

| Node | Degree | Closeness |
|------|---------:|---------:|
| 58 | 12 | 0.397402 |

Although node 58 has only 12 direct neighbors, it ranks second in closeness centrality.

This suggests that the node is positioned near important communication paths in the graph.

### Observation 4: Reachability and Closeness Often Agree

Many nodes that rank highly in 3-hop reachability also rank highly in closeness centrality.

Examples include:

- Node 428
- Node 563
- Node 414
- Node 376

These nodes appear to be well positioned within the network structure.

### Observation 5: Different Definitions Produce Different Rankings

The rankings demonstrate that there is no single definition of an "important" node.

Depending on the question being asked, one might prefer:

- Degree (direct influence)
- Reachability (short-term network influence)
- Closeness Centrality (global accessibility)

---

## Conclusions

1. Degree, reachability, and closeness centrality measure different aspects of influence.

2. High degree alone does not guarantee high influence.

3. A node with relatively few direct neighbors may still occupy a highly central position within the network.

4. Understanding large networks often requires multiple measures rather than relying on a single metric.

5. The Facebook graph contains nodes that act as highly connected hubs as well as nodes that achieve strategic network positions despite having relatively modest degrees.
```
