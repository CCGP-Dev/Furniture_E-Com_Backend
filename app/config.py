import  os
from dotenv import load_dotenv
load_dotenv()
pg_username = os.getenv("POSTGRES_USERNAME")
pg_password = os.getenv("POSTGRES_PASSWORD")
pg_host = os.getenv("DB_HOST")
pg_port = os.getenv("DB_PORT")
pg_database = os.getenv("POSTGRES_DB")
pg_connection = os.getenv("DB_CONNECTION")

SQLALCHEMY_DATABASE_URL=f"{pg_connection}://{pg_username}:{pg_password}@{pg_host}:{pg_port}/{pg_database}"
print("pg url --->",SQLALCHEMY_DATABASE_URL)