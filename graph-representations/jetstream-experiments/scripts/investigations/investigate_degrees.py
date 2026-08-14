from pathlib import Path
from statistics import median

from scripts.utilities.graph_utils import (
    load_graph,
    graph_stats
)

from scripts.utilities.graph_utils import DATA_FILE

#
# Load graph
#

edge_df, nodes, adj = load_graph(DATA_FILE)

(
    degrees,
    highest_degree_node,
    highest_degree,
    avg_degree
) = graph_stats(
    nodes,
    adj
)

#
# Degree statistics
#

degree_values = list(degrees.values())

median_degree = median(degree_values)

num_degree_gt_100 = sum(
    1
    for d in degree_values
    if d > 100
)

num_degree_eq_1 = sum(
    1
    for d in degree_values
    if d == 1
)

top10 = sorted(
    degrees.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]

#
# Output
#

print()
print("DEGREE ANALYSIS")
print("=" * 60)

print()
print(f"Number of Nodes : {len(nodes)}")
print(f"Number of Edges : {len(edge_df)}")

print()
print(f"Highest Degree Node : {highest_degree_node}")
print(f"Highest Degree      : {highest_degree}")

print()
print(f"Average Degree : {avg_degree:.2f}")
print(f"Median Degree  : {median_degree}")

print()
print(f"Nodes with Degree > 100 : {num_degree_gt_100}")
print(f"Nodes with Degree = 1   : {num_degree_eq_1}")

print()
print("Top 10 Highest-Degree Nodes")
print("-" * 60)

for rank, (node, degree) in enumerate(
    top10,
    start=1
):
    print(
        f"{rank:2}. "
        f"Node {node:<6} "
        f"Degree = {degree}"
    )
