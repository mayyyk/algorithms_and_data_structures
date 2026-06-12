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


def rec_pd_pattern(P, T, substring_mode = False, lcs_mode = False):
    D = [[0]*len(T) for _ in range(len(P))]
    
    for row in range(len(P)):
        D[row][0] = row # wypełnienie całej pierwszej kolumny

    if substring_mode==True:
        pass
    else:
        for col in range(len(T)): 
            D[0][col] = col # wypełnienie całego pierwszego rzędu

    # I - wstawianie, D - usunięcie, R - zamiana, M - zgodne
    Parents = [["X"]*len(T) for _ in range(len(P))]
    
    for row in range(len(P)):
        Parents[row][0] = "D" # wypełnienie całej pierwszej kolumny

    if substring_mode==True:
        for col in range(len(T)):
            Parents[0][col] = "X" # wypełnienie całego pierwszego rzędu
    else:
        for col in range(len(T)):
            Parents[0][col] = "I" # wypełnienie całego pierwszego rzędu

    Parents[0][0] = "X"

    # liczenie

    for i in range(1, len(P)): # wiersze
        for j in range(1, len(T)): # kolumny
            val_ins = D[i][j-1] + 1
            val_del = D[i-1][j] + 1

            if lcs_mode:
                val_sub = D[i-1][j-1] + (0 if P[i] == T[j] else 1000)
            else:
                val_sub = D[i-1][j-1] + (1 if P[i] != T[j] else 0) 
            
            D[i][j] = min(val_ins, val_del, val_sub)

            if D[i][j] == val_sub:
                if P[i] == T[j]:
                    Parents[i][j] = "M"
                else:
                    Parents[i][j] = "R"
            elif D[i][j] == val_del:
                Parents[i][j] = "D"
            elif D[i][j] == val_ins:
                Parents[i][j] = "I"

    if substring_mode:
        min_val = min(D[-1][1:])
        min_val_idx = D[-1][1:].index(min_val) + 1
        return min_val, min_val_idx, Parents
    else:
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


def decode_solution(Parents, P, T, start_i, start_j, extract_lcs = False):
    i = start_i
    j = start_j
    lcs_chars = []

    while Parents[i][j] != "X":
        val = Parents[i][j]
        if val == "M":
            if extract_lcs:
                lcs_chars.append(P[i])
            i -= 1
            j -= 1
        elif val == "R":
            i -= 1
            j -= 1
        elif val == "I":
            j -= 1
        elif val == "D":
            i -= 1        
            
    if extract_lcs:
        return "".join(reversed(lcs_chars))
    else:
        return j

P = ' biały autobus'
T = ' czarny autokar'
print(rec_pd_pattern(P, T)[0])

P = ' thou shalt not'
T = ' you should not'
print(path2string(rec_pd_pattern(P, T)[1], P, T))

# d) wyszukiwanie podciągów
T_d = ' mokeyssbanana'

# Test 1 
P_d1 = ' ban'
koszt1, idx_konca1, parents1 = rec_pd_pattern(P_d1, T_d, substring_mode=True)
idx_startu1 = decode_solution(parents1, P_d1, T_d, len(P_d1)-1, idx_konca1)
print(f"{idx_startu1}, {koszt1}")

# Test 2 
P_d2 = ' bin'
koszt2, idx_konca2, parents2 = rec_pd_pattern(P_d2, T_d, substring_mode=True)
idx_startu2 = decode_solution(parents2, P_d2, T_d, len(P_d2)-1, idx_konca2)
print(f"{idx_startu2}, {koszt2}")


# e) najdłuższa wspólna sekwencja
P_e = ' democrat'
T_e = ' republican'
koszt_e, parents_e = rec_pd_pattern(P_e, T_e, lcs_mode=True)
print(decode_solution(parents_e, P_e, T_e, len(P_e)-1, len(T_e)-1, extract_lcs=True))


# f) najdłuższa podsekwencja monotoniczna
T_f = ' 243517698'
P_f = ' ' + "".join(sorted(T_f.strip())) # tworzenie posortowanego wzorca P ze spacją na początku
koszt_f, parents_f = rec_pd_pattern(P_f, T_f, lcs_mode=True)
print(decode_solution(parents_f, P_f, T_f, len(P_f)-1, len(T_f)-1, extract_lcs=True))