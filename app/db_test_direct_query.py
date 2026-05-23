from sqlalchemy import text

from db_sql_direct_exec import sql_create_query_executor as sql_create
from db_sql_direct_exec import sql_select_query_executor as sql_select
from db_sql_direct_exec import sql_insert_query_executor as sql_insert


def test_create(conn):
    # Create Table query
    create_table_query = text("""
            CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE
            )
            """)
    result = sql_create(conn, create_table_query)
    print(result)


def test_insert(conn):
    # Insert data query
    insert_query_columns = text("""
            INSERT INTO users (name, email) VALUES (:name, :email)
            """)
    insert_query_values = [
        {"name": "shivam", "email": "shivam@example.com"},
        {"name": "dhruv", "email": "dhruv@example.com"},
    ]

    result = sql_insert(conn, insert_query_columns, insert_query_values)
    print(result)


def test_select(conn):
    # Select data query
    select_query = text("""
            SELECT * FROM users
            """)
    result = sql_select(conn, select_query)
    print(result)
