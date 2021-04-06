N, M = list(map(int, input().split()))
points = list(map(int, input().split()))
points.sort()
distances = []
endToEnd = points[-1] - points[0]

if N >= M:
    print(0)
    exit()

for i in range(1, len(points)):
    d = points[i] - points[i-1]
    distances.append(d)

# print('points', points)
# print('before distances', distances)
distances.sort(key = lambda x: -x)
for i in range(N-1):
    endToEnd -= distances[i]
# print('after distances', distances)

print(endToEnd)




