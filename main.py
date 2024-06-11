import psycopg2
import age

GRAPH_NAME = "test_graph"
ag = age.connect(host="172.0.0.1", port="5455", dbname="postgresDB", \
    user="postgresUser", password="postgresPW", graph=GRAPH_NAME)
conn = ag.connection

# procedures


# get database configuration


# create data access object


# connect to the database


# create writer object 


# listen to sent queries

