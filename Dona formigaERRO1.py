from collections import defaultdict

def max_rooms_visited(S, T, P, heights, tunnels):
    graph = defaultdict(list)
    for i, j in tunnels:
        if heights[i-1] > heights[j-1]:
            graph[i].append(j)
        elif heights[j-1] > heights[i-1]:
            graph[j].append(i)

    visited = set()
    stack = [P]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
    return len(visited) - 1

S = 4
T = 5
P = 2
heights = [100, 150, -50, 200]
tunnels = [(1, 2), (2, 4), (1, 4), (3, 4), (1, 3)]

print(max_rooms_visited(S, T, P, heights, tunnels))