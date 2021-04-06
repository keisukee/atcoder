N = int(input())
heights =  list(map(int, input().split()))
dp = [0] * len(heights)

for i in range(1, N):
    if heights[i-1] >= heights[i]:
        dp[i] = dp[i-1] + 1

print(max(dp))

