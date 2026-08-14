import duckdb

def create_connection(edge_df):
    conn = duckdb.connect()
    conn.register("EdgeTable", edge_df)
    return conn

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

