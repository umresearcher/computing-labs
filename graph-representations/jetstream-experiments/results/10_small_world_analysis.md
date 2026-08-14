# Investigation 6: Small-World Analysis

## Dataset

Facebook Graph

- Nodes: 4039
- Edges: 88234

---

## Goal

This investigation explores how quickly nodes can reach one another in the Facebook graph.

Many real-world social networks exhibit the **small-world phenomenon**, which suggests that most nodes can be reached from one another using only a small number of intermediate connections.

The investigation examines:

- Connected components
- Diameter
- Radius
- Average shortest-path length
- Eccentricity

---

## Definitions

### Connected Component

A connected component is a set of nodes in which every node can reach every other node.

If a graph has only one connected component, then every node can reach every other node.

### Shortest Path

A shortest path between two nodes is a path containing the fewest possible edges.

### Average Shortest-Path Length

The average shortest-path length is the average number of hops required to travel between pairs of nodes in the graph.

Smaller values indicate that nodes are generally close to one another.

### Eccentricity

The eccentricity of a node is the maximum shortest-path distance from that node to any other node.

Example:

```text
Eccentricity(node) = 5
```

means that every node in the graph can be reached from that node within at most 5 hops.

### Radius

The radius of a graph is the minimum eccentricity among all nodes.

A node whose eccentricity equals the radius is often called a **central node**.

### Diameter

The diameter of a graph is the maximum eccentricity among all nodes.

It represents the largest shortest-path distance between any pair of nodes in the graph.

All nodes satisfy:

```text
Radius ≤ Eccentricity(node) ≤ Diameter
```

---

## Results

### Connectivity

Connected Components: 1

Largest Component Size: 4039

The graph consists of a single connected component containing every node in the dataset.

---

### Distance Measures

Diameter: 8

Radius: 4

Average Shortest-Path Length: 3.693

---

## Nodes with Lowest Eccentricity

| Rank | Node | Eccentricity |
|------|------|-------------:|
| 1 | 567 | 4 |
| 2 | 58 | 5 |
| 3 | 107 | 5 |
| 4 | 171 | 5 |
| 5 | 348 | 5 |

These nodes can reach all other nodes within a relatively small number of hops.

---

## Nodes with Highest Eccentricity

| Rank | Node | Eccentricity |
|------|------|-------------:|
| 1 | 687 | 8 |
| 2 | 688 | 8 |
| 3 | 689 | 8 |
| 4 | 690 | 8 |
| 5 | 691 | 8 |

These nodes are among the most distant nodes in the graph with respect to shortest-path distance.

---

## Observations

### Observation 1: The Graph Is Fully Connected

The graph contains a single connected component consisting of all 4039 nodes.

Every node can reach every other node.

---

### Observation 2: Short Paths Link Most Nodes

The average shortest-path length is only 3.693.

This means that, on average, fewer than four hops are required to travel between two randomly selected nodes.

---

### Observation 3: The Diameter Is Small

The diameter of the graph is 8.

This means that no pair of nodes is more than 8 hops apart.

Even the most distant nodes in the graph can be connected through a relatively short path.

---

### Observation 4: Some Nodes Are Especially Central

The radius of the graph is 4.

Node 567 has eccentricity 4, meaning that every node in the graph can be reached from node 567 within four hops.

This makes node 567 one of the most central nodes in the network.

---

### Observation 5: Centrality Is Different from Degree

Node 567 previously appeared among the top reachability and centrality rankings despite not having an exceptionally large degree.

This suggests that a node's position within the network can be more important than the number of direct neighbors.

---

### Observation 6: The Results Support the Small-World Hypothesis

The graph exhibits several characteristics associated with small-world networks:

- A single large connected component.
- Small average shortest-path length.
- Small diameter relative to graph size.
- Highly central nodes that can quickly reach the entire graph.

---

## Conclusions

1. The Facebook graph is fully connected.

2. Most nodes can be reached in only a few hops.

3. The diameter of the graph is 8, indicating that even the most distant nodes are relatively close.

4. Node 567 is among the most central nodes in the graph, with eccentricity equal to the graph radius.

5. The Facebook graph exhibits strong small-world characteristics, demonstrating how large social networks can remain highly connected despite containing thousands of nodes.
