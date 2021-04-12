import sys
sys.setrecursionlimit(10**6)

n = int(input())
c = list(map(int, input().split()))
graph = [[] for _ in range(n)]

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

ans = []
check = [0]*(10**5+1)


def dfs(i, pre):
    color = c[i]
    print(i, check[color])
    if check[color] == 0:
        ans.append(i+1)
    check[color] += 1
    for pro in graph[i]:
        if pro == pre:
            continue
        dfs(pro, i)
    check[color] -= 1


dfs(0, -1)
ans.sort()
print(*ans, sep='\n')
