S, T, P = map(int, input().split()) 
A = list(map(int, input().split())) 
G = {}
for i in range(T):
    I, J = map(int, input().split())
    if I not in G:
        G[I] = []
    G[I].append(J)
    if J not in G:
        G[J] = []
    G[J].append(I)

def explorar(salao):
    maximo = 0
    if salao in G:
        for vizinho in G[salao]:
            if A[vizinho-1] < A[salao-1]:
                visitados = 1 + explorar(vizinho)
                if visitados > maximo:
                    maximo = visitados
    return maximo

print(explorar(P))