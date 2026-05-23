from sqlalchemy import create_engine, text
from dotenv import load_dotenv
from db_test_direct_query import test_create, test_insert, test_select


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
    test_create(conn)
    test_insert(conn)
    test_select(conn)
