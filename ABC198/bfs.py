from collections import deque
def bfs(edges, start):
    nodes = deque([start])
    visited = set()
    while nodes:
        current_node = nodes.popleft()
        print(current_node, visited, nodes)
        visited.add(current_node)
        for next_node in edges[current_node]:
            if next_node not in visited:
                nodes.append(next_node)

    return

edges = [[1], [0, 2, 4], [5, 1, 3], [2], [1], [2]]
bfs(edges, 0)
