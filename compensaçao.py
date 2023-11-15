def compensar_cheques(lista_cheques):
    saldo = [0] * (N+1)

    for x, v, y in lista_cheques:
        saldo[x] -= v
        saldo[y] += v

    possivel_diminuir = False
    for i in range(1, N+1):
        if saldo[i] < 0:
            possivel_diminuir = True
            break

    total_minimo = sum(abs(s) for s in saldo) // 2

    if possivel_diminuir:
        print("S")
    else:
        print("N")
    print(total_minimo)


M, N = map(int, input().split())
lista_cheques = []
for _ in range(M):
    x, v, y = map(int, input().split())
    lista_cheques.append((x, v, y))

compensar_cheques(lista_cheques)
