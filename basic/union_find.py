def root(parent, x):
    print('parent of x is', x, parent[x])
    if parent[x] == x:
        return x
    else:
        parent[x] = root(parent, parent[x])
        return parent[x]

def isSame(x, y, parent):
    return root(parent, x) == root(parent, y)

def unite(x, y, parent):
    x = root(parent, x)
    y = root(parent, y)
    if x == y:
        return
    parent[x] = y
    print('parent', parent)

N, Q = list(map(int, input().split()))

parent = [i for i in range(N)]
for q in range(Q):
    p, a, b = list(map(int, input().split()))
    if p == 0: # 連結クエリ
        unite(a, b, parent)
    elif p == 1: # 判定クエリ
        if isSame(a, b, parent):
            print('Yes')
        else:
            print('No')


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

