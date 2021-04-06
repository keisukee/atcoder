import sys
sys.setrecursionlimit(500000)

N, M =  list(map(int, input().split()))
brokenFloors = set()
for i in range(M):
    data = int(input())
    brokenFloors.add(data)

def calcTotalWays(step, brokenFloors, memo):
    if step in brokenFloors:
        return 0
    if step in memo:
        return memo[step]

    ways = calcTotalWays(step-1, brokenFloors, memo) + calcTotalWays(step-2, brokenFloors, memo)
    memo[step] = ways
    return ways

memo = {0: 1, 1: 1}
ways = calcTotalWays(N, brokenFloors, memo)
print(ways % 1000000007)


