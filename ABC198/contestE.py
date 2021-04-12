import sys
sys.setrecursionlimit(10**6)

N = int(input())
C = [int(x) for x in input().split()]

colors = [0 for _ in range(10 ** 5 + 1)]
good = [False for _ in range(N)]

def dfs(edges, parent, root):
    global colors, good

    if colors[C[root]] == 0:
        good[root] = True

    colors[C[root]] += 1
    for tip in edges[root]:
        if tip != parent:
            dfs(edges, root, tip)
    colors[C[root]] -= 1


edges = [list() for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges[a].append(b)
    edges[b].append(a)


dfs(edges, -1, 0)

for i in range(N):
    if good[i]:
        print(i + 1)
