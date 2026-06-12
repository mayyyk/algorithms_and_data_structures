def rec_pattern(P, T, i, j):
    if i==0:
        return j # koszt wstawienia wszystkich brakujących z T do P to ilość liter, które zostały w T, czyli j
    if j==0:
        return i # koszt usunięcia wszysktich ze wzorca, bo w T już się skończyło to ilość liter pozostałych we wzorcu

    val_ins = 1 + rec_pattern(P, T, i, j-1) # wstawienie do wzorca, więc T dopasowane, można iść dalej, ale w P i zostaje
    val_del = 1 + rec_pattern(P, T, i-1, j) # usunięcie ze wzorca, ale w T dalej trzeba sobie z tym poradzić
    val_sub = rec_pattern(P, T, i-1, j-1) + (1 if P[i] != T[j] else 0) # sprawia, że obydwa znaki są załatwione, więc można iść dalej

    return min(val_ins, val_del, val_sub)

P = ' kot'
T = ' pies'
print(rec_pattern(P, T, len(P)-1, len(T)-1))

def rec_pd_pattern(P, T):
    D = [[0]*len(T) for _ in range(len(P))]
    
    for row in range(len(P)):
        D[row][0] = row # wypełnienie całej pierwszej kolumny

    for col in range(len(T)):
        D[0][col] = col

    # I - wstawianie, D - usunięcie, R - zamiana, M - zgodne
    Parents = [["X"]*len(T) for _ in range(len(P))]
    
    for row in range(len(P)):
        Parents[row][0] = "D" # wypełnienie całej pierwszej kolumny

    for col in range(len(T)):
        Parents[0][col] = "I" # wypełnienie całego pierwszego rzędu

    Parents[0][0] = "X"

    # liczenie

    for i in range(1, len(P)): # wiersze
        for j in range(1, len(T)): # kolumny
            val_ins = D[i][j-1] + 1
            val_del = D[i-1][j] + 1
            val_sub = D[i-1][j-1] + (1 if P[i] != T[j] else 0) 
            
            D[i][j] = min(val_ins, val_del, val_sub)

            if D[i][j] == val_sub:
                if P[i] == T[j]:
                    Parents[i][j] = "M"
                else:
                    Parents[i][j] = "R"
            elif D[i][j] == val_ins:
                Parents[i][j] = "I"
            elif D[i][j] == val_del:
                Parents[i][j] = "D"



    return D[-1][-1], Parents

def path2string(Parents, P, T):
    i = len(P)-1
    j = len(T)-1

    path = []

    while Parents[i][j] != "X":
        val = Parents[i][j]
        path.append(val)
        if val=="R" or val=="M":
            i-=1
            j-=1
        elif val == "I":
            j-=1
        elif val == "D":
            i-=1        
    
    return "".join(reversed(path))

P = ' biały autobus'
T = ' czarny autokar'
print(rec_pd_pattern(P, T)[0])

P = ' thou shalt not'
T = ' you should not'
print(path2string(rec_pd_pattern(P, T)[1], P, T))