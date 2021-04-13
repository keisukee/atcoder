from heapq import heappush, heappop
INF = 10 ** 9
def dijkstra(s, n): # (始点, ノード数)
    dist = [INF] * n
    minheap = [(0, s)] # (distance, node)
    dist[s] = 0
    seen = [False] * n # ノードが確定済みかどうか
    while minheap:
        _, v = heappop(minheap) # ノードを pop する
        seen[v] = True
        for to, cost in adj[v]: # ノード v に隣接しているノードに対して
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(minheap, (dist[to], to))
    return dist