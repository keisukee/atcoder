dishes = []
for i in range(5):
    data = int(input())
    dishes.append(data)

minTime = float('inf')
def getPermutation(dishes, currentIdx, allPatterns):
    if currentIdx == len(dishes):
        allPatterns.append(dishes[:])
        return

    for i in range(currentIdx, len(dishes)):
        dishes[currentIdx], dishes[i] = dishes[i], dishes[currentIdx]
        getPermutation(dishes, currentIdx+1, allPatterns)
        dishes[currentIdx], dishes[i] = dishes[i], dishes[currentIdx]

    return

def getMinTime(patterns):
    minTime = float('inf')
    for pattern in patterns:
        currentTime = 0
        for i in range(len(pattern)):
            currentTime += pattern[i]
            if i != len(pattern)-1 and currentTime % 10 != 0:
                currentTime += (10 - currentTime % 10)

        minTime = min(minTime, currentTime)
    return minTime

allPatterns = []
getPermutation(dishes, 0, allPatterns)

minTime = getMinTime(allPatterns)
print(minTime)
