A, B = list(map(int, input().split()))

currentCount = 1
powerStripCount = 0
while currentCount < B:
    currentCount -= 1
    powerStripCount += 1
    currentCount += A

print(powerStripCount)
