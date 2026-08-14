from pathlib import Path

from scripts.utilities.graph_utils import (
    load_graph,
    build_adjacency_matrix,
    benchmark,
    print_stats,
    relative_speed
)

from scripts.utilities.duckdb_utils import create_connection

from scripts.utilities.graph_utils import DATA_FILE

def adjacency_list_connected_to_all(
    adj,
    selected_nodes
):
    common = set(adj[selected_nodes[0]])

    for node in selected_nodes[1:]:
        common &= set(adj[node])

    return common


def adjacency_matrix_connected_to_all(
    matrix,
    nodes,
    selected_nodes
):
    result = []

    for candidate in nodes:

        connected_to_all = True

        for selected in selected_nodes:

            if matrix[selected][candidate] == 0:
                connected_to_all = False
                break

        if connected_to_all:
            result.append(candidate)

    return result


def sql_connected_to_all(
    conn,
    selected_nodes
):
    node_list = ",".join(
        f"'{node}'"
        for node in selected_nodes
    )

    sql = f"""
    SELECT neighbor
    FROM
    (
        SELECT Node2 AS neighbor,
               Node1 AS selected_node
        FROM EdgeTable
        WHERE Node1 IN ({node_list})

        UNION ALL

        SELECT Node1 AS neighbor,
               Node2 AS selected_node
        FROM EdgeTable
        WHERE Node2 IN ({node_list})
    )
    GROUP BY neighbor
    HAVING COUNT(
        DISTINCT selected_node
    ) = {len(selected_nodes)}
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
# Experiment setup
#

selected_nodes = [
    "0",
    "1"
]

#
# Run benchmarks
#

list_stats = benchmark(
    adjacency_list_connected_to_all,
    adj,
    selected_nodes
)

matrix_stats = benchmark(
    adjacency_matrix_connected_to_all,
    matrix,
    nodes,
    selected_nodes
)

sql_stats = benchmark(
    sql_connected_to_all,
    conn,
    selected_nodes
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

result = adjacency_list_connected_to_all(
    adj,
    selected_nodes
)

print(
    "Nodes Connected To All Selected Nodes:",
    len(result)
)