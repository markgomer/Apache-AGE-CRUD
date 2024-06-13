# Data Access Object
import age

class DAO:

    def __init__(self, graph_name, config) :
        self.graph_name = graph_name
        self.config = config
        pass

    def connect(self):
        try:
            self.ag = age.connect(graph=self.graph_name, dsn=self.config)
        except:
            print("Database connection error. Is postgres server running?")
        return self.ag

    def close_connection(self):
        self.ag.close()


    def execQuery(self, query):
        try:
            cursor = self.ag.execCypher(query)
            self.ag.commit()
            for row in cursor:
                print("CREATED: ", row[0]) 
        except:
            print("Cypher execution error")
