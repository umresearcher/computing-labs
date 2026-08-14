# Investigation 2: Do High-Degree Nodes Have Greater Influence?

## Dataset

Facebook Graph

- Nodes: 4039
- Edges: 88234

---

## Candidate Nodes

The investigation considered several highly connected nodes identified during the degree analysis.

| Node | Degree |
|--------|--------:|
| 107 | 1045 |
| 1684 | 792 |
| 1912 | 755 |
| 3437 | 547 |
| 0 | 347 |

---

## Reachability

### Node 107

| Hops | Reachable Nodes | Percentage of Graph |
|------|------:|------:|
| 1 | 1046 | 25.90% |
| 2 | 2687 | 66.53% |
| 3 | 3780 | 93.59% |

### Node 1684

| Hops | Reachable Nodes | Percentage of Graph |
|------|------:|------:|
| 1 | 793 | 19.63% |
| 2 | 1831 | 45.33% |
| 3 | 3327 | 82.37% |

### Node 1912

| Hops | Reachable Nodes | Percentage of Graph |
|------|------:|------:|
| 1 | 756 | 18.72% |
| 2 | 1003 | 24.83% |
| 3 | 3238 | 80.17% |

### Node 3437

| Hops | Reachable Nodes | Percentage of Graph |
|------|------:|------:|
| 1 | 548 | 13.57% |
| 2 | 703 | 17.41% |
| 3 | 2116 | 52.39% |

### Node 0

| Hops | Reachable Nodes | Percentage of Graph |
|------|------:|------:|
| 1 | 348 | 8.62% |
| 2 | 1519 | 37.61% |
| 3 | 3261 | 80.74% |

---

## Ranking of selected high-degree nodes by 3-Hop Reachability

The nodes were selected from the highest-degree nodes identified during the degree analysis. The purpose was to determine whether higher degree corresponds to greater reachability.

| Rank | Node | Degree | Reachable Within 3 Hops |
|------|------|--------:|--------:|
| 1 | 107 | 1045 | 3780 |
| 2 | 1684 | 792 | 3327 |
| 3 | 0 | 347 | 3261 |
| 4 | 1912 | 755 | 3238 |
| 5 | 3437 | 547 | 2116 |

---

## Observations

1. Node 107 was both the highest-degree node and the node with the greatest 3-hop reachability.

2. Degree and influence were related but not identical.

3. Node 0 demonstrated that a node can have a moderate degree while still reaching a large fraction of the graph within a small number of hops.

4. Node 3437 had a relatively large degree but substantially lower reachability than the other highly connected nodes.

5. Reachability may provide a broader view of influence than degree alone because it considers indirect connections in addition to direct neighbors.