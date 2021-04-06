import math
N = int(input())
data = list(map(int, input().split()))

commonDivider = data[0]
for i in range(1, len(data)):
    commonDivider = math.gcd(commonDivider, data[i])

print(commonDivider)


