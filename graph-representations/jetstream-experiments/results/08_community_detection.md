# Investigation 4: Community Detection

## Dataset

Facebook Graph

- Nodes: 4039
- Edges: 88234

---

## Goal

This investigation explores whether the Facebook graph contains groups of nodes that are more densely connected to one another than to the rest of the graph.

Such groups are called **communities**.

---

## Definition

A community is a set of nodes that:

- have many connections within the group, and
- have relatively fewer connections to nodes outside the group.

In a social network, communities may correspond to:

- friend groups
- organizations
- classrooms
- research groups
- clubs

---

## Algorithm

We used NetworkX's **Greedy Modularity Community Detection** algorithm.

The algorithm attempts to maximize a measure called **modularity**.

Intuitively, modularity measures how much more densely connected the communities are compared to what would be expected in a random graph.

---

## Results

Number of Communities: 16

## Community Sizes

The following table displays the detected community sizes (up to 20 communities).

| Rank | Community Size |
|------|---------------:|
| 1 | 1031 |
| 2 | 739 |
| 3 | 547 |
| 4 | 542 |
| 5 | 357 |
| 6 | 220 |
| 7 | 208 |
| 8 | 206 |
| 9 | 59 |
| 10 | 49 |
| 11 | 25 |
| 12 | 22 |
| 13 | 19 |
| 14 | 6 |
| 15 | 6 |
| 16 | 3 |

---

## Community Containing Node 107

Node 107 belongs to Community 1.

Community Size: 1031

---

## Observations

1. The graph was divided into 16 communities.

2. Community sizes vary substantially.

3. The largest community contains 1031 nodes, approximately one quarter of the graph.

4. Several large communities exist, suggesting that the graph contains multiple densely connected regions.

5. Node 107, which ranked highly in degree, reachability, and closeness centrality, belongs to the largest community.

6. The results suggest that highly influential nodes may play important roles within large communities.

---

## Questions for Further Investigation

1. Are the highest-degree nodes concentrated in the same community?

2. Which communities contain the most influential nodes?

3. Which nodes connect different communities?

4. Are there nodes that act as bridges between communities?

These questions motivate the study of betweenness centrality and bridge nodes.