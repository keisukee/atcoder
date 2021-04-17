import sys
class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

N, M = map(int, input().split())
info = [tuple(map(int, s.split())) for s in sys.stdin.readlines()]

union_find_tree = UnionFind(N)
for a, b in info:
    a -= 1; b -= 1
    union_find_tree.union(a, b)

ans = min(union_find_tree.parents)

print(-ans)
