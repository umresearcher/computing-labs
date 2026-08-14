from collections import deque
import pandas as pd
import time
from statistics import mean, median, stdev
from pathlib import Path

PROJECT_ROOT = (
    Path(__file__).resolve()
    .parent.parent.parent
)

DATA_FILE = (
    PROJECT_ROOT
    / "data"
    / "facebook_combined.txt"
)

def load_graph(data_file):
    edge_df = pd.read_csv(
        data_file,
        sep=" ",
        names=["Node1", "Node2"]
    )
    edge_df = edge_df.astype(str)
    nodes = (
        set(edge_df["Node1"])
        | set(edge_df["Node2"])
    )
    adj = {
        node: []
        for node in nodes
    }
    for _, row in edge_df.iterrows():

        u = row["Node1"]
        v = row["Node2"]

        adj[u].append(v)
        adj[v].append(u)
    return edge_df, nodes, adj

def graph_stats(nodes, adj):
    num_nodes = len(nodes)
    degrees = {
        node: len(adj[node])
        for node in nodes
    }
    highest_degree_node = max(
        degrees,
        key=degrees.get
    )
    highest_degree = degrees[
        highest_degree_node
    ]
    avg_degree = (
        sum(degrees.values())
        / num_nodes
    )

    return (
        degrees,
        highest_degree_node,
        highest_degree,
        avg_degree
    )

#BFS to return nodes at distance <= k from start, along with distance
def nodes_within_k_hops(adj, start, k):
    distances = {start: 0}
    q = deque([(start, 0)])
    while q:
        node, dist = q.popleft()
        if dist == k:
            continue
        for nbr in adj[node]:
            if nbr not in distances:
                distances[nbr] = dist + 1
                q.append(
                    (nbr, dist + 1)
                )
    return distances

def build_adjacency_matrix(nodes, adj):
    sorted_nodes = sorted(
        nodes,
        key=int
    )
    matrix = {}
    for node in sorted_nodes:
        matrix[node] = {}
        nbrs = set(adj[node])
        for other in sorted_nodes:
            matrix[node][other] = (
                1
                if other in nbrs
                else 0
            )
    return matrix

def nodes_within_k_hops_matrix(
    matrix,
    nodes,
    start,
    k
):
    distances = {
        start: 0
    }
    q = deque(
        [(start, 0)]
    )
    while q:
        current_node, dist = q.popleft()
        if dist == k:
            continue
        for node in nodes:
            if (
                matrix[current_node][node] == 1
                and
                node not in distances
            ):
                distances[node] = dist + 1
                q.append(
                    (node, dist + 1)
                )
    return distances

def generate_reachability_sql(start_node, k):

    sql = "WITH\n\n"

    # Hop0
    sql += f"""
Hop0 AS (

    SELECT '{start_node}' AS node

)
"""

    # Hop1
    sql += f""",

Hop1 AS (

    SELECT node2 AS node
    FROM EdgeTable
    WHERE node1 = '{start_node}'

    UNION

    SELECT node1 AS node
    FROM EdgeTable
    WHERE node2 = '{start_node}'

)
"""

    # Hop2 ... Hopk
    for hop in range(2, k + 1):

        prev = hop - 1

        sql += f""",

Hop{hop} AS (

    SELECT e.node2 AS node
    FROM Hop{prev} h
         JOIN EdgeTable e
           ON h.node = e.node1

    UNION

    SELECT e.node1 AS node
    FROM Hop{prev} h
         JOIN EdgeTable e
           ON h.node = e.node2

)
"""

    # Return all nodes reachable within k hops
    sql += "\n\nSELECT * FROM Hop0"

    for hop in range(1, k + 1):

        sql += f"""

UNION

SELECT * FROM Hop{hop}
"""

    sql += ";"

    return sql

def measure_time(func, *args):
    start = time.perf_counter()
    result = func(*args)
    end = time.perf_counter()
    return result, end - start

def benchmark(func, *args, repetitions=50):
    times = []

    # warmup run
    func(*args)

    result = None

    for _ in range(repetitions):
        result, elapsed = measure_time(func, *args)
        times.append(elapsed)

    return {
        "result": result,
        "runs": repetitions,
        "mean": mean(times),
        "median": median(times),
        "min": min(times),
        "max": max(times),
        "range": max(times) - min(times),
        "stdev": stdev(times) if len(times) > 1 else 0,
        "raw_times": times
    }

def benchmark_sql(
    conn,
    sql,
    repetitions=50
):
    # warmup run
    conn.execute(sql).df()

    times = []
    result = None

    for _ in range(repetitions):
        start = time.perf_counter()

        result = conn.execute(sql).df()

        end = time.perf_counter()

        times.append(end - start)

    return {
        "result": result,
        "runs": repetitions,
        "mean": mean(times),
        "median": median(times),
        "min": min(times),
        "max": max(times),
        "range": max(times) - min(times),
        "stdev": stdev(times) if len(times) > 1 else 0,
        "raw_times": times
    }

def print_stats(name, stats):
    print()
    print(name)
    print("-" * len(name))
    print(f"Runs   : {stats['runs']}")
    print(f"Median : {stats['median']:.10f}")
    print(f"Mean   : {stats['mean']:.10f}")
    print(f"Min    : {stats['min']:.10f}")
    print(f"Max    : {stats['max']:.10f}")
    print(f"Range  : {stats['range']:.10f}")
    print(f"StdDev : {stats['stdev']:.10f}")

def relative_speed(reference_stats, other_stats):
    return (
        other_stats["median"]
        / reference_stats["median"]
    )

#The following is used in streamlit, but deprecated for our experiments

def average_time(
    func,
    *args,
    repetitions=50
):
    total_time = 0
    result = None
    for _ in range(repetitions):
        result, elapsed = measure_time(
            func,
            *args
        )
        total_time += elapsed
    return result, total_time / repetitions

def average_sql_time(
    conn,
    sql,
    repetitions=50
):
    total_time = 0
    result = None
    for _ in range(repetitions):
        start = time.perf_counter()
        result = conn.execute(sql).df()
        end = time.perf_counter()
        total_time += (end - start)
    return result, total_time / repetitions



