E, M, D = map(int, input().split())

like_pairs = [[] for _ in range(E + 1)]
dislike_pairs = [[] for _ in range(E + 1)]

for _ in range(M):
    X, Y = map(int, input().split())
    like_pairs[X].append(Y)
    like_pairs[Y].append(X)

for _ in range(D):
    U, V = map(int, input().split())
    dislike_pairs[U].append(V)
    dislike_pairs[V].append(U)

groups = [list(map(int, input().split())) for _ in range(E // 3)]

violations = 0
for group in groups:
    for i in range(3):
        for j in range(i + 1, 3):
            stud1 = group[i]
            stud2 = group[j]
            if stud2 in like_pairs[stud1] or stud2 in dislike_pairs[stud1]:
                violations += 1
            if stud1 in like_pairs[stud2] or stud1 in dislike_pairs[stud2]:
                violations += 1

print(violations)