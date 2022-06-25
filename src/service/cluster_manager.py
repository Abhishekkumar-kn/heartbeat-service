import awswrangler as wr


def connect_opensearch_cluster():
    connection = wr.opensearch.connect(
        host='https://vpc-testing-5n5xmn54rbzn3b747d6fzbprdu.us-west-2.es.amazonaws.com/'
        , port=443, username='testing', password='')
    return connection
