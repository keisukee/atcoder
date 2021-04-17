N = int(input())
coordinates = []
candidates = []

for i in range(N):
    x, y = list(map(int, input().split()))
    coordinates.append([x, y])

coordinates.sort(key = lambda x: (x[0], x[1]))
current_index = 0
while current_index < len(coordinates):
    x, y = coordinates[current_index]
    candidates.append([x, y])
    if current_index + 1 < len(coordinates) and x == coordinates[current_index+1][0]:
        while current_index < len(coordinates) and x == coordinates[current_index][0]:
            y = coordinates[current_index][1]
            current_index += 1

        candidates.append([x, y])
    else:
        current_index += 1

# print(coordinates)
# print(candidates)

max_manhattan_distance = 0
for i in range(len(candidates)-1):
    x1, y1 = candidates[i]
    for j in range(i+1, len(candidates)):
        x2, y2 = candidates[j]
        manhattan_distance = abs(x1-x2) + abs(y1-y2)
        max_manhattan_distance = max(manhattan_distance, max_manhattan_distance)

print(max_manhattan_distance)


