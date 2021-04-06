N, X = list(map(int, input().split()))

a_n, p_n = [1], [1]
for i in range(N):
    a_n.append(a_n[i] * 2 + 3)
    p_n.append(p_n[i] * 2 + 1)


def calc(level, X, a_n, p_n):
    if level == 0:
        return 0 if X <= 0 else 1
    elif X <= 1+a_n[level-1]:
        return calc(level-1, X-1, a_n, p_n)
    else:
        return p_n[level-1] + 1 + calc(level-1, X-a_n[level-1]-2, a_n, p_n)


count = calc(N, X, a_n, p_n)

print(count)
