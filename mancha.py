def is_regular_mancha(mancha):
    N = len(mancha)

    for i in range(N):
        for j in range(N):
            if mancha[i][j] == "*":
                for k in range(i, N):
                    for l in range(j, N):
                        if mancha[k][l] == "*":
                            d_manhattan = abs(i - k) + abs(j - l)
                            d = bfs(mancha, i, j, k, l)
                            if d < d_manhattan:
                                return False
    return True


def bfs(mancha, i, j, k, l):
    N = len(mancha)
    visited = [[False] * N for _ in range(N)]
    queue = [(i, j, 0)]
    visited[i][j] = True

    while queue:
        x, y, d = queue.pop(0)

        if x == k and y == l:
            return d

        neighbors = get_neighbors(N, x, y)
        for nx, ny in neighbors:
            if mancha[nx][ny] == "*" and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, d + 1))


def get_neighbors(N, x, y):
    neighbors = []

    if x > 0:
        neighbors.append((x - 1, y))
    if x < N - 1:
        neighbors.append((x + 1, y))
    if y > 0:
        neighbors.append((x, y - 1))
    if y < N - 1:
        neighbors.append((x, y + 1))

    return neighbors


N = int(input())
mancha = []
for _ in range(N):
    linha = input()
    mancha.append(list(linha))

if is_regular_mancha(mancha):
    print("S")
else:
    print("N")
