import streamlit as st
import pandas as pd
from pathlib import Path

from graphutils import (
    load_graph,
    graph_stats
)

@st.cache_data
def cached_load_graph(data_file):
    return load_graph(data_file)


@st.cache_data
def cached_graph_stats(nodes, adj):
    return graph_stats(nodes, adj)

st.title(
    "3. Exploring a Real-World Graph"
)

st.markdown("""
In the previous activities, we worked with a small graph that could be
drawn and inspected visually.

Real-world graphs are often much larger. In this activity, we will
explore a social-network graph from the Stanford Network Analysis Platform (SNAP).
""")

st.info("""
Dataset: Facebook Social Network (SNAP)

Nodes: 4,039
Edges: 88,234

Source:
https://snap.stanford.edu/data/egonets-Facebook.html
""")

DATA_FILE = (
    Path(__file__).resolve()
    .parent.parent.parent
    / "datasets"
    / "facebook_combined.txt"
)

with open(DATA_FILE, "rb") as f:

    st.download_button(
        label="Download Dataset",
        data=f,
        file_name="facebook_combined.txt",
        mime="text/plain"
    )

edge_df, nodes, adj = cached_load_graph(DATA_FILE)

(
    degrees,
    highest_degree_node,
    highest_degree,
    avg_degree
) = cached_graph_stats(
    nodes,
    adj
)

st.subheader("Preview of the Dataset")

st.dataframe(
    edge_df.head(20),
    hide_index=True,
    use_container_width=True
)

st.markdown("""
Each row represents an edge in the graph.

For example:

(0,1)

means that nodes 0 and 1 are connected.

The graph is undirected, so the edge could equivalently be written as:

(1,0)
""")

st.subheader("Basic Graph Statistics")

num_edges = len(edge_df)
num_nodes = len(nodes)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Number of Nodes",
        f"{num_nodes:,}"
    )

    st.metric(
        "Number of Edges",
        f"{num_edges:,}"
    )

with col2:

    st.metric(
        "Highest Degree Node",
        highest_degree_node
    )

    st.metric(
        "Highest Degree",
        highest_degree
    )

st.info(
    f"""
Average Degree: {avg_degree:.2f}

For any undirected graph:

Average Degree = (2 × Number of Edges) / Number of Nodes

For this graph:

Average Degree = (2 × {num_edges:,}) / {num_nodes:,}
               = {avg_degree:.2f}
"""
)

st.subheader("Top 10 Highest-Degree Nodes")

top10 = sorted(
    degrees.items(),
    key=lambda x: x[1],
    reverse=True
)[:10]

top10_df = pd.DataFrame(
    top10,
    columns=["Node", "Degree"]
).astype(str)

st.dataframe(
    top10_df,
    hide_index=True,
    use_container_width=True
)

st.subheader("Explore a Node")

selected_node = st.selectbox(
    "Choose a node",
    sorted(nodes, key=int)
)

neighbors = sorted(adj[selected_node])

degree = len(neighbors)

st.metric(
    "Degree",
    degree
)

st.info(
    f"""
Node {selected_node} is connected to
{degree} other nodes.

The degree of a node is the number of
neighbors that it has.
"""
)

st.markdown("### Neighbor List")

MAX_NEIGHBORS_TO_SHOW = 20

if degree <= MAX_NEIGHBORS_TO_SHOW:

    st.write(
        ", ".join(neighbors)
    )

else:

    st.write(
        ", ".join(
            neighbors[:MAX_NEIGHBORS_TO_SHOW]
        )
    )

    st.caption(
        f"Showing the first "
        f"{MAX_NEIGHBORS_TO_SHOW} of "
        f"{degree} neighbors."
    )

st.info(
"""
A node's degree is the number of neighbors it has.

In a social-network graph, nodes with high degrees may be
potential influencers because they are directly connected
to many other nodes.
"""
)

st.subheader("Common Neighbors")

col1, col2 = st.columns(2)

with col1:

    node1 = st.selectbox(
        "First Node",
        sorted(nodes, key=int),
        key="common_neighbors_node1"
    )

with col2:

    node2 = st.selectbox(
        "Second Node",
        sorted(nodes, key=int),
        key="common_neighbors_node2"
    )

common_neighbors = sorted(
    set(adj[node1]) &
    set(adj[node2])
)

st.metric(
    "Number of Common Neighbors",
    len(common_neighbors)
)

if len(common_neighbors) == 0:

    st.info(
        f"Nodes {node1} and {node2} do not have any common neighbors."
    )

else:

    MAX_COMMON_TO_SHOW = 20

    st.markdown("### Common Neighbor List")

    if len(common_neighbors) <= MAX_COMMON_TO_SHOW:

        st.write(
            ", ".join(common_neighbors)
        )

    else:

        st.write(
            ", ".join(
                common_neighbors[:MAX_COMMON_TO_SHOW]
            )
        )

        st.caption(
            f"Showing the first "
            f"{MAX_COMMON_TO_SHOW} of "
            f"{len(common_neighbors)} common neighbors."
        )

st.info(
"""
Common neighbors are nodes that are connected
to both selected nodes.

In a social network, a large number of common
neighbors may indicate that two users belong to
similar communities or groups.
"""
)

st.subheader("Connected to All")

selected_nodes = st.multiselect(
    "Select 2 to 5 Nodes",
    sorted(nodes, key=int),
    default=["0", "1"],
    max_selections=5
)

if len(selected_nodes) < 2:

    st.info(
        "Select at least two nodes."
    )

else:

    connected_to_all = set(
        adj[selected_nodes[0]]
    )

    for node in selected_nodes[1:]:

        connected_to_all &= set(
            adj[node]
        )

    connected_to_all = sorted(
        connected_to_all
    )

    st.metric(
        "Nodes Connected to All Selected Nodes",
        len(connected_to_all)
    )

    if len(connected_to_all) == 0:

        st.info(
            "No nodes are connected to all selected nodes."
        )

    else:

        MAX_TO_SHOW = 20

        st.markdown(
            "### Connected-to-All Node List"
        )

        if len(connected_to_all) <= MAX_TO_SHOW:

            st.write(
                ", ".join(
                    connected_to_all
                )
            )

        else:

            st.write(
                ", ".join(
                    connected_to_all[:MAX_TO_SHOW]
                )
            )

            st.caption(
                f"Showing the first "
                f"{MAX_TO_SHOW} of "
                f"{len(connected_to_all)} nodes."
            )

    st.info(
        """
Nodes connected to all selected nodes can be found
by intersecting the neighbor lists of the selected
nodes.

This operation will later be used to compare graph
representations and SQL-based representations.
"""
    )
