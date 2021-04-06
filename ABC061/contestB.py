N, M = list(map(int, input().split()))
roads = [[] for i in range(N)]
for i in range(M):
    a, b = list(map(int, input().split()))
    roads[a-1].append(b-1)
    roads[b-1].append(a-1)

for i in range(N):
    print(len(roads[i]))