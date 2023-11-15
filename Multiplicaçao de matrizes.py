def calcular_valor_matriz_c(N, P, Q, R, S, X, Y, I, J):
    A = [[(P * i + Q * j) % X for j in range(N)] for i in range(N)]
    B = [[(R * i + S * j) % Y for j in range(N)] for i in range(N)]
    C = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
    
    return C[I-1][J-1]

N = int(input())
P, Q, R, S, X, Y = map(int, input().split())
I, J = map(int, input().split())

valor_matriz_c = calcular_valor_matriz_c(N, P, Q, R, S, X, Y, I, J)
print(valor_matriz_c)
