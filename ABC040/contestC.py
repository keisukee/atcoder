N = int(input())
pillars = list(map(int, input().split()))
minMovementCost = [0] * N

minMovementCost[1] = abs(pillars[1]-pillars[0])
for i in range(2, N):
    minMovementCost[i] = min(minMovementCost[i-1] + abs(pillars[i]-pillars[i-1]), minMovementCost[i-2] + abs(pillars[i]-pillars[i-2]))

print(minMovementCost[-1])



