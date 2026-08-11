import streamlit as st
import graphviz
from graphutils import nodes_within_k_hops

st.set_page_config(
    page_title="Graph Representations Lab",
    layout="wide"
)

st.title(
    "2. Reachability and Breadth-First Search (BFS)"
)

st.markdown("""
Given a starting node, we often want to know which
other nodes can be reached within a small number
of hops.

We can answer this question using
**Breadth-First Search (BFS)**.
""")


# ---------------------------------------
# Toy Graph
# ---------------------------------------

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D"),
    ("D", "E")
]

nodes = sorted(
    set([u for u, v in edges] +
        [v for u, v in edges])
)

adj = {
    node: []
    for node in nodes
}

for u, v in edges:

    adj[u].append(v)
    adj[v].append(u)


col1, col2 = st.columns([1, 1])


with col2:

    start_node = st.selectbox(
        "Starting Node",
        nodes
    )

    k = st.slider(
        "Maximum Number of Hops",
        min_value=0,
        max_value=4,
        value=0
    )

    reachable = nodes_within_k_hops(
        adj,
        start_node,
        k
    )

    st.success(
        f"Reachable Nodes: "
        f"{', '.join(sorted(reachable.keys()))}"
    )

    st.info(
        f"{len(reachable)} nodes are reachable "
        f"within {k} hops."
    )

    st.markdown("### BFS Levels")
    for distance in range(k + 1):
        nodes_at_distance = sorted(
            node
            for node, d in reachable.items()
            if d == distance
        )

        st.markdown(
            f"- **Distance {distance}:** "
            f"{', '.join(nodes_at_distance)}"
        )

with col1:

    g = graphviz.Graph(
        format="png"
    )

    g.attr(rankdir="LR")

    g.attr(nodesep="0.3")
    g.attr(ranksep="0.4")

    g.attr(
        "node",
        shape="circle",
        fontsize="12",
        width="0.4",
        height="0.4",
        fixedsize="true"
    )

    for n in nodes:

        if n == start_node:

            g.node(
                n,
                style="filled",
                fillcolor="red",
                fontcolor="white"
            )

        elif n in reachable:

            g.node(
                n,
                style="filled",
                fillcolor="lightgreen"
            )

        else:

            g.node(n)

    for u, v in edges:

        g.edge(
            u,
            v,
            color="gray"
        )

    st.graphviz_chart(
        g,
        use_container_width=False
    )


st.divider()

st.header(
    "How Does BFS Work?"
)

st.code(
"""
# Find all nodes within k hops
# Input Parameters:
#   adj   : adjacency list
#   start : starting node
#   k     : maximum number of hops
# Returns:
#   set of nodes at distance <= k hops from start node

def nodes_within_k_hops(adj, start, k):
    visited = {start}        #visited is the set of nodes visited so far
    queue = [(start, 0)]     #use a queue data structure maintaining nodes seen, but whose edges are not explored.
                             #for each node, record (node, distance form start)
    while queue:             #loop as long as there are still nodes in the queue
        node, dist = queue.pop(0)

        # Stop expanding once we reach k hops
        if dist == k:
            continue

        # Explore all neighbors of the current node
        for nbr in adj[node]:
            if nbr not in visited:
                visited.add(nbr)    #add nbr to visited if not in visited
                queue.append(       #add (nbr, distance from start) to queue
                    (nbr, dist + 1)
                )
    return visited                  #visited is the set of nodes at distance <= k steps from start
""",
language="python"
)

st.info("""
BFS explores the graph level by level.

It first explores nodes 1 hop away,
then 2 hops away,
then 3 hops away, and so on.
""")

st.info("""
BFS visits each node at most once
and each edge at most once.

Running Time: O(V + E)

where V is the number of nodes
and E is the number of edges.
""")