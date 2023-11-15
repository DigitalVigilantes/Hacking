from collections import deque

N, M, K = map(int, input().split())

exhibition = [[0 for _ in range(M)] for _ in range(N)]

for _ in range(K):
    C, L, D = input().split()
    C = int(C) - 1
    L = int(L) - 1
    exhibition[C][L] = 1
    if D == 'N':
        for i in range(L - 1, -1, -1):
            exhibition[C][i] = 1
    elif D == 'S':
        for i in range(L + 1, M):
            exhibition[C][i] = 1
    elif D == 'L':
        for i in range(C + 1, N):
            exhibition[i][L] = 1
    else:
        for i in range(C - 1, -1, -1):
            exhibition[i][L] = 1

queue = deque([(0, 0)])
visited = set()
while queue:
    x, y = queue.popleft()
    if (x, y) == (N - 1, M - 1):
        print('S')
        break
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_x = x + dx
        new_y = y + dy
        if (new_x >= 0 and new_x < N and new_y >= 0 and new_y < M and exhibition[new_x][new_y] == 0 and (new_x, new_y) not in visited):
            queue.append((new_x, new_y))
            visited.add((new_x, new_y))
else:
    print('N')