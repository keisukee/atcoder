import sys
sys.setrecursionlimit(500000)
H, W = list(map(int, input().split()))

grid = []
for i in range(H):
    row = list(input())
    grid.append(row)


def getTarget(grid, char):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == char:
                return (i, j)
    return (-1, -1)


def show(grid):
    for i in range(len(grid)):
        print(grid[i])


def canReachGoal(grid, visited, row, col):
    if not(0 <= row < len(grid) and 0 <= col < len(grid[0])) or visited[row][col] or grid[row][col] == '#':
        return

    visited[row][col] = True
    if grid[row][col] == 'g':
        return True

    nextLocs = [(row-1, col), (row+1, col),
                (row, col-1), (row, col+1)]

    for nextLoc in nextLocs:
        if canReachGoal(grid, visited, nextLoc[0], nextLoc[1]):
            return True


# show(grid)
startLoc = getTarget(grid, 's')
visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
answer = 'Yes' if canReachGoal(grid, visited, startLoc[0], startLoc[1]) else 'No'
# print('startLoc', startLoc)
print(answer)
