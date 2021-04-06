N = int(input())

conditions = []
minHeight = 0
for i in range(N):
    x, y, h = list(map(int, input().split()))
    minHeight = max(minHeight, h)
    conditions.append([x, y, h])

def findCoordinate(conditions, cx, cy, maxHeight):
    # print('cx, cy, maxHeight', cx, cy, maxHeight)

    for i in range(len(conditions)):
        x, y, h = conditions[i]
        if h != max(maxHeight - abs(cx-x) - abs(cy-y), 0):
            return False

    return True

currentHeight = minHeight
while True:
    for cx in range(101):
        for cy in range(101):
            if findCoordinate(conditions, cx, cy, currentHeight):
                print(cx, cy, currentHeight)
                exit()
    currentHeight += 1
