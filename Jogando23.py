N = int(input())
joao = sum(map(int, input().split()))
maria = sum(map(int, input().split()))
comuns = list(map(int, input().split()))

for carta in comuns:
    joao += carta
    maria += carta

if joao > 23:
    joao = 0

menor_carta = -1
for i in range(1, 14):
    if maria + i <= 23 and (joao + i > 23 or joao + i < maria + i):
        menor_carta = i
        break

print(menor_carta)
