from math import gcd
N = int(input())
data = list(map(int, input().split()))

fromLeft, fromRight = [0] * N, [0] * N
fromLeft[0] = data[0]
fromRight[-1] = data[-1]
for i in range(1, N):
    fromLeft[i] = gcd(fromLeft[i-1], data[i])

for i in reversed(range(0, N-1)):
    fromRight[i] = gcd(fromRight[i+1], data[i])

# print('data', data)
# print('fromLeft', fromLeft)
# print('fromRight', fromRight)

maxGCD = float('-inf')
for i in range(N):
    if i == 0:
        maxGCD = max(maxGCD, fromRight[i+1])
    elif i == N-1:
        maxGCD = max(maxGCD, fromLeft[i-1])
    else:
        maxGCD = max(maxGCD, gcd(fromLeft[i-1], fromRight[i+1]))

print(maxGCD)
