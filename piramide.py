N = int(input())

pyramid = [[0 for _ in range(N)] for _ in range(N)]

for layer in range(N // 2 + 1):
    for i in range(layer, N - layer):
        for j in range(layer, N - layer):
            pyramid[i][j] += 1

for row in pyramid:
    print(' '.join(map(str, row)))