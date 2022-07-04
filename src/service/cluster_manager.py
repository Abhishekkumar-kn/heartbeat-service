import awswrangler as wr
import mysql.connector


def opensearch_cluster_connection() -> object:
    return wr.opensearch.connect(
        host='https://vpc-testing-5n5xmn54rbzn3b747d6fzbprdu.us-west-2.es.amazonaws.com/'
        , port=443, username='abhishek', password='Abhishek2022@')


def db_connection():
    return mysql.connector.connect(
        host="kx-ocr-db.cufogrztxzel.us-west-2.rds.amazonaws.com",
        user="kxuser",
        password="101Metro",
        database="ocrdb"
    )
