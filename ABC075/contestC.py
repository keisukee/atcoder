import sys
sys.setrecursionlimit(500000)

N, M = list(map(int, input().split()))
graph = [[] for i in range(N)]
connected = {i: 0 for i in range(N)}
vertices = []
for i in range(M):
    a, b = list(map(int, input().split()))
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    vertices.append([a-1, b-1])


def canTraverse(graph, visited, currentEdge, removedVertice):
    visited[currentEdge] = True
    if len(graph) == len(visited):
        return True

    for nextEdge in graph[currentEdge]:
        if (currentEdge == removedVertice[0] and nextEdge == removedVertice[1]) or (currentEdge == removedVertice[1] and nextEdge == removedVertice[0]):
            continue
        if nextEdge not in visited:
            if canTraverse(graph, visited, nextEdge, removedVertice):
                return True

    return False


bridgeCount = 0
for i in range(M):
    removedVertice = vertices[i]
    visited = {}
    startEdge = 0
    if not canTraverse(graph, visited, startEdge, removedVertice):
        bridgeCount += 1

print(bridgeCount)
