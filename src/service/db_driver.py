import awswrangler as wr
from mysql.connector import Error

from .cluster_manager import opensearch_cluster_connection, db_connection


def get_table_from_opensearch(sql_query):
    return wr.opensearch.search_by_sql(client=opensearch_cluster_connection(),
                                       sql_query=sql_query)


def write_timestamp_in_db():
    try:
        connection = db_connection()
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("insert into heartbeat values (current_timestamp)")
            connection.commit()
    except Error as e:
        print("Error while connecting to MySQL", e)
