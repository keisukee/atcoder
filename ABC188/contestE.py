from collections import deque
import sys
sys.setrecursionlimit(500000)

N, M = list(map(int, input().split()))
prices = list(map(int, input().split()))
graph = [[] for _ in range(N)]

for i in range(M):
    x, y = list(map(int, input().split()))
    graph[x-1].append(y-1)


prices_sorted_by_order = sorted([(prices[idx], idx) for idx in range(len(prices))])

def get_maximum_profit(graph, location, prices, visited):
    max_profit = float('-inf')
    queue = deque(graph[location])
    min_price = prices[location]

    while queue:
        current_edge = queue.popleft()
        if current_edge in visited:
            continue

        visited[current_edge] = True

        if prices[current_edge] - min_price > max_profit:
            max_profit = prices[current_edge] - min_price

        for next_edge in graph[current_edge]:

            queue.append(next_edge)

    return max_profit

visited = {}

max_profit = float('-inf')
for val, idx in prices_sorted_by_order:
    max_profit = max(max_profit, get_maximum_profit(graph, idx, prices, visited))

print(max_profit)