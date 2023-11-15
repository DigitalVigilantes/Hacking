lista = []
while True:
    n = int(input("Digite um número: "))
    if n < 0:
        break
    lista.append(n)

intervalos = [[0, 25], [26, 50], [51, 75], [76, 100]]
contagem = [0] * len(intervalos)

for n in lista:
    for i in range(len(intervalos)):
        if intervalos[i][0] <= n <= intervalos[i][1]:
            contagem[i] += 1

for i in range(len(intervalos)):
    print(f"Intervalo {intervalos[i]}: {contagem[i]}")