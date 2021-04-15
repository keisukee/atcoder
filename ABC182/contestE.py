height, width, N, M = list(map(int, input().split()))
grid = [['-' for _ in range(width)] for _ in range(height)]
light_map = [[False for _ in range(width)] for _ in range(height)]

for i in range(N):
    a, b = list(map(int, input().split()))
    grid[a-1][b-1] = '.'

for i in range(M):
    c, d = list(map(int, input().split()))
    grid[c-1][d-1] = '#'

def show(grid):
    for row in grid:
        print(row)

def count_light(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                count += 1
    return count

def traverse(grid, light_map):
    for i in range(len(grid)):
        see_light = False
        for j in range(len(grid[0])):
            if grid[i][j] == '.':
                see_light = True
            elif grid[i][j] == '#':
                see_light = False
            if not light_map[i][j]:
                light_map[i][j] = see_light

        see_light = False
        for j in reversed(range(len(grid[0]))):
            if grid[i][j] == '.':
                see_light = True
            elif grid[i][j] == '#':
                see_light = False

            if not light_map[i][j]:
                light_map[i][j] = see_light

    for j in range(len(grid[0])):
        see_light = False
        for i in range(len(grid)):
            if grid[i][j] == '.':
                see_light = True
            elif grid[i][j] == '#':
                see_light = False
            if not light_map[i][j]:
                light_map[i][j] = see_light

        see_light = False
        for i in reversed(range(len(grid))):
            if grid[i][j] == '.':
                see_light = True
            elif grid[i][j] == '#':
                see_light = False
            if not light_map[i][j]:
                light_map[i][j] = see_light

traverse(grid, light_map)
answer = count_light(light_map)
# show(light_map)
print(answer)
# def traverse(grid, light_map, visited, row, col):
#     stack = []
#     for current_row in reversed(range(0, row)):
#         if grid[current_row][col] == '#':
#             break
#         if (current_row, col) in visited:
#             continue
#         stack.append([current_row, col])

#     for current_row in range(row, len(grid)):
#         if grid[current_row][col] == '#':
#             break
#         if (current_row, col) in visited:
#             continue
#         stack.append([current_row, col])

#     for current_col in reversed(range(0, len(grid[0]))):
#         if grid[row][current_col] == '#':
#             break
#         if (row, current_col) in visited:
#             continue
#         stack.append([row, current_col])

#     for current_col in range(col, len(grid[0])):
#         if grid[row][current_col] == '#':
#             break
#         if (row, current_col) in visited:
#             continue
#         stack.append([row, current_col])

#     while stack:
#         current_row, current_col = stack.pop()
#         visited[(current_row, current_col)] = True
#         light_map[current_row][current_col] = True
#     return

# # show(grid)
# visited = {}
# for row in range(len(grid)):
#     for col in range(len(grid[0])):
#         if (row, col) not in visited and grid[row][col] == '.':
#             traverse(grid, light_map, visited, row, col)

# # show(light_map)
# answer = count_light(light_map)
# print(answer)


