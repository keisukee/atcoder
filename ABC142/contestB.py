N, K = list(map(int, input().split()))
heights = list(map(int, input().split()))

count = len(list(filter(lambda x: x >= K, heights)))
print(count)