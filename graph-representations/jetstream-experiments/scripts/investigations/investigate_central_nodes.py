from pathlib import Path
import networkx as nx

from scripts.utilities.graph_utils import (
    load_graph,
    graph_stats,
    nodes_within_k_hops
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
# Build NetworkX graph
#

G = nx.Graph()

for _, row in edge_df.iterrows():
    G.add_edge(
        row["Node1"],
        row["Node2"]
    )

#
# Closeness Centrality
#

print()
print("Computing closeness centrality...")
print()

closeness = nx.closeness_centrality(G)

#
# Build comparison table
#

results = []

for node in nodes:

    reachability_3 = len(
        nodes_within_k_hops(
            adj,
            node,
            3
        )
    )

    results.append(
        (
            node,
            degrees[node],
            reachability_3,
            closeness[node]
        )
    )

#
# Top Degree Nodes
#

top_degree = sorted(
    results,
    key=lambda x: x[1],
    reverse=True
)[:10]

#
# Top Reachability Nodes
#

top_reachability = sorted(
    results,
    key=lambda x: x[2],
    reverse=True
)[:10]

#
# Top Closeness Nodes
#

top_closeness = sorted(
    results,
    key=lambda x: x[3],
    reverse=True
)[:10]

print("=" * 70)
print("TOP 10 BY DEGREE")
print("=" * 70)

for rank, (
    node,
    degree,
    reachability,
    close
) in enumerate(
    top_degree,
    start=1
):
    print(
        f"{rank:2}. "
        f"Node {node:<6} "
        f"Degree={degree:<5} "
        f"Reach3={reachability:<5} "
        f"Closeness={close:.6f}"
    )

print()
print("=" * 70)
print("TOP 10 BY 3-HOP REACHABILITY")
print("=" * 70)

for rank, (
    node,
    degree,
    reachability,
    close
) in enumerate(
    top_reachability,
    start=1
):
    print(
        f"{rank:2}. "
        f"Node {node:<6} "
        f"Degree={degree:<5} "
        f"Reach3={reachability:<5} "
        f"Closeness={close:.6f}"
    )

print()
print("=" * 70)
print("TOP 10 BY CLOSENESS CENTRALITY")
print("=" * 70)

for rank, (
    node,
    degree,
    reachability,
    close
) in enumerate(
    top_closeness,
    start=1
):
    print(
        f"{rank:2}. "
        f"Node {node:<6} "
        f"Degree={degree:<5} "
        f"Reach3={reachability:<5} "
        f"Closeness={close:.6f}"
    )
