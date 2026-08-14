import networkx as nx

from scripts.utilities.graph_utils import (
    DATA_FILE,
    load_graph
)

#
# Load graph
#

edge_df, nodes, adj = load_graph(
    DATA_FILE
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

print()
print("BRIDGE NODE ANALYSIS")
print("=" * 70)

print()
print("Computing betweenness centrality...")
print()

betweenness = nx.betweenness_centrality(
    G
)

top10 = sorted(
    betweenness.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]

print("Top 10 Bridge Nodes")
print("-" * 70)

for rank, (node, score) in enumerate(
    top10,
    start=1
):

    print(
        f"{rank:2}. "
        f"Node {node:<6} "
        f"Degree={len(adj[node]):<5} "
        f"Betweenness={score:.6f}"
    )

