from pathlib import Path

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
# Choose candidate influencer nodes.
# Top degree nodes from previous analysis.
#

candidate_nodes = [
    "107",
    "1684",
    "1912",
    "3437",
    "0"
]

num_nodes = len(nodes)

print()
print("INFLUENCER ANALYSIS")
print("=" * 70)

print()
print(
    f"Graph Size: {num_nodes} nodes"
)

for node in candidate_nodes:

    degree = len(adj[node])

    print()
    print("-" * 70)
    print(
        f"Node {node}"
    )
    print(
        f"Degree: {degree}"
    )

    for k in [1, 2, 3]:

        reachable = (
            nodes_within_k_hops(
                adj,
                node,
                k
            )
        )

        reachable_count = len(
            reachable
        )

        percentage = (
            100 *
            reachable_count /
            num_nodes
        )

        print(
            f"Reachable within "
            f"{k} hops: "
            f"{reachable_count} "
            f"({percentage:.2f}%)"
        )

print()
print("=" * 70)
print("RANKING OF SELECTED HIGH-DEGREE NODES BY 3-HOP REACHABILITY")
print("=" * 70)

ranking = []

for node in candidate_nodes:

    reachable = (
        nodes_within_k_hops(
            adj,
            node,
            3
        )
    )

    ranking.append(
        (
            node,
            len(reachable),
            len(adj[node])
        )
    )

ranking.sort(
    key=lambda x: x[1],
    reverse=True
)

for rank, (
    node,
    reachable,
    degree
) in enumerate(
    ranking,
    start=1
):
    print(
        f"{rank}. "
        f"Node {node:<6} "
        f"Degree={degree:<5} "
        f"3-Hop Reachability={reachable}"
    )
