import streamlit as st

st.set_page_config(
    page_title="Independent Graph Investigation",
    layout="wide"
)

st.title(
    "5. Independent Graph Investigation"
)

st.markdown("""
In this activity, you will investigate your own
questions about the Facebook graph.
""")

col1, col2 = st.columns(2)

with col1:
    st.success("""
    Your goal is to:

    • Formulate an interesting question.

    • Choose an appropriate representation.

    • Implement and test a solution.

    • Interpret the results.

    • Reflect on your choices.
    """)

with col2:
    st.info("""
    You may use:

    • SQL on an Edge Table

    • Python with Adjacency Lists

    • Python with Adjacency Matrices

    • AI tools or AI agents

    • Jetstream and other resources approved in class
    """)

st.warning("""
AI-generated code and AI-generated explanations
should be carefully tested and validated before
they are used.
""")

st.header("Suggested Investigation Questions")

st.markdown("""
You may investigate one or more of the following
questions, or propose a question of your own.
""")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### Neighborhoods

• Which node has the largest degree?

• How many nodes have degree greater than 100?

• How many nodes have degree equal to 1?

### Common Neighbors

• Which pair of nodes has the most common neighbors?

• Do highly connected nodes tend to share many neighbors?

### Reachability

• How many nodes are reachable within
  1, 2, 3, 4, or 5 hops?

• What fraction of the graph can be reached
  within 3 hops?
""")

with col2:

    st.markdown("""
### Communities

• Are there groups of nodes that appear to form
  tightly connected communities?

### Central Nodes

• Which nodes appear to be most influential?

• Which nodes can reach many other nodes
  within a small number of hops?

• Which nodes appear near the center of the graph?

### Your Own Question

• Use AI, class discussions, or your own
  curiosity to propose and investigate a
  question of interest.
""")

st.header("Getting Started")

col1, col2 = st.columns(2)

with col1:

    st.subheader("SQL")

    st.markdown("""
    Store the graph as an Edge Table.

    Each row contains the endpoints of one edge.
    """)

    st.code(
"""
CREATE TABLE EdgeTable
(
    node1 INTEGER,
    node2 INTEGER
);
""",
    language="sql"
    )

    st.markdown("""
Import the Facebook dataset into
the EdgeTable table.

You can then write SQL queries to investigate
your question.
""")

with col2:

    st.subheader("Python")

    st.markdown("""
Represent the graph using an adjacency list.
""")

    st.code(
"""
import pandas as pd

# Load the Facebook graph and store it as an edge list.
edge_df = pd.read_csv("facebook_combined.txt",
                      sep=" ",
                      names=["node1", "node2"])
edges = list(zip(edge_df["node1"], edge_df["node2"]))

# Build the adjacency list.
adj = {}
for u, v in edges:
    adj.setdefault(u, []).append(v)
    adj.setdefault(v, []).append(u)
""",
    language="python"
    )

    st.markdown("""
In this representation:

• adj[x] contains the neighbors of x

• The neighbors may not be sorted

• Use sorted(adj[x]) if needed
""")

st.header("Additional Python Tools")

col1, col2 = st.columns(2)

with col1:

    st.subheader("Breadth-First Search (BFS)")

    st.code(
"""
def nodes_within_k_hops(
    adj,
    start,
    k
):
    ...
""",
    language="python"
    )

with col2:

    st.subheader("Adjacency Matrix")

    st.code(
"""
# Assume edges and adj have already been computed.
nodes = set([u for u, v in edges] + [v for u, v in edges])
matrix = {}
for u in nodes:
    # Initialize the entire row to 0
    matrix[u] = {v: 0 for v in nodes}
    
    # Set neighbors to 1
    for nbr in adj[u]:
        matrix[u][nbr] = 1
""",
    language="python"
    )

st.info("""
The code snippets above are intended as starting
points. You may modify them, combine them, or use
AI tools to generate alternative implementations.

Be sure to test and validate your results.
""")

st.header("Using AI")

st.markdown("""
AI tools may help you:

• Formulate a question

• Design an algorithm

• Generate SQL

• Generate Python code

• Interpret results

Remember to validate all AI-generated
code and explanations.
""")

st.header("Using Jetstream")

st.markdown("""
If you would like to run your own Python
programs using Jetstream or other resources
approved in class, please follow the
instructions provided in class.

Jetstream may be useful for:

• Running larger experiments

• Evaluating AI-generated code

• Comparing graph representations

• Measuring performance
""")

st.success("""
You are now ready to investigate your own
questions about the Facebook graph.

Choose a question, select an appropriate
representation, implement a solution,
evaluate the results, and reflect on your
choices.

Good investigations often begin with
simple questions and evolve into more
interesting ones.
""")
