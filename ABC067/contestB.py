N, K = list(map(int, input().split()))
sticks = list(map(int, input().split()))
sticks.sort(key = lambda x: -x)
result = sum(sticks[:K])
print(result)