import streamlit as st
import pandas as pd
import graphviz

st.set_page_config(
    page_title="Graph Representations Lab",
    layout="wide"
)

st.title("1. Explore Graph Representations Using Small Graphs")

#st.title("Graph Representations Lab")

st.markdown("""
This activity explores how the same graph can be represented in different ways.

We will use:

- An edge table (database representation)
- An adjacency list
- An adjacency matrix

and answer the same questions using each representation.
""")

# --------------------------------------------------
# Toy Graph
# --------------------------------------------------

edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("B", "D"),
    ("C", "D"),
    ("D", "E")
]

nodes = sorted(
    set([u for u, v in edges] + [v for u, v in edges])
)

# --------------------------------------------------
# Edge Table
# --------------------------------------------------

edge_df = pd.DataFrame(
    edges,
    columns=["Node1", "Node2"]
)

# --------------------------------------------------
# Adjacency List
# --------------------------------------------------

adj = {node: [] for node in nodes}

for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

for node in nodes:
    adj[node] = sorted(adj[node])

# --------------------------------------------------
# Adjacency Matrix
# --------------------------------------------------

matrix = pd.DataFrame(
    "0",
    index=nodes,
    columns=nodes
)

for u, v in edges:
    matrix.loc[u, v] = "1"
    matrix.loc[v, u] = "1"

# --------------------------------------------------
# Row 1
# --------------------------------------------------

st.header("Graph and Edge Table")

col1, col2 = st.columns([1, 1])

with col1:

    st.subheader("Graph")

    try:
        g = graphviz.Graph(format="png")

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
            g.node(str(n))

        for u, v in edges:
            g.edge(
                str(u),
                str(v)
            )

        st.graphviz_chart(
            g,
            use_container_width=False
        )

    except Exception:
        st.error("Unable to display graph.")

with col2:

    st.subheader("Database Representation")

    st.info(
        """
        A graph can be stored in a database as a two-column edge table.

        For an undirected graph, an edge such as **(A,B)**
        may be stored as either **(A,B)** or **(B,A)**.
        """
    )

    st.dataframe(
        edge_df,
        hide_index=True,
        use_container_width=True
    )

# --------------------------------------------------
# Row 2
# --------------------------------------------------

st.header("Adjacency List and Adjacency Matrix")

col3, col4 = st.columns([1, 1])

with col3:

    st.subheader("Adjacency List")

    st.info(
        "Notation: adj[x] denotes the adjacency list of node x."
    )

    adj_rows = []

    for node in nodes:
        adj_rows.append(
            {
                "Node": node,
                "List of Neighbors":
                    " -> ".join(adj[node])
            }
        )

    st.dataframe(
        pd.DataFrame(adj_rows),
        hide_index=True,
        use_container_width=True
    )

with col4:

    st.subheader("Adjacency Matrix")

    st.info(
        "Notation: matrix[x,y] = 1 if an edge exists between x and y."
    )

    st.dataframe(
        matrix,
        use_container_width=True
    )

# --------------------------------------------------
# Neighborhood Exploration
# --------------------------------------------------

st.divider()

st.header("Neighborhood Exploration")

col5, col6 = st.columns([1, 1])

with col6:

    selected_node = st.selectbox(
        "Select a node",
        nodes
    )

    neighbors = adj[selected_node]

    st.success(
        f"Neighbors of {selected_node}: "
        f"{', '.join(neighbors)}"
    )

    st.info(
        f"Degree of {selected_node}: "
        f"{len(neighbors)}"
    )

with col5:

    g = graphviz.Graph(format="png")

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

        if n == selected_node:

            g.node(
                n,
                style="filled",
                fillcolor="red",
                fontcolor="white"
            )

        elif n in neighbors:

            g.node(
                n,
                style="filled",
                fillcolor="lightgreen"
            )

        else:

            g.node(n)

    for u, v in edges:
        g.edge(u, v)

    st.graphviz_chart(
        g,
        use_container_width=False
    )

# --------------------------------------------------
# Representation Comparison
# --------------------------------------------------

col5, col6, col7 = st.columns(3)

with col5:

    st.subheader("SQL")

    sql_text = f"""
SELECT node2
FROM EdgeTable
WHERE node1 = '{selected_node}'

UNION

SELECT node1
FROM EdgeTable
WHERE node2 = '{selected_node}';
"""

    st.code(
        sql_text.strip(),
        language="sql"
    )


with col6:

    st.subheader("Adjacency List")

    adj_text = f"""
nbrs = []

for nbr in adj["{selected_node}"]:
    nbrs.append(nbr)
"""

    st.code(
        adj_text.strip(),
        language="python"
    )


with col7:

    st.subheader("Adjacency Matrix")

    matrix_text = f"""
nbrs = []

for node in nodes:
    if matrix.loc["{selected_node}", node] == 1:
        nbrs.append(node)
"""

    st.code(
        matrix_text.strip(),
        language="python"
    )

st.divider()

st.subheader("Running Time Discussion")

col8, col9, col10 = st.columns(3)

with col8:

    st.info("""
**SQL Edge Table**

Without indexes, we may need to examine every edge in the table.

Running Time: **O(E)**

where **E** is the number of edges.
""")

with col9:

    st.info(f"""
**Adjacency List**

The neighbors of {selected_node} are stored directly in its adjacency list.

Running Time: **O(degree({selected_node}))**

where degree(x) is the number of neighbors of x.
""")

with col10:

    st.info("""
    **Adjacency Matrix**

    We loop through all **V** nodes in the graph.

    For each node, we check one cell in the adjacency matrix to determine
    whether an edge exists between the selected node and that node.

    Accessing a particular entry in a 2-D array (or matrix) takes **O(1)**
    time.

    Since we perform **V** such checks, the total running time is:

    **O(V)**

    where **V** is the number of nodes.
    """)

st.success("""
Notice that all three representations answer the same question.

However, the amount of work required can be different.

A good data representation can make a computation much more efficient.
""")
