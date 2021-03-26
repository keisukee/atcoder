H, W, A, B = list(map(int, input().split()))

dp = [[0 for i in range(W)] for j in range(H)]

def show(dp):
    for i in range(len(dp)):
        print(dp[i])

    print('===========')

def dfs(dp, remain, i, j, width, height):
    if remain == 0:
        # show(dp)
        return 1

    if i == height:
        return 1 if remain == 0 else 0
    if j == width:
        return dfs(dp, remain, i+1, 0, width, height)

    if dp[i][j] == 1:
        return dfs(dp, remain, i, j+1, width, height)

    totalCount = 0
    if j+1 < width and dp[i][j+1] == 0 and remain > 0:
        dp[i][j], dp[i][j+1] = 1, 1
        totalCount += dfs(dp, remain-1, i, j+1, width, height)
        dp[i][j], dp[i][j+1] = 0, 0

    if i+1 < height and dp[i+1][j] == 0 and remain > 0:
        dp[i][j], dp[i+1][j] = 1, 1
        totalCount += dfs(dp, remain-1, i, j+1, width, height)
        dp[i][j], dp[i+1][j] = 0, 0

    totalCount += dfs(dp, remain, i, j+1, width, height)
    return totalCount

# def dfs(dp, remain, currentX, currentY, width, height, visited):
#     global totalCount

#     visited[currentY][currentX] = True

#     if remain == 0:
#         show(dp)
#         totalCount += 1
#         return

#     if currentX == width-1 and currentY == height-1:
#         return

#     for i in range(currentY, height):
#         for j in range(currentX, width):
#             if j+1 < width and dp[i][j] == 0 and dp[i][j+1] == 0:
#                 dp[i][j], dp[i][j+1] = 1, 1
#                 dfs(dp, remain-1, j, i, width, height, visited)
#                 dp[i][j], dp[i][j+1] = 0, 0

#             if i+1 < height and dp[i][j] == 0 and dp[i+1][j] == 0:
#                 dp[i][j], dp[i+1][j] = 1, 1
#                 dfs(dp, remain-1, j, i, width, height, visited)
#                 dp[i][j], dp[i+1][j] = 0, 0

#     return


visited = [[False for i in range(W)] for j in range(H)]

print(dfs(dp, A, 0, 0, W, H))