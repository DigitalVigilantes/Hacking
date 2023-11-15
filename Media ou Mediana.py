def calcular_c(A, B):
    C = A + B - max(A, B)
    return C

A, B = map(int, input().split())

C = calcular_c(A, B)

print(C)
