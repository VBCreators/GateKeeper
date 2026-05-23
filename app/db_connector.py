from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from db_sql_direct_exec import sql_create_query_executor as sql_create
from db_sql_direct_exec import sql_insert_query_executor as sql_insert

import os

load_dotenv()

username = os.getenv("db_user")
password = os.getenv("db_password")
host = os.getenv("db_host")
port = os.getenv("db_port")
database = os.getenv("db_name")

# postgresql+psycopg2://username:password@host:port/database
# echo=True --> prints all SQL statements

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}", echo=True
)
with engine.connect() as conn:
    # Create Table query
    create_table_query = text("""
            CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE
            )
            """)
    result = sql_create(conn, create_table_query)
    conn.commit()
    print(result)

    # Insert data query
    insert_query_columns = text("""
            INSERT INTO users (name, email) VALUES (:name, :email)
            """)
    insert_query_values = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"},
    ]

    result = sql_insert(conn, insert_query_columns, insert_query_values)

    print(result)
