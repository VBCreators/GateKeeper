def sql_create_query_executor(conn, query):
    result = conn.execute(query)
    try:
        if result.returns_rows:
            return result.fetchall()
        else:
            return "Query executed successfully but no rows returned."
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


def sql_insert_query_executor(conn, query, values):
    print("executing query:", query)
    print("with values:", values)

    try:
        result = conn.execute(query, values)
        if result.returns_rows:
            conn.commit()
            return result.fetchall()
        else:
            conn.commit()
            return "Query executed successfully but no rows returned."
    except Exception as e:
        print(f"Error occurred: {e}")
        return None
