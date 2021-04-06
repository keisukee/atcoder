N = int(input())
a, b = list(map(int, input().split()))
K = int(input())
path = list(map(int, input().split()))
uniquePath = set(path)

if len(uniquePath) != len(path) or a in uniquePath or b in uniquePath:
    print('NO')
else:
    print('YES')
