from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from db_sql_direct_exec import sql_query_executor as sql_exec
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
    result = sql_exec(conn, create_table_query)
    conn.commit()
    print(result)

    # #Insert data query
    # insert_data_query = """
    #         INSERT INTO users (name, email) VALUES ('John Doe', 'john.doe@example.com')
    #         """
    # result = sql_exec(conn, insert_data_query)
    # print(result)
