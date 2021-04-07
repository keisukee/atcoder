from math import gcd

N, X = list(map(int, input().split()))
points = list(map(lambda x: int(x) - X, input().split()))

maxDistance = abs(points[0])
for num in points:
    maxDistance = gcd(maxDistance, num)

print(maxDistance)