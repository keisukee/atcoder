N, K = list(map(int, input().split()))
sleeps = []
for i in range(N):
    t = int(input())
    sleeps.append(t)

def getSpeepDeprivedDay(sleeps):
    accumulatedSleepTime = 0
    for i in range(N):
        if i <= 2:
            accumulatedSleepTime += sleeps[i]
        else:
            accumulatedSleepTime -= sleeps[i-3]
            accumulatedSleepTime += sleeps[i]

        if i >= 2 and accumulatedSleepTime < K:
            print(i+1)
            return

    print(-1)
    return

getSpeepDeprivedDay(sleeps)