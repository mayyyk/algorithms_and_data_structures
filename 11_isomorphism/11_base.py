# skończone
from Matrix import Matrix, transpose
from copy import deepcopy

graph_G = [ ('A','B',1), ('B','F',1), ('B','C',1), ('C','D',1), ('C','E',1), ('D','E',1)] # ilość kolumn M
graph_P = [ ('A','B',1), ('B','C',1), ('A','C',1)] # ilość wierszy M

def ullman_bruteforce(G, P):
    stats = {"iso": 0, "calls": 0}
    num_m_rows = len(P._vertices_list)
    num_m_cols = len(G._vertices_list)
    used_cols = [False for _ in range(num_m_cols)]
    M = Matrix((num_m_rows,num_m_cols))
    ullman_bruteforce_rec(used_cols, 0, M, G, P, stats)
    return stats["iso"], stats["calls"]

def ullman_bruteforce_rec(used_cols, cur_row, M, G, P, stats):
    stats["calls"]+=1
    if cur_row==len(P._vertices_list):
        right = M*G._Matrix*transpose(M)
        if P._Matrix == right:
            stats["iso"]+=1
        #print(M)
        return
    for c in range(M.size()[1]):
        if used_cols[c]!=True:
            used_cols[c] = True
            for idx in range(M.size()[1]):
                if idx==c:
                    M[cur_row][idx] = 1
                else:
                    M[cur_row][idx] = 0
            ullman_bruteforce_rec(used_cols, cur_row+1, M, G, P, stats)
            used_cols[c] = False

def ullman_optimal(G, P):
    stats = {"iso": 0, "calls": 0}
    num_m_rows = len(P._vertices_list)
    num_m_cols = len(G._vertices_list)
    used_cols = [False for _ in range(num_m_cols)]
    M0 = Matrix((num_m_rows,num_m_cols))

    for i in range(num_m_rows):
        deg_P = sum(1 for _ in P.neighbours(i))

        for j in range(num_m_cols):
            deg_G = sum(1 for _ in G.neighbours(j))

            if deg_P <= deg_G:
                M0[i][j] = 1
            else:
                M0[i][j] = 0
    
    M = deepcopy(M0)

    ullman_optimal_rec(used_cols, 0, M, G, P, stats, M0)
    return stats["iso"], stats["calls"]

def ullman_optimal_rec(used_cols, cur_row, M, G, P, stats, M0):
    stats["calls"]+=1
    if cur_row==len(P._vertices_list):
        right = M*G._Matrix*transpose(M)
        if P._Matrix == right:
            stats["iso"]+=1
        #print(M)
        return
    for c in range(M.size()[1]):
        if M0[cur_row][c] != 0 and used_cols[c]!=True:
            used_cols[c] = True
            M_copy = deepcopy(M)
            for idx in range(M.size()[1]):
                if idx==c:
                    M_copy[cur_row][idx] = 1
                else:
                    M_copy[cur_row][idx] = 0
            ullman_optimal_rec(used_cols, cur_row+1, M_copy, G, P, stats, M0)
            used_cols[c] = False


class AdjacencyMatrix:
    def __init__(self, init_val=0):
        self._Matrix = Matrix((0, 0), init_val)  
        self._vertices_list = []
        self._init_val = init_val

    def __eq__(self, other: object) -> bool:
        if isinstance(other, AdjacencyMatrix):
            return self._Matrix == other._Matrix and self._vertices_list == other._vertices_list
        return False

    def is_empty(self):
        return len(self._vertices_list) == 0

    def insert_vertex(self, v):
        if v in self._vertices_list:
            return
        
        self._vertices_list.append(v)

        matrix_data = self._Matrix.get_matrix()
        
        for row in matrix_data:
            row.append(self._init_val)
            
        matrix_data.append([self._init_val] * len(self._vertices_list))
        
        self._Matrix = Matrix(matrix_data)

    def insert_edge(self, v1, v2, edge=1):
        self.insert_vertex(v1)
        self.insert_vertex(v2)

        idx1 = self._vertices_list.index(v1)
        idx2 = self._vertices_list.index(v2)

        self._Matrix[idx1][idx2] = edge
        self._Matrix[idx2][idx1] = edge # dwukierunkowy graf, nieskierowany

    def delete_vertex(self, v):
        if v in self._vertices_list:
            idx = self._vertices_list.index(v)
            self._vertices_list.pop(idx)
            
            matrix_data = self._Matrix.get_matrix()
            
            matrix_data.pop(idx)
            
            for row in matrix_data:
                row.pop(idx)
                
            self._Matrix = Matrix(matrix_data)

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
        for i in range(len(self._vertices_list)):
            yield i

    def get_vertex(self, v_id):
        return self._vertices_list[v_id]
        
    def __str__(self):
        return str(self._Matrix)


def main():
    g = AdjacencyMatrix()
    for v1, v2, edge in graph_G:
        g.insert_edge(v1, v2, edge)
        
    p = AdjacencyMatrix()
    for v1, v2, edge in graph_P:
        p.insert_edge(v1, v2, edge)

    print(ullman_bruteforce(g, p))
    print(ullman_optimal(g, p))

if __name__ == "__main__":
    main()