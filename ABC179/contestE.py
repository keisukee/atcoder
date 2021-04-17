N, X, M = map(int, input().split())
a = X
d = set([X])
X_squared = [X]
for _ in range(N-1):
    a = a ** 2 % M
    if a in d:
        break
    d.add(a)
    X_squared.append(a)
start_idx = X_squared.index(a)
repeat = (N - start_idx) // (len(X_squared) - start_idx)
res = (N - start_idx) % (len(X_squared) - start_idx)
# print(start_idx, repeat, res)
ans = 0
for i in range(len(X_squared)):
    if i < start_idx:
        ans += X_squared[i]
    else:
        ans += X_squared[i] * repeat
if res > 0:
    a = X_squared[-1]
    for _ in range(res):
        a = a**2 % M
        ans += a
print(ans)
