import heapq

N, M, X, Y = list(map(int, input().split()))
graph = [[] for _ in range(N)]

for i in range(M):
    a, b, t, k = list(map(int, input().split()))
    graph[a-1].append([b-1, t, k])
    graph[b-1].append([a-1, t, k])

min_time = float('inf')

def search_fastest_path(graph, start, goal):
    distances = [float('inf')] * len(graph)
    distances[start] = 0
    minheap = [(0, start)] # (distance, edge)
    while minheap:
        current_distance, current_edge = heapq.heappop(minheap)
        # print(distances)
        if current_distance > distances[current_edge]:
            continue

        for next_edge, t, k in graph[current_edge]:

            wait = (k - distances[current_edge]%k) if distances[current_edge] % k != 0 else 0
            new_distance = distances[current_edge] + wait + t
            if new_distance < distances[next_edge]:
                distances[next_edge] = new_distance
                heapq.heappush(minheap, (distances[next_edge], next_edge))

    return distances[goal]

cost = search_fastest_path(graph, X-1, Y-1)
# print(cost)
answer = cost if cost != float('inf') else -1
print(answer)



