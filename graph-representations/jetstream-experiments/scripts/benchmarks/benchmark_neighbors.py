from scripts.utilities.graph_utils import (
    load_graph,
    build_adjacency_matrix,
    benchmark,
    print_stats,
    relative_speed
)

from scripts.utilities.graph_utils import DATA_FILE

from scripts.utilities.duckdb_utils import (
    create_connection,
    sql_neighbors    
)

def adjacency_list_neighbors(adj, node):
    return adj[node]

def adjacency_matrix_neighbors(
    matrix,
    nodes,
    node
):
    neighbors = []

    for other in nodes:
        if matrix[node][other] == 1:
            neighbors.append(other)

    return neighbors

def sql_neighbors(conn, node):

    sql = f"""
    SELECT Node2 AS neighbor
    FROM EdgeTable
    WHERE Node1 = '{node}'

    UNION

    SELECT Node1 AS neighbor
    FROM EdgeTable
    WHERE Node2 = '{node}'
    """

    return conn.execute(sql).fetchall()

edge_df, nodes, adj = load_graph(
    DATA_FILE
)

matrix = build_adjacency_matrix(
    nodes,
    adj
)

conn = create_connection(edge_df)

node = "107"

list_stats = benchmark(
    adjacency_list_neighbors,
    adj,
    node
)

matrix_stats = benchmark(
    adjacency_matrix_neighbors,
    matrix,
    nodes,
    node
)

sql_stats = benchmark(
    sql_neighbors,
    conn,
    "107"
)

print_stats(
    "Adjacency List",
    list_stats
)

print_stats(
    "Adjacency Matrix",
    matrix_stats
)

print_stats(
    "SQL",
    sql_stats
)

print()
print(
    f"Adjacency Matrix is "
    f"{relative_speed(list_stats, matrix_stats):,.1f}x slower "
    f"than the Adjacency List."
)

print(
    f"SQL is "
    f"{relative_speed(list_stats, sql_stats):,.1f}x slower "
    f"than the Adjacency List."
)

print(
    f"SQL is "
    f"{relative_speed(matrix_stats, sql_stats):,.1f}x slower "
    f"than the Adjacency Matrix."
)