def sql_query_executor(conn, query):
    result = conn.execute(query)
    if result.returns_rows:
        return result.fetchall()
    else:
        return "Query executed successfully but no rows returned."
