class Edge:
    def __init__(self, cap=0, is_res=False):
        self._is_res = is_res
        self._cap = 0 if is_res else cap
        self._flow = 0
        self._res_cap = 0 if is_res else cap
        self.reverse_edge = None

    def __repr__(self):
        return f"{self._cap} {self._flow} {self._res_cap} {self._is_res}"
class Vertex:
    def __init__(self, key, value=None):
        self._key = key
        self._value = value

    def __hash__(self):  # używane przez słownik w Graph
        return hash(self._key)

    def __eq__(self, other):
        return self._key == other._key

    def __repr__(self):
        return self._key


class Graph:
    def __init__(self):
        self._List = {}

    def _bfs(self, s, t):
        parent = {}
        queue = [s]
        visited = {s}
        while len(queue):
            v = queue.pop(0)
            neighbors = self.neighbours(v)
            for n, edge in neighbors:
                if n not in visited and self.get_edge(v, n)._res_cap > 0:
                    visited.add(n)
                    queue.append(n)
                    parent[n] = v
                    if n == t:
                        return parent
        return parent

    def _get_min_cap(self, s, t, parent):
        min_cap = float("inf")
        curr = t
        while curr != s:
            prev = parent[curr]
            edge = self.get_edge(prev, curr)
            if edge._res_cap < min_cap:
                min_cap = edge._res_cap
            curr = prev
        return min_cap

    def _augment(self, s, t, parent, min_cap):
        curr = t
        while curr != s:
            prev = parent[curr]
            edge = self.get_edge(prev, curr)
            rev_edge = edge.reverse_edge

            edge._res_cap -= min_cap
            rev_edge._res_cap += min_cap

            if not edge._is_res:
                edge._flow += min_cap
            if edge._is_res:
                edge.reverse_edge._flow -= min_cap
            curr = prev

    def edmond_karp(self, graph, s, t):
        max_flow = 0
        while True:
            parent = self._bfs(s, t)
            if t not in parent:
                break
            min_cap = self._get_min_cap(s, t, parent)
            self._augment(s, t, parent, min_cap)
            max_flow += min_cap

        return max_flow

    def is_empty(self):
        if len(self._List) == 0:
            return True
        return False

    def insert_vertex(self, v):
        if not v in self._List:
            self._List[v] = {}  # cały obiekt klasy Vertex jest kluczem

    def insert_edge(self, v1, v2, capacity):
        edge = Edge(capacity, False)
        res_edge = Edge(is_res=True)

        edge.reverse_edge = res_edge
        res_edge.reverse_edge = edge

        if v1 not in self._List:
            self.insert_vertex(v1)
        if v2 not in self._List:
            self.insert_vertex(v2)

        self._List[v1][v2] = edge  # Kierunek rzeczywisty
        self._List[v2][v1] = res_edge

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


def printGraph(g):
    print("------GRAPH------")
    for v in g.vertices():
        print(v, end=" -> ")
        for n, w in g.neighbours(v):
            print(n, w, end=";")
        print()
    print(" -")


def build_graph(data):
    g = Graph()
    for u_id, v_id, cap in data:
        u = Vertex(u_id)
        v = Vertex(v_id)
        g.insert_vertex(u)
        g.insert_vertex(v)
        g.insert_edge(u, v, cap)
    return g


g0_data = [("s", "u", 2), ("u", "t", 1), ("u", "v", 3), ("s", "v", 1), ("v", "t", 2)]
g1_data = [
    ("s", "a", 16),
    ("s", "c", 13),
    ("a", "c", 10),
    ("a", "b", 12),
    ("b", "c", 9),
    ("b", "t", 20),
    ("c", "d", 14),
    ("d", "b", 7),
    ("d", "t", 4),
]
g2_data = [
    ("s", "a", 3),
    ("s", "c", 3),
    ("a", "b", 4),
    ("b", "s", 3),
    ("b", "c", 1),
    ("b", "d", 2),
    ("c", "e", 6),
    ("c", "d", 2),
    ("d", "t", 1),
    ("e", "t", 9),
]
g3_data = [
    ("s", "a", 3),
    ("s", "d", 2),
    ("a", "b", 4),
    ("b", "c", 5),
    ("c", "t", 6),
    ("a", "f", 3),
    ("f", "t", 3),
    ("d", "e", 2),
    ("e", "f", 2),
]


def main():
    g0 = build_graph(g0_data)
    g1 = build_graph(g1_data)
    g2 = build_graph(g2_data)
    g3 = build_graph(g3_data)
    s = Vertex("s")
    t = Vertex("t")

    result = g0.edmond_karp(g0, s, t)
    print(result)
    printGraph(g0)
    flow_from_u = 0
    vertex_u = Vertex("u")
    for neighbor, edge in g0.neighbours(vertex_u):
        if not edge._is_res:
            flow_from_u += edge._flow
    print(f"Przepływ z u: {flow_from_u}")

    result = g1.edmond_karp(g1, s, t)
    print(result)
    printGraph(g1)
    flow_from_a = 0
    vertex_a = Vertex("a")
    for neighbor, edge in g1.neighbours(vertex_a):
        if not edge._is_res:
            flow_from_a += edge._flow
    print(f"Przepływ z a: {flow_from_a}")

    result = g2.edmond_karp(g2, s, t)
    print(result)
    printGraph(g2)
    flow_from_a = 0
    for neighbor, edge in g2.neighbours(vertex_a):
        if not edge._is_res:
            flow_from_a += edge._flow
    print(f"Przepływ z a: {flow_from_a}")

    result = g3.edmond_karp(g3, s, t)
    print(result)
    printGraph(g3)
    flow_from_a = 0
    for neighbor, edge in g3.neighbours(vertex_a):
        if not edge._is_res:
            flow_from_a += edge._flow
    print(f"Przepływ z a: {flow_from_a}")


main()
