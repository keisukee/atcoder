N, K = list(map(int, input().split()))
nums = []
for i in range(N):
    data = int(input())
    nums.append(data)

startIdx = 0
currentProduct = 1
maxLength = 0
for i in range(len(nums)):
    if nums[i] == 0:
        maxLength = len(nums)
        break

    currentProduct *= nums[i]
    if currentProduct > K:
        currentProduct //= nums[startIdx]
        startIdx += 1
    else:
        currentLength = i - startIdx + 1
        maxLength = max(maxLength, currentLength)

print(maxLength)

