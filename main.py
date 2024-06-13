import age

GRAPH_NAME = "test_graph"
CONFIG = (
    "host=127.0.0.1 \
    port=5455 \
    dbname=postgresDB \
    user=postgresUser \
    password=postgresPW"
)

try:
    connection = age.connect(graph=GRAPH_NAME, dsn=CONFIG)
    
    # query test
    query = "CREATE (n:Person {name: 'Maria'}) RETURN n"

    # send the query to the database
    cursor = connection.execCypher(query)

    for row in cursor:
        print("CREATED: ", row[0]) 

    connection.commit()

except Exception as e: 
    print(f"Error: {e}") 
    connection.rollback()
    
age.deleteGraph(connection.connection, GRAPH_NAME)
connection.close()
