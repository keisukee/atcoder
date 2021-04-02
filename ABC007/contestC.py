from collections import deque
R, C = list(map(int, input().split()))
sy, sx = list(map(int, input().split()))
gy, gx = list(map(int, input().split()))
maze = []
sy -= 1
sx -= 1
gy -= 1
gx -= 1

for i in range(R):
    data = list(input())
    maze.append(data)

def bfs(maze, sy, sx, gy, gx, visited):
    queue = deque([[sy, sx, 0]])
    while queue:
        y, x, distance = queue.popleft()
        if (y, x) in visited:
            continue

        visited[(y, x)] = True
        if y == gy and x == gx:
            return distance

        nextLocs = [[y-1, x], [y+1, x], [y, x+1], [y, x-1]]
        for nextLoc in nextLocs:
            if not(0 <= nextLoc[0] < len(maze) and 0 <= nextLoc[1] < len(maze[0])):
                continue
            if maze[nextLoc[0]][nextLoc[1]] == '#':
                continue
            queue.append([nextLoc[0], nextLoc[1], distance+1])
    return -1

visited = {}
minDistance = bfs(maze, sy, sx, gy, gx, visited)
# print('visited', visited)
print(minDistance)