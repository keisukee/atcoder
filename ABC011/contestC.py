N = int(input())
prohibitedNums = set()
for i in range(3):
    d = int(input())
    prohibitedNums.add(d)

canFinish = True
for i in range(100):
    if N in prohibitedNums:
        canFinish = False
        break
    if N - 3 not in prohibitedNums:
        N -= 3
    elif N - 2 not in prohibitedNums:
        N -= 2
    elif N - 1 not in prohibitedNums:
        N -= 1
    else:
        canFinish = False
        break

canFinish &= N <= 0
if canFinish:
    print('YES')
else:
    print('NO')
