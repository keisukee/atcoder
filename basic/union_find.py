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

