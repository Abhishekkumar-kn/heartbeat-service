# this file will contains all the functions
import calendar
import time

# from .service import cluster_manager
from service.db_driver import get_table_from_opensearch


def heartbeat():
    try:
        query = "SELECT * FROM .kibana_1407856029_abhishek_1"
        data = get_table_from_opensearch(query)
        print(data)
    except EOFError as e:
        print(e)


if __name__ == "__main__":
    heartbeat()
