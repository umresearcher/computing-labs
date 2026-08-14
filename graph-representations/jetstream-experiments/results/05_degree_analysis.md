# Investigation 1: Degree Analysis

## Dataset

Facebook Graph

- Nodes: 4039
- Edges: 88234

---

## Degree Statistics

Highest Degree Node: 107

Highest Degree: 1045

Average Degree: 43.69

Median Degree: 25

---

## Degree Distribution Observations

Nodes with Degree > 100: 481

Nodes with Degree = 1: 75

---

## Top 10 Highest-Degree Nodes

| Rank | Node | Degree |
|------|------|---------|
| 1 | 107 | 1045 |
| 2 | 1684 | 792 |
| 3 | 1912 | 755 |
| 4 | 3437 | 547 |
| 5 | 0 | 347 |
| 6 | 2543 | 294 |
| 7 | 2347 | 291 |
| 8 | 1888 | 254 |
| 9 | 1800 | 245 |
| 10 | 1663 | 235 |

---

## Observations

1. Node 107 is the most highly connected node in the graph, with 1045 neighbors.

2. The average degree (43.69) is much larger than the median degree (25), indicating a highly skewed degree distribution.

3. A relatively small number of nodes have extremely high connectivity. There are 481 nodes with degree greater than 100.

4. The graph also contains low-connectivity nodes, including 75 nodes with degree equal to 1.

5. The gap between the average and median degree suggests the presence of hub nodes that are substantially more connected than typical nodes.

6. The Facebook graph appears to exhibit characteristics commonly associated with social networks, in which a small number of highly connected nodes coexist with a much larger number of moderately connected nodes.