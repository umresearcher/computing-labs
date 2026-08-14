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
print("SMALL-WORLD ANALYSIS")
print("=" * 70)

print()

print(
    "Connected Components:",
    nx.number_connected_components(G)
)

largest_component = max(
    nx.connected_components(G),
    key=len
)

largest_subgraph = G.subgraph(
    largest_component
).copy()

print(
    "Largest Component Size:",
    len(largest_component)
)

print()
print(
    "Computing graph diameter..."
)

diameter = nx.diameter(
    largest_subgraph
)

print(
    "Diameter:",
    diameter
)

print()
print(
    "Computing average shortest path length..."
)

avg_path = nx.average_shortest_path_length(
    largest_subgraph
)

print(
    f"Average Shortest Path Length: "
    f"{avg_path:.3f}"
)

eccentricities = nx.eccentricity(
    largest_subgraph
)

radius = min(
    eccentricities.values()
)

diameter = max(
    eccentricities.values()
)

print()
print("Radius:", radius)

print(
    "Diameter:",
    diameter
)

#
# Lowest eccentricities
#

lowest = sorted(
    eccentricities.items(),
    key=lambda x: x[1]
)[:5]

print()
print("Five Nodes with Lowest Eccentricity")
print("-" * 70)

for rank, (node, ecc) in enumerate(
    lowest,
    start=1
):
    print(
        f"{rank}. "
        f"Node {node:<6} "
        f"Eccentricity={ecc}"
    )

#
# Highest eccentricities
#

highest = sorted(
    eccentricities.items(),
    key=lambda x: x[1],
    reverse=True
)[:5]

print()
print("Five Nodes with Highest Eccentricity")
print("-" * 70)

for rank, (node, ecc) in enumerate(
    highest,
    start=1
):
    print(
        f"{rank}. "
        f"Node {node:<6} "
        f"Eccentricity={ecc}"
    )
