from  constant import *
import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Підключення до бази даних успішне")
    except OperationalError as e:
        print(f"Помилка '{e}' ")
    return connection

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"Помилка '{e}' ")
        
query = """
SELECT *
FROM users;
"""


if __name__ == "__main__":
    connection = create_connection(
        db_name=database,
        db_user=user,
        db_password=password,
        db_host=host,
        db_port=port
    )

    if connection:
        print("Підключення до бази даних:", connection)
    else:
        print("Помилка підключення до бази даних")
        
    query_result = execute_read_query(
    connection=connection,
    query=query
)

print(query_result)

