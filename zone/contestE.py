import sys
sys.setrecursionlimit(500000)
from itertools import permutations

R, C = list(map(int, input().split()))
col_cost = []
row_cost = []
for i in range(R):
    data = list(map(int, input().split()))
    col_cost.append(data)

for i in range(R-1):
    data = list(map(int, input().split()))
    row_cost.append(data)

R -= 1
C -= 1
min_cost = float('inf')

def get_min_cost(row, col, target_row, target_col, col_cost, row_cost, visited, cost):
    global min_cost
    if row == target_row and col == target_col:
        min_cost = min(min_cost, cost)
        print(visited)
        print('min_cost', min_cost)
        return

    if cost > min_cost:
        return

    right = [row, col+1, col_cost[row][col]] if col < target_col else [row, col+1, float('inf')]
    left = [row, col-1, col_cost[row][col-1]] if col-1 >= 0 else [row, col-1, float('inf')]
    up = [row+1, col, row_cost[row][col]] if row < target_row else [row+1, col, float('inf')]
    down = [row-1, col, 2] if row-1 >= 0 else [row-1, col, float('inf')]

    visited[(row, col)] = True
    print(row, col, cost)
    next_locations = [right, left, up, down]
    for next_row, next_col, next_cost in next_locations:
        is_in_range = 0 <= next_row <= target_row and 0 <= next_col <= target_col

        if is_in_range and (next_row, next_col) not in visited:
            get_min_cost(next_row, next_col, target_row, target_col, col_cost, row_cost, visited, cost + next_cost)

    del visited[(row, col)]

visited = {}
get_min_cost(0, 0, R, C, col_cost, row_cost, visited, 0)

print(min_cost)
