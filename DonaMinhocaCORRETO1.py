#Dona Formiga/Danilo Melo!!!#

S, T, P = map(int, input().split())
heights = list(map(int, input().split()))
graph = [[] for _ in range(S)]
for _ in range(T):
    I, J = map(int, input().split())
    if heights[I-1] > heights[J-1]:
        graph[I-1].append(J-1)
    elif heights[J-1] > heights[I-1]:
        graph[J-1].append(I-1)

visited = [False] * S
def dfs(node):
    visited[node] = True
    count = 1
    for neighbor in graph[node]:
        if not visited[neighbor]:
            count += dfs(neighbor)
    return count

print(dfs(P-1) - 1)

#comment//~~!!
#//~~