N = int(input())
toFlipNums = list(map(int, input().split()))

def getMaxSum(toFlipNums):
    maxSums = [[None, None] for _ in range(len(toFlipNums)+1)]

    maxSums[0][0] = 0
    maxSums[0][1] = float('-inf')

    for i in range(len(toFlipNums)):
        maxSums[i+1][0] = max(maxSums[i][0] + toFlipNums[i], maxSums[i][1] - toFlipNums[i])
        maxSums[i+1][1] = max(maxSums[i][0] - toFlipNums[i], maxSums[i][1] + toFlipNums[i])

    # print('maxSums', maxSums)
    return maxSums[-1][0]

print(getMaxSum(toFlipNums))




