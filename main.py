import psycopg2
from DAO import DAO
import Writer

# procedures
# setup AGE
GRAPH_NAME = "test_graph"

# get database configuration
config = "host=127.0.0.1 port=5455 dbname=postgresDB user=postgresUser password=postgresPW"

# create data access object
Dao = DAO(GRAPH_NAME, config);

# connect to the database
connection = Dao.connect()

# create writer object 
writer = Writer.Writer()

# send test queries
# "CREATE (n:Person {name: 'Joe'})"
v_label = 'Person'
v_prop = "{name: 'Joe'}"
query = writer.create_vertex(v_label, v_prop)
Dao.execQuery(query)

Dao.close_connection()
