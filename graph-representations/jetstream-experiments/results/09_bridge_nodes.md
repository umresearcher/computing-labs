# Investigation 5: Bridge Nodes

## Dataset

Facebook Graph

- Nodes: 4039
- Edges: 88234

---

## Goal

This investigation explores the following question:

> Which nodes serve as bridges between different parts of the network?

Some nodes may be important not because they have many neighbors, but because they connect otherwise distant regions of the graph.

---

## Definition

### Betweenness Centrality

Betweenness centrality measures how often a node lies on shortest paths between other pairs of nodes.

A node receives a high betweenness score if many shortest paths in the graph pass through it.

Intuitively:

- High-degree nodes have many direct neighbors.
- High-betweenness nodes act as bridges connecting different regions of the graph.

Such nodes may be important for communication and information flow within the network.

---

## Algorithm

For every node:

1. Consider every pair of nodes in the graph.
2. Find shortest paths between the pair.
3. Determine whether the node lies on those shortest paths.
4. Count how often this occurs.
5. Normalize the result to obtain the betweenness centrality score.

Nodes with larger scores participate in more shortest paths and therefore play a more important bridging role.

---

## Top 10 Bridge Nodes

| Rank | Node | Degree | Betweenness Centrality |
|------|------|---------:|---------:|
| 1 | 107 | 1045 | 0.480518 |
| 2 | 1684 | 792 | 0.337797 |
| 3 | 3437 | 547 | 0.236115 |
| 4 | 1912 | 755 | 0.229295 |
| 5 | 1085 | 66 | 0.149015 |
| 6 | 0 | 347 | 0.146306 |
| 7 | 698 | 68 | 0.115330 |
| 8 | 567 | 63 | 0.096310 |
| 9 | 58 | 12 | 0.084360 |
| 10 | 428 | 115 | 0.064309 |

---

## Observations

### Observation 1: Node 107 Remains the Most Important Node

Node 107 ranked highest in:

- Degree
- 3-Hop Reachability
- Closeness Centrality
- Betweenness Centrality

This suggests that node 107 occupies an exceptionally influential position in the Facebook graph.

---

### Observation 2: Bridge Nodes Do Not Need High Degree

Several nodes have relatively modest degrees but rank highly in betweenness centrality.

Examples:

| Node | Degree | Betweenness |
|------|---------:|---------:|
| 1085 | 66 | 0.149015 |
| 698 | 68 | 0.115330 |
| 567 | 63 | 0.096310 |
| 58 | 12 | 0.084360 |

These nodes appear to play important structural roles despite having relatively few direct neighbors.

---

### Observation 3: Node 58 Appears Again

In the Central Nodes investigation, node 58 ranked second in closeness centrality despite having only 12 neighbors.

Node 58 also appears among the top bridge nodes.

This suggests that node 58 occupies a strategically important position within the network.

---

### Observation 4: Degree and Betweenness Measure Different Concepts

Degree measures:

> How many neighbors a node has.

Betweenness measures:

> How important a node is for connecting different parts of the network.

A node can have:

- many neighbors but limited bridging importance, or
- relatively few neighbors but significant influence over communication paths.

---

### Observation 5: Community Structure May Explain the Results

The Community Detection investigation identified 16 communities.

High-betweenness nodes may serve as connections between those communities.

Removing such nodes could potentially increase separation between communities and reduce overall connectivity.

---

## Conclusions

1. Betweenness centrality identifies nodes that act as bridges within the network.

2. Important bridge nodes do not necessarily have high degree.

3. Nodes 1085, 698, 567, and 58 demonstrate that structural position can be more important than the number of direct connections.

4. Node 107 consistently appears as the most influential node under multiple measures.

5. Different notions of influence capture different aspects of network structure. Degree, reachability, closeness centrality, and betweenness centrality should be viewed as complementary measures rather than competing ones.