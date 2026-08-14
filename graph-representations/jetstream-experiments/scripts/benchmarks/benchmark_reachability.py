from pathlib import Path

from scripts.utilities.graph_utils import (
    load_graph,
    build_adjacency_matrix,
    nodes_within_k_hops,
    nodes_within_k_hops_matrix,
    generate_reachability_sql,
    benchmark,
    benchmark_sql,
    print_stats,
    relative_speed
)

from scripts.utilities.duckdb_utils import create_connection

from scripts.utilities.graph_utils import DATA_FILE

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
# Experiment parameters
#

start_node = "107"

for k in range(1, 6):

    print()
    print("=" * 60)
    print(f"Reachability Within {k} Hops")
    print("=" * 60)

    #
    # Adjacency List
    #

    list_stats = benchmark(
        nodes_within_k_hops,
        adj,
        start_node,
        k
    )

    #
    # Adjacency Matrix
    #

    matrix_stats = benchmark(
        nodes_within_k_hops_matrix,
        matrix,
        nodes,
        start_node,
        k
    )

    #
    # SQL
    #

    sql = generate_reachability_sql(
        start_node,
        k
    )

    sql_stats = benchmark_sql(
        conn,
        sql
    )

    #
    # Print Results
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

    #
    # Reachable node counts
    #

    reachable_list = nodes_within_k_hops(
        adj,
        start_node,
        k
    )

    print()

    print(
        f"Reachable Nodes Within {k} Hops: "
        f"{len(reachable_list)}"
    )