import streamlit as st

st.set_page_config(
    page_title="Graph Representations Lab",
    layout="wide"
)

st.title("Graph Representations Lab")

st.markdown("""
This lab explores how different graph representations
influence computation.

You will work with:

- Edge Tables
- Adjacency Lists
- Adjacency Matrices
- Breadth-First Search (BFS)
- Real-world social-network data
- Representation tradeoffs
""")

st.info("""
Suggested order:

1. Graph Representations Using Small Graphs
2. Reachability and Breadth-First Search
3. Exploring a Real-World Graph
4. Representation Tradeoffs
5. Independent Graph Investigation
""")

st.success("""
Central Idea:

The same graph can be represented in multiple ways.

The choice of representation affects how efficiently
different questions can be answered.
""")