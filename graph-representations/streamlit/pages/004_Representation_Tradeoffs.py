import streamlit as st
import pandas as pd
from pathlib import Path
import duckdb
import time

from graphutils import measure_time, nodes_within_k_hops, nodes_within_k_hops_matrix

from graphutils import (
    load_graph,
    graph_stats,
    build_adjacency_matrix,
    generate_reachability_sql,
    average_time,
    average_sql_time
)

@st.cache_data
def cached_load_graph(data_file):
    return load_graph(data_file)


@st.cache_data
def cached_graph_stats(nodes, adj):
    return graph_stats(nodes, adj)

@st.cache_data
def cached_build_matrix(nodes, adj):
    return build_adjacency_matrix(
        nodes,
        adj
    )

@st.cache_resource
def get_duckdb(edge_df):
    conn = duckdb.connect()
    conn.register(
        "EdgeTable",
        edge_df
    )
    return conn

st.set_page_config(
    page_title="Representation Tradeoffs",
    layout="wide"
)

st.title(
    "4. Representation Tradeoffs"
)

st.markdown("""
In the previous activities, we explored graphs using:

- Edge Tables
- Adjacency Lists
- Adjacency Matrices

In this activity, we will compare these representations.

The goal is not to determine which representation is always best.

Instead, we will see that different representations support
different computations efficiently.
""")

st.info("""
Key Question:

How does the choice of representation affect the amount of work
required to answer a question about a graph?
""")

DATA_FILE = (
    Path(__file__).resolve()
    .parent.parent.parent
    / "datasets"
    / "facebook_combined.txt"
)

edge_df, nodes, adj = cached_load_graph(
    DATA_FILE
)

sorted_nodes = sorted(
    nodes,
    key=int
)

matrix = cached_build_matrix(
    nodes,
    adj
)

conn = get_duckdb(edge_df)

st.header("Question 1: Find the Neighbors of a Node")

selected_node = st.selectbox(
    "Choose a Node",
    sorted(nodes, key=int)
)

st.markdown(
    f"""
Suppose we want to answer the following question:

**Who are the neighbors of node {selected_node}?**
"""
)

col1, col2, col3 = st.columns(3)

with col1:

    st.subheader("Edge Table")

    st.markdown(
        f"""
**Idea**

Find all rows containing **{selected_node}**
(either as `node1` or `node2`) and return
the node at the other end of the edge.
"""
    )

    st.code(
f"""
SELECT node2
FROM EdgeTable
WHERE node1 = '{selected_node}'

UNION

SELECT node1
FROM EdgeTable
WHERE node2 = '{selected_node}';
""",
        language="sql"
    )

    st.info("""
**Running Time**

Without indexes, we may need to examine
all edges in the graph.

Running Time: O(E)

where E is the number of edges.
""")
    
with col2:

    st.subheader("Adjacency List")

    st.markdown(
        f"""
**Idea**

The neighbors of node **{selected_node}**
are stored directly in the adjacency list
`adj["{selected_node}"]`.

Traverse this list and return its elements.
"""
    )

    st.code(
f"""
nbrs = []

for nbr in adj["{selected_node}"]:
    nbrs.append(nbr)
""",
        language="python"
    )

    st.info(
f"""
**Running Time**

If node **{selected_node}** has degree
**degree({selected_node})**, then its
adjacency list contains exactly
**degree({selected_node})** neighbors.

We examine each neighbor once.

Running Time: O(degree({selected_node}))
"""
    )

with col3:

    st.subheader("Adjacency Matrix")

    st.markdown(
        f"""
**Idea**

Traverse the matrix row corresponding to
node **{selected_node}**.

A value of 1 indicates that an edge exists
between **{selected_node}** and the corresponding node.
"""
    )

    st.code(
f"""
nbrs = []

for node in nodes:
    if matrix["{selected_node}"][node] == 1:
        nbrs.append(node)
""",
        language="python"
    )

    st.info("""
**Running Time**

We examine one matrix entry for every node
in the graph.

Accessing a particular entry of a 2-D array
(or matrix) takes O(1) time.

Since we examine V entries, the total
running time is:

O(V)

where V is the number of nodes.
""")

neighbors = sorted(adj[selected_node])

st.markdown("### Result")

st.success(
    ", ".join(neighbors[:20])
)

if len(neighbors) > 20:

    st.caption(
        f"Showing the first 20 of "
        f"{len(neighbors)} neighbors."
    )

st.success("""
Takeaway:

All three representations answer the same question.

As seen above, the amount of work required can be very different.

A good representation can make a computation significantly
more efficient.
""")

st.divider()

st.header("Question 2: Find Common Neighbors")

col1, col2 = st.columns(2)

with col1:

    node1 = st.selectbox(
        "First Node",
        sorted(nodes, key=int),
        key="q2_node1"
    )

with col2:

    node2 = st.selectbox(
        "Second Node",
        sorted(nodes, key=int),
        key="q2_node2"
    )

common_neighbors = sorted(
    set(adj[node1]) &
    set(adj[node2]),
    key=int
)

st.markdown(
    f"""
Suppose we want to answer the following question:

**Which nodes are neighbors of both {node1} and {node2}?**
"""
)

col3, col4, col5 = st.columns(3)

with col3:

    st.subheader("Edge Table")

    st.markdown(
        f"""
**Idea**

Find the neighbors of nodes **{node1}** and
**{node2}** as in Question 1.

Then intersect the two neighbor sets using
the SQL **INTERSECT** operation.
"""
    )

    st.code(
f"""
(   -- find neighbours of {node1} as for Question 1
    SELECT node2 FROM EdgeTable 
    WHERE node1 = '{node1}'
    UNION    
    SELECT node1 FROM EdgeTable 
    WHERE node2 = '{node1}'
)

INTERSECT

(   -- find neighbours of {node2} as for Question 1
    SELECT node2 FROM EdgeTable
    WHERE node1 = '{node2}'
    UNION
    SELECT node1 FROM EdgeTable
    WHERE node2 = '{node2}'
);
""",
        language="sql"
    )

    st.info("""
**Running Time**

Finding the two neighbor sets may require
examining all edges in the table.

We have not included the cost of computing
the intersection itself.

Running Time (without intersection): O(E)

where E is the number of edges.
""")
    
with col4:

    st.subheader("Adjacency List")

    st.markdown(
        f"""
**Idea**

Find the neighbors of nodes **{node1}** and
**{node2}** as in Question 1.

Then intersect the two neighbor sets using
the Python set intersection operator.
"""
    )

    st.code(
f"""
neighbors1 = set(adj["{node1}"])

neighbors2 = set(adj["{node2}"])

common = neighbors1 & neighbors2
""",
        language="python"
    )

    st.info(
f"""
**Running Time**

Finding the two neighbor sets requires
examining the adjacency lists of the
selected nodes.

We have not included the cost of computing
the intersection itself.

Running Time (without intersection):

O(degree({node1}) + degree({node2}))
"""
    )

with col5:

    st.subheader("Adjacency Matrix")

    st.markdown(
        f"""
**Idea**

Traverse the rows corresponding to
nodes **{node1}** and **{node2}**.

A node is a common neighbor if both
adjacency-matrix entries are 1.
"""
    )

    st.code(
f"""
common = []

for node in nodes:

    if (
        matrix["{node1}"][node] == 1
        and
        matrix["{node2}"][node] == 1
    ):
        common.append(node)
""",
        language="python"
    )

    st.info("""
**Running Time**

We examine one matrix entry for every node
in the graph.

Accessing a particular matrix entry takes
O(1) time.

The intersection is incorporated into the
same scan because we check the two matrix
entries simultaneously.

Running Time: O(V)

where V is the number of nodes.
""")

st.markdown("### Result")

st.metric(
    "Number of Common Neighbors",
    len(common_neighbors)
)

MAX_TO_SHOW = 20

if len(common_neighbors) == 0:

    st.info(
        "The selected nodes have no common neighbors."
    )

elif len(common_neighbors) <= MAX_TO_SHOW:

    st.write(
        ", ".join(common_neighbors)
    )

else:

    st.write(
        ", ".join(
            common_neighbors[:MAX_TO_SHOW]
        )
    )

    st.caption(
        f"Showing the first "
        f"{MAX_TO_SHOW} of "
        f"{len(common_neighbors)} common neighbors."
    )

st.success("""
Takeaway:

All three representations answer the same question.

As seen above, different representations perform
different amounts of work to find the common neighbors.

There is no universally best representation; the
appropriate representation depends on the operations
that we need to support efficiently.
""")

st.divider()

st.header("Question 3: Find Nodes Connected to All Selected Nodes")

selected_nodes = st.multiselect(
    "Select 2 to 5 Nodes",
    sorted(nodes, key=int),
    default=["0", "1"],
    max_selections=5
)

if len(selected_nodes) < 2:

    st.info(
        "Please select at least two nodes."
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
        connected_to_all,
        key=int
    )

    st.markdown(
        f"""
Suppose we want to answer the following question:

**Which nodes are connected to all of the following nodes?**

{', '.join(selected_nodes)}
"""
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.subheader("Edge Table")

        st.markdown(
            f"""
        **Idea**

        Find the neighbors of all selected nodes.

        For each neighbor, count how many of the selected
        nodes it is connected to.

        A node is connected to all selected nodes if this
        count equals **{len(selected_nodes)}**.

        The SQL **GROUP BY** and **HAVING** clauses are used
        to perform this counting.
        """
        )

        node_list = ", ".join(
            f"'{node}'"
            for node in selected_nodes
        )

        st.code(
        f"""
SELECT neighbor
FROM
(
    SELECT e.node2 AS neighbor
    FROM EdgeTable e
    WHERE e.node1 IN ({node_list})

    UNION ALL

    SELECT e.node1 AS neighbor
    FROM EdgeTable e
    WHERE e.node2 IN ({node_list})
)
GROUP BY neighbor
HAVING COUNT(*) = {len(selected_nodes)};
        """,
            language="sql"
        )

        st.info(f"""
        **Running Time**

        For each edge, we check whether one endpoint
        belongs to the set of {len(selected_nodes)} selected nodes.

        We have not included the cost of grouping
        and counting.

        Running Time (without grouping):

        O(E × k)

        where

        E = number of edges

        k = number of selected nodes
        """)

    with col2:

        st.subheader("Adjacency List")

        st.markdown(
            """
**Idea**

Find the neighbor list of the selected nodes.

Repeatedly intersect the neighbor sets.

The remaining nodes are connected to all
selected nodes.
"""
        )

        node_strings = [
            f'set(adj["{node}"])'
            for node in selected_nodes
        ]

        code_text = (
            "result = "
            + "\n\n         & ".join(node_strings)
        )

        st.code(
            code_text,
            language="python"
        )

        st.info(
            """
**Running Time**

We examine the adjacency lists of the
selected nodes.

We have not included the cost of computing
the intersections themselves.

Running Time (without intersections):

O(sum of selected node degrees)
"""
        )

    with col3:

        st.subheader("Adjacency Matrix")

        st.markdown(
            """
**Idea**

Traverse every node in the graph.

For each node, check whether it is adjacent
to all selected nodes.

A node is returned only if every matrix
entry examined is 1.
"""
        )

        st.code(
"""
connected = []

for node in nodes:

    is_connected = True

    for selected in selected_nodes:

        if matrix[selected][node] == 0:

            is_connected = False

            break

    if is_connected:

        connected.append(node)
""",
            language="python"
        )

        st.info(
            """
        **Running Time**

        We examine every node in the graph.

        For each node, we check adjacency against
        all selected nodes. This is effectively
        performing the intersection.

        Running Time:

        O(V × k)

        where

        V = number of nodes

        k = number of selected nodes
        """
        )

    st.markdown("### Result")

    st.metric(
        "Nodes Connected to All Selected Nodes",
        len(connected_to_all)
    )

    MAX_TO_SHOW = 20

    if len(connected_to_all) == 0:

        st.info(
            "No nodes are connected to all selected nodes."
        )

    elif len(connected_to_all) <= MAX_TO_SHOW:

        st.write(
            ", ".join(connected_to_all)
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

    st.success(
"""
Takeaway:

This question generalizes Common Neighbors.

Instead of intersecting two neighbor sets,
we intersect several neighbor sets.

As the question becomes more complex,
the choice of graph representation becomes
increasingly important.
"""
    )

st.divider()

st.header("Question 4: Find Nodes Within k Hops")

col1, col2 = st.columns(2)

with col1:

    start_node = st.selectbox(
        "Starting Node",
        sorted(nodes, key=int),
        key="q4_start_node"
    )

with col2:

    k = st.slider(
        "Maximum Number of Hops",
        min_value=0,
        max_value=5,
        value=2,
        key="q4_k"
    )

distances = nodes_within_k_hops(
    adj,
    start_node,
    k
)

reachable = sorted(
    distances.keys(),
    key=int
)

st.markdown(
    f"""
Suppose we want to answer the following question:

**Which nodes are reachable from node {start_node} within {k} hops?**
"""
)

col3, col4, col5 = st.columns(3)

with col3:

    st.subheader("Edge Table")

    st.markdown(
        """
    **Idea**

    The starting node is reachable from itself
    in 0 hops.

    Find the nodes reachable in 1 hop.

    Then use joins to find nodes reachable
    in 2 hops, 3 hops, and so on.

    To find nodes reachable within k hops,
    we combine the results from Hop0, Hop1,
    Hop2, ..., Hopk.

    The amount of work grows rapidly as the
    number of hops increases.
    """
    )

    st.code(
    f"""
WITH

Hop0 AS (    -- Nodes reachable in 0 hops
    SELECT '{start_node}' AS node
),

Hop1 AS (    -- Nodes reachable in 1 hop
    SELECT node2 AS node
    FROM EdgeTable
    WHERE node1 = '{start_node}'

    UNION

    SELECT node1 AS node
    FROM EdgeTable
    WHERE node2 = '{start_node}'
),

Hop2 AS (    -- Nodes reachable in 2 hops
    SELECT e.node2 AS node
    FROM Hop1 h
        JOIN EdgeTable e
        ON h.node = e.node1

    UNION

    SELECT e.node1 AS node
    FROM Hop1 h
        JOIN EdgeTable e
        ON h.node = e.node2
)

-- Nodes reachable within 2 hops

SELECT * FROM Hop0
UNION
SELECT * FROM Hop1
UNION
SELECT * FROM Hop2;
    """,
        language="sql"
    )

    st.info(
"""
**Running Time**

Repeated joins are required to determine
reachability at larger distances.

The amount of work grows rapidly as the
number of hops increases.

For larger values of k, SQL-based
reachability queries may become expensive.
"""
    )

with col4:

    st.subheader("Adjacency List")

    st.markdown(
        """
    **Idea**

    Use Breadth-First Search (BFS).

    Starting from the selected node,
    explore the graph level by level.

    Visit each node at most once.

    The nodes that are visited form the set
    of nodes reachable within k hops.
    """
    )

    st.code(
f"""
reachable = nodes_within_k_hops(
    adj,
    "{start_node}",
    {k}
)
""",
        language="python"
    )

    st.info(
"""
**Running Time**

BFS visits each node at most once
and each edge at most once.

Running Time:

O(V + E)

where

V = number of nodes

E = number of edges
"""
    )

with col5:

    st.subheader("Adjacency Matrix")

    st.markdown(
        """
**Idea**

Use the same Breadth-First Search (BFS)
strategy.

Maintain a frontier (or queue) of nodes
that still need to be explored and a set
of nodes that have already been visited.

Whenever neighbors of a node are needed,
scan the corresponding matrix row.

A full row scan may be required for each
visited node.
"""
    )

    st.code(
"""
visited = {start_node}
frontier = [start_node]

while frontier:

    current_node = frontier.pop(0)

    for node in nodes:

        if (
            matrix[current_node][node] == 1
            and
            node not in visited
        ):

            visited.add(node)
            frontier.append(node)
""",
        language="python"
    )

    st.info(
"""
**Running Time**

BFS visits each node at most once.

For each visited node, we may need to
scan an entire row of the adjacency matrix.

Accessing a matrix entry takes O(1)
time.

Since there are at most V row scans,
each of length V, the running time is:

O(V²)

where

V = number of nodes.
"""
    )

st.markdown("### Result")

st.metric(
    "Reachable Nodes",
    len(reachable)
)

MAX_TO_SHOW = 20

if len(reachable) <= MAX_TO_SHOW:

    st.write(
        ", ".join(reachable)
    )

else:

    st.write(
        ", ".join(
            reachable[:MAX_TO_SHOW]
        )
    )

    st.caption(
        f"Showing the first {MAX_TO_SHOW} "
        f"of {len(reachable)} reachable nodes."
    )

st.success(
"""
Takeaway:

As graph questions become more complex,
the choice of representation becomes
increasingly important.

For multi-hop reachability, graph-oriented
representations support efficient traversal
algorithms such as BFS.

This is one reason why graph representations
are often preferred for reachability and
traversal problems.
"""
)

st.subheader(
    "Observed Performance on the Facebook Graph"
)

st.markdown("""
Select a starting node and compare the running times
for finding nodes reachable within 1, 2, 3, 4, and 5 hops.
""")

experiment_start_node = st.selectbox(
    "Starting Node",
    sorted_nodes,
    index=sorted_nodes.index("107"),
    key="experiment_start_node"
)

if st.button(
    "Run Experiment",
    key="run_experiment"
):

    rows = []

    table_placeholder = st.empty()

    progress_bar = st.progress(0)

    for hop in range(1, 6):

        reachable, adj_time = average_time(
            nodes_within_k_hops,
            adj,
            experiment_start_node,
            hop,
            repetitions=3
        )

        reachable, matrix_time = average_time(
            nodes_within_k_hops_matrix,
            matrix,
            sorted_nodes,
            experiment_start_node,
            hop,
            repetitions=3
        )

        sql = generate_reachability_sql(
            experiment_start_node,
            hop
        )

        result, sql_time = average_sql_time(
            conn,
            sql,
            repetitions=3
        )

        bfs_answer = set(reachable.keys())
        sql_answer = set(
            result["node"].astype(str)
        )
        if bfs_answer != sql_answer:
            st.error(
                f"SQL and BFS disagree for {hop}-hop reachability."
            )
            st.write("BFS:", len(bfs_answer))
            st.write("SQL:", len(sql_answer))
            st.write(
                "Only in BFS:",
                sorted(bfs_answer - sql_answer)[:10]
            )

        rows.append(
            {
                "k-Hop": str(hop),
                "Adj List + BFS":
                    f"{adj_time:.6f} sec",
                "Adj Matrix + BFS":
                    f"{matrix_time:.6f} sec",
                "SQL":
                    f"{sql_time:.6f} sec"
            }
        )

        # Update the table immediately
        table_placeholder.dataframe(
            pd.DataFrame(rows),
            hide_index=True,
            use_container_width=True
        )

        # Update the progress bar
        progress_bar.progress(hop / 5)

    progress_bar.empty()

    st.info("""
    All running times shown above are averages
    over 3 executions of the corresponding
    algorithm or query.

    Averaging helps reduce variability caused
    by background activity and other factors.
    """)

    st.info("""
    The Facebook graph used in this activity is small enough
    to fit entirely in memory.

    As a result, in-memory graph representations such as
    adjacency lists perform very well for this activity.
    
    Database systems become especially valuable when datasets
    grow beyond the memory available on a single machine.

    In addition, modern database systems use optimized query
    execution strategies and specialized internal representations
    to process data efficiently.

    The key lesson is that different representations and systems
    are designed to support different types of computations.
    """)
    
st.markdown("### Reflection")

st.markdown(
"""
Think about the questions explored in this module.

- Which representation would you choose?
- Why would you choose it?
- How did the observed running times influence your decision?

Did any of the measured results surprise you?
"""
)

st.success(
"""
Summary

The same graph can be represented in several ways.

The most important lesson is that there is no
universally best representation.

The choice of representation should be guided by
the operations that must be supported efficiently.
"""
)
