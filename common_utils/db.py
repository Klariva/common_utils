from google.auth import default
from google.auth.transport.requests import Request
import psycopg
import os

def getconn():

    # Get IAM auth token
    creds, _ = default()
    creds.refresh(Request())
    iam_token = creds.token
    conn = psycopg.connect(
        user=os.getenv("DB_USER"),
        dbname=os.getenv("DB_NAME"),
        host=os.getenv("DB_HOST"),
        password=iam_token,
        sslmode="disable",
        target_session_attrs="read-write",
    )
    return conn

def run_sql(conn, sql):
    try:
        with conn.cursor() as cur:
            cur.execute(sql)
        conn.commit()
    finally:
        conn.close()
