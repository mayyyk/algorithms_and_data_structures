from graf_mst import graf

class Vertex:
    def __init__(self, key, value=None):
        self._key = key
        self._value = value

    def __hash__(self):  # używane przez słownik w AdjacencyList
        return hash(self._key)

    def __eq__(self, other):
        return self._key == other._key

    def __repr__(self):
        return self._key


class AdjacencyList:
    def __init__(self):
        self._List = {}

    def is_empty(self):
        if len(self._List) == 0:
            return True
        return False

    def insert_vertex(self, v):
        if not v in self._List:
            self._List[v] = {}  # cały obiekt klasy Vertex jest kluczem

    def insert_edge(self, v1, v2, edge_weight=0):
        self._List[v1][v2] = edge_weight
        self._List[v2][v1] = edge_weight  # dwukierunkowe, bo graf nieskierowany teraz

    def delete_vertex(self, v):
        original_v = None
        for vertex in self._List:
            if vertex == v:
                original_v = vertex
                break
        if original_v:
            for neighbour in list(self._List[v].keys()):
                self._List[neighbour].pop(original_v, None)
            del self._List[original_v]

    def delete_edge(self, v1, v2):
        if v1 in self._List and v2 in self._List[v1]:
            del self._List[v1][v2]
        if v2 in self._List and v1 in self._List[v2]:
            del self._List[v2][v1]

    def get_edge(self, v1, v2):
        if v1 in self._List and v2 in self._List[v1]:
            return self._List[v1][v2]
        return

    def neighbours(self, v_id):
        for n_id, edge in self._List[v_id].items():
            yield n_id, edge

    def vertices(self):
        for v_id in self._List.keys():
            yield v_id

    def get_vertex(self, v_id):
        return v_id

def prim_mst(g):
    intree ={v: False for v in g.vertices()}
    distance = {v: float('inf') for v in g.vertices()}
    parent = {v: None for v in g.vertices()}
   
    start_node = next(iter(g.vertices())) # pierwszy element z generatora yield
    distance[start_node] = 0

    mst_graph = AdjacencyList()
    mst_graph.insert_vertex(start_node)

    for _ in range(len(intree)):
        u = None
        min_dist = float('inf')

        for v in g.vertices():      
            if (distance[v] < min_dist) and not intree[v]:
                min_dist = distance[v]
                u = v
        
        if u is None:
            break

        intree[u] = True
        mst_graph.insert_vertex(u)

        if parent[u] is not None:
            mst_graph.insert_edge(parent[u], u, distance[u])
        
        for neighbour, weight in g.neighbours(u):
            if not intree[neighbour] and weight < distance[neighbour]:
                distance[neighbour] = weight
                parent[neighbour] = u
    return mst_graph

def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end = " -> ")
        for (n, w) in g.neighbours(v):
            print(n, w, end=";")
        print()
    print("-------------------")

def main():
    g = AdjacencyList()
    vertices = {}
    for edge in graf:
        v1 = edge[0]
        v2 = edge[1]
        edge_weight = edge[2]

        if v1 not in vertices:
            vertices[v1] = Vertex(v1)
        if v2 not in vertices:
            vertices[v2] = Vertex(v2)

        g.insert_vertex(vertices[v1])
        g.insert_vertex(vertices[v2])
        g.insert_edge(vertices[v1], vertices[v2], edge_weight)

    mst_g = prim_mst(g)
    printGraph(mst_g)

main()
