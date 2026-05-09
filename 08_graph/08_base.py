import polska as pl


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

    def insert_edge(self, v1, v2, edge=None):
        self._List[v1][v2] = edge
        self._List[v2][v1] = edge  # dwukierunkowe, bo graf nieskierowany teraz

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


class AdjacencyMatrix:
    def __init__(self, init_val=0):
        self._Matrix = []
        self._vertices_list = []
        self._init_val = init_val

    def is_empty(self):
        return len(self._Matrix) == 0

    def insert_vertex(self, v):
        if v in self._vertices_list:
            return
        for row in self._Matrix:
            row.append(self._init_val)
        self._vertices_list.append(v)
        self._Matrix.append([self._init_val] * len(self._vertices_list))

    def insert_edge(self, v1, v2, edge=1):
        # zabezpieczenie, gdyby ich nie było
        self.insert_vertex(v1)
        self.insert_vertex(v2)

        idx1 = self._vertices_list.index(v1)
        idx2 = self._vertices_list.index(v2)

        self._Matrix[idx1][idx2] = edge
        self._Matrix[idx2][idx1] = edge  # dwukierunkowe, bo graf nieskierowany teraz

    def delete_vertex(self, v):
        if v in self._vertices_list:
            idx = self._vertices_list.index(v)
            self._Matrix.pop(idx)
            for row in self._Matrix:
                row.pop(idx)
            self._vertices_list.pop(idx)

    def delete_edge(self, v1, v2):
        if v1 in self._vertices_list and v2 in self._vertices_list:
            idx1 = self._vertices_list.index(v1)
            idx2 = self._vertices_list.index(v2)
            self._Matrix[idx1][idx2] = self._init_val
            self._Matrix[idx2][idx1] = self._init_val

    def get_edge(self, v1, v2):
        if v1 not in self._vertices_list or v2 not in self._vertices_list:
            return None
        idx1 = self._vertices_list.index(v1)
        idx2 = self._vertices_list.index(v2)
        return self._Matrix[idx1][idx2]

    def neighbours(self, v_id):
        row = self._Matrix[v_id]
        for col, edge in enumerate(row):
            if edge != self._init_val:
                yield col, edge

    def vertices(self):
        for i in range(0, len(self._Matrix)):
            yield i

    def get_vertex(self, v_id):
        return self._vertices_list[v_id]


def main():
    g_list = AdjacencyList()
    g_matrix = AdjacencyMatrix()

    vertices = {}
    for edge in pl.graf:
        v1 = edge[0]
        v2 = edge[1]

        if v1 not in vertices:
            vertices[v1] = Vertex(v1)
        if v2 not in vertices:
            vertices[v2] = Vertex(v2)

        g_list.insert_vertex(vertices[v1])
        g_matrix.insert_vertex(vertices[v1])

        g_list.insert_vertex(vertices[v2])
        g_matrix.insert_vertex(vertices[v2])

        g_list.insert_edge(vertices[v1], vertices[v2])
        g_matrix.insert_edge(vertices[v1], vertices[v2])

    g_list.delete_vertex(Vertex("K"))
    g_matrix.delete_vertex(Vertex("K"))

    g_list.delete_edge(Vertex("W"), Vertex("E"))
    g_matrix.delete_edge(Vertex("W"), Vertex("E"))

    pl.draw_map(g_list)
    pl.draw_map(g_matrix)


main()
