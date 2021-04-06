N, M = list(map(int, input().split()))
graph = [[] for _ in range(N)]
for i in range(M):
    a, b = list(map(int, input().split()))
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def getAllTraverseWays(graph, visited, count, currentEdge):
    # print('visited', visited)
    if count == len(graph):
        return 1

    visited[currentEdge] = True
    ways = 0
    for nextEdge in graph[currentEdge]:
        if not visited[nextEdge]:
            ways += getAllTraverseWays(graph, visited, count+1, nextEdge)

    visited[currentEdge] = False
    return ways

visited = [False for _ in range(N)]
ways = getAllTraverseWays(graph, visited, 1, 0)
print(ways)


