# need = {
#     1: 2,
#     2: 5,
#     3: 5,
#     4: 4,
#     5: 5,
#     6: 6,
#     7: 3,
#     8: 7,
#     9: 6
# }

# N, M =  list(map(int, input().split()))
# choice = list(map(int, input().split()))

# dp = [[0 for _ in range(N+1)] for _ in range(len(choice)+1)]

# for i, value in enumerate(choice, 1):
#     needCount = need[value]
#     for j in range(1, N+1):
#         if needCount >= j:
#             num1 = int(str(value) + str(dp[i][j-needCount]))
#             num2 = int(str(dp[i][j-needCount]) + str(value))
#             num3 = int(str(dp[i-1][j])) if dp[i-1][j] != '' else 0
#             print('num1, num2, num3', num1, num2, num3)
#             dp[i][j] = str(max(num1, num2, num3))
#         else:
#             num1 = int(dp[i-1][j]) if dp[i-1][j] != '' else 0
#             num2 = int(dp[i][j-1]) if dp[i][j-1] != '' else 0
#             maxValue = max(num1, num2)
#             dp[i][j] = str(maxValue) if maxValue > 0 else ''

# for i in range(len(dp)):
#     print(dp[i])


N, M = map(int, input().split())
A = list(map(int, input().split()))
weight = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
dp = [-1]*(N+1)
dp[0] = 0
for i in range(N+1):
    for a in A:
        if i+weight[a] < N+1:
            dp[i+weight[a]] = max(dp[i+weight[a]], dp[i]*10+a)
print(dp)
print(dp[N])
