def solve_passatempo(L, C, linhas, colunas):
    variaveis = set()
    coeficientes = {}

    for i in range(L):
        for j in range(C):
            variavel = linhas[i][j]
            coeficientes[variavel] = [0] * (L + C)

    for i in range(L):
        for j in range(C):
            variavel = linhas[i][j]
            coeficientes[variavel][i] += 1
            coeficientes[variavel][L + j] -= 1

    for i in range(L + C - 1):
        pivo = coeficientes[list(coeficientes.keys())[i]][i]
        for j in range(i + 1, L + C):
            coeficiente_atual = coeficientes[list(coeficientes.keys())[j]][i]
            fator = coeficiente_atual / pivo
            for k in range(i, L + C):
                coeficientes[list(coeficientes.keys())[j]][k] -= fator * coeficientes[list(coeficientes.keys())[i]][k]

    valores_variaveis = {}
    for i in range(L + C - 2, -1, -1):
        variavel = list(coeficientes.keys())[i]
        soma = coeficientes[variavel][-1]
        for j in range(i + 1, L + C - 1):
            soma -= coeficientes[variavel][j] * valores_variaveis[list(coeficientes.keys())[j]]
        valores_variaveis[variavel] = soma

    variaveis_ordenadas = sorted(list(valores_variaveis.keys()))

    for variavel in variaveis_ordenadas:
        print(variavel, valores_variaveis[variavel])


L, C = map(int, input().split())
linhas = []
for _ in range(L):
    linha = input().split()
    linhas.append(linha[:-1])
colunas = list(map(int, input().split()))

solve_passatempo(L, C, linhas, colunas)
