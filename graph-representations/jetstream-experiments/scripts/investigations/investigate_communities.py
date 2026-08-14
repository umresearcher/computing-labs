from pathlib import Path
import networkx as nx

from scripts.utilities.graph_utils import (
    load_graph
)

from scripts.utilities.graph_utils import DATA_FILE

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
print("COMMUNITY DETECTION")
print("=" * 70)

print()
print("Computing communities...")
print()

communities = list(
    nx.community.greedy_modularity_communities(
        G
    )
)

print(
    f"Number of Communities: "
    f"{len(communities)}"
)

print()

sizes = sorted(
    [len(c) for c in communities],
    reverse=True
)

MAX_COMMUNITIES_TO_SHOW = 20

print()
print(
    f"Displaying up to {MAX_COMMUNITIES_TO_SHOW} Largest Community Sizes"
)

print("-" * 70)

for i, size in enumerate(
    sizes[:MAX_COMMUNITIES_TO_SHOW],
    start=1
):
    print(
        f"{i:2}. {size}"
    )

#
# Community containing node 107
#

for i, community in enumerate(
    communities,
    start=1
):
    if "107" in community:

        print()
        print(
            "Node 107 belongs to "
            f"Community {i}"
        )

        print(
            f"Community Size: "
            f"{len(community)}"
        )

        break