from pathlib import Path

from scripts.utilities.graph_utils import (
    load_graph,
    build_adjacency_matrix,
    benchmark,
    print_stats,
    relative_speed
)

from scripts.utilities.graph_utils import DATA_FILE

from scripts.utilities.duckdb_utils import (
    create_connection
)

def adjacency_list_common_neighbors(
    adj,
    node1,
    node2
):
    return set(adj[node1]) & set(adj[node2])


def adjacency_matrix_common_neighbors(
    matrix,
    nodes,
    node1,
    node2
):
    common = []

    for node in nodes:
        if (
            matrix[node1][node] == 1
            and
            matrix[node2][node] == 1
        ):
            common.append(node)

    return common

def sql_common_neighbors(
    conn,
    node1,
    node2
):
    sql = f"""
    (
        SELECT Node2 AS neighbor
        FROM EdgeTable
        WHERE Node1 = '{node1}'

        UNION

        SELECT Node1 AS neighbor
        FROM EdgeTable
        WHERE Node2 = '{node1}'
    )

    INTERSECT

    (
        SELECT Node2 AS neighbor
        FROM EdgeTable
        WHERE Node1 = '{node2}'

        UNION

        SELECT Node1 AS neighbor
        FROM EdgeTable
        WHERE Node2 = '{node2}'
    )
    """

    return conn.execute(sql).fetchall()


#
# Load graph
#

edge_df, nodes, adj = load_graph(
    DATA_FILE
)

matrix = build_adjacency_matrix(
    nodes,
    adj
)

conn = create_connection(
    edge_df
)

#
# Select nodes
#

node1 = "107"
node2 = "1684"

#
# Run benchmarks
#

list_stats = benchmark(
    adjacency_list_common_neighbors,
    adj,
    node1,
    node2
)

matrix_stats = benchmark(
    adjacency_matrix_common_neighbors,
    matrix,
    nodes,
    node1,
    node2
)

sql_stats = benchmark(
    sql_common_neighbors,
    conn,
    node1,
    node2
)

#
# Print results
#

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

print()

print(
    "Number of Common Neighbors:",
    len(
        adjacency_list_common_neighbors(
            adj,
            node1,
            node2
        )
    )
)