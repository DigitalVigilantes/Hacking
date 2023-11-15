N, Q = map(int, input().split())
pessoas_por_andar = list(map(int, input().split()))

prefixa = [0]
for pessoas in pessoas_por_andar:
    prefixa.append(prefixa[-1] + pessoas)

for _ in range(Q):
    evento = input().split()
    tipo = int(evento[0])
    andar = int(evento[1])

    if tipo == 0:
        pessoas_por_andar[andar - 1] = int(evento[2])
        prefixa = [0]
        for pessoas in pessoas_por_andar:
            prefixa.append(prefixa[-1] + pessoas)
    elif tipo == 1:
        total_pessoas = prefixa[andar]
        print(total_pessoas)
