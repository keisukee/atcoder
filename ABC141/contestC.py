N, K, Q = list(map(int, input().split()))
points = [K] * N

for i in range(Q):
    answer = int(input())
    points[answer-1] += 1

for point in points:
    if point-Q > 0:
        print('Yes')
    else:
        print('No')