MOD = 998244353

def verificar_ultramaratona_valida(pontos_hidratacao):
    cidades = set()
    for estrada in pontos_hidratacao:
        cidades.add(estrada[0])
        cidades.add(estrada[1])
    return len(cidades) == N

def dfs(estradas, cidade_atual, pontos_hidratacao):
    if len(pontos_hidratacao) == N - 1:
        ultramaratona_valida = verificar_ultramaratona_valida(pontos_hidratacao)
        if ultramaratona_valida:
            yield 1
        return

    for estrada in estradas:
        Ai, Bi, Ei = estrada
        if (Ai == cidade_atual or Bi == cidade_atual) and Ei == 1 and estrada not in pontos_hidratacao:
            pontos_hidratacao.append(estrada)
            proxima_cidade = Ai if Bi == cidade_atual else Bi
            yield from dfs(estradas, proxima_cidade, pontos_hidratacao)
            pontos_hidratacao.remove(estrada)

N = int(input())
estradas = []
for _ in range(N - 1):
    Ai, Bi, Ei = map(int, input().split())
    estradas.append((Ai, Bi, Ei))

contador_combinacoes = 0
for _ in dfs(estradas, 1, []):
    contador_combinacoes += 1
    print(contador_combinacoes % MOD)
