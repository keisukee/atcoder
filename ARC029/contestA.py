N = int(input())
meats = []

totalTime = 0
for i in range(N):
    data = int(input())
    totalTime += data
    meats.append(data)

minTime = totalTime
def calcMinTime(meats, currentIdx, totalTime, currentTime):
    global minTime
    # print('totalTime, currentTime', totalTime, currentTime)
    if currentIdx == len(meats):
        minTime = min(minTime, max(totalTime - currentTime, currentTime))
        return

    calcMinTime(meats, currentIdx+1, totalTime, currentTime)
    calcMinTime(meats, currentIdx+1, totalTime, currentTime + meats[currentIdx])
    return

calcMinTime(meats, 0, totalTime, 0)
print(minTime)
