N = int(input())
cities = list(map(int, input().split()))
savers = list(map(int, input().split()))

count = 0
for i in range(len(savers)):
    if cities[i] < savers[i]:
        savers[i] -= cities[i]
        count += cities[i]

        if cities[i+1] > savers[i]:
            cities[i+1] -= savers[i]
            count += savers[i]
        else:
            count += cities[i+1]
            cities[i+1] = 0
    else:
        count += savers[i]

print(count)

