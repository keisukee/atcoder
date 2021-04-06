N = int(input())
steps =  list(map(int, input().split()))
dp = [0] * N
dp[1] = abs(steps[1]-steps[0])
for i in range(2, N):
    dp[i] = min(dp[i-1] + abs(steps[i]-steps[i-1]), dp[i-2] + abs(steps[i]-steps[i-2]))

print(dp[-1])

