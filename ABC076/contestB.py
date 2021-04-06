N = int(input())
K = int(input())
value = 1
for i in range(N):
    if 2 * value > value + K:
        value += K
    else:
        value *= 2

print(value)