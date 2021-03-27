N = int(input())
nums = list(map(int, input().split()))
minValue = float('inf')
from functools import reduce

def backtrack(nums, idx, pattern):
    global minValue
    if minValue == 0:
        return

    if idx == len(nums):
        currentXOR = reduce(lambda i, j: int(i) ^ int(j), pattern) # get xor
        minValue = min(minValue, currentXOR)

    for i in range(idx, len(nums)):
        lastPart = nums[idx : i+1]
        lastPartOR = reduce(lambda i, j: int(i) | int(j), lastPart) # get or
        pattern.append(lastPartOR)
        backtrack(nums, i+1, pattern)
        pattern.pop()
    return

backtrack(nums, 0, [])
print(minValue)
