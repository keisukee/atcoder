a, b, c = list(map(int, input().split()))

result = a ** 2 + b ** 2 < c ** 2

if result:
    print('Yes')
else:
    print('No')