class Writer : 

    def __init__(self) -> None:
        pass

    def create_vertex(self, label, prop) :
        query = f'CREATE (:{label} {prop})'
        print(query)
        return query
