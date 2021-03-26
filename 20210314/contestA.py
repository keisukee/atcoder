# 7
# 3 4 6 7 8 9 10

N = int(input())
nums = list(map(int, input().split()))

nums.sort()
def getMinDivisor(num, divisors):
    for d in divisors:
        if num % d == 0:
            return d

    for i in range(2, num+1):
        if num % i == 0:
            return i

minValue = float('inf')
# def backtrack(divisorItems, currentIdx, counter, currentVal, nums):
#     if currentIdx == len(divisorItems):
#         return

#     print('currentIdx', currentIdx, currentVal, len(counter))
#     for i in range(currentIdx, len(divisorItems)):
#         valToMul, originals = divisorItems[i]
#         for x in originals:
#             counter[x] = True
#         backtrack(divisorItems, currentIdx+1, counter.copy(), currentVal*valToMul, nums)
#         for x in originals:
#             del counter[x]

#     return

divisors = set()
for num in nums:
    val = getMinDivisor(num, divisors)
    divisors.add(val)



# print('divisors', divisors)
ans = 1
for d in divisors:
    ans *= d

print(ans)
