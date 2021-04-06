import math
N = int(input())
minutesToTake = []
for i in range(5):
    data = int(input())
    minutesToTake.append(data)

smallestCapacity = minutesToTake[0]
smallestCapacityIdx = 0
for i in range(1, len(minutesToTake)):
    if smallestCapacity > minutesToTake[i]:
        smallestCapacity = minutesToTake[i]
        smallestCapacityIdx = i

totalTime = math.ceil(N / smallestCapacity) + len(minutesToTake) - 1
print(totalTime)