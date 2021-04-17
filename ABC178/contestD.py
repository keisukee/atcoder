S = int(input())

# 3以上の組み合わせで
def get_all_patterns_added_up_to_N(N, cache):
    if N in cache:
        return cache[N]
    if N == 0:
        return 1
    if N < 3:
        return 0

    count = 0
    for i in range(3, N+1):
        count += get_all_patterns_added_up_to_N(N - i, cache)

    cache[N] = count
    return cache[N]

cache = {}
divider = 10**9 + 7
# for i in range(3, S+1):
#     print(i)
count = get_all_patterns_added_up_to_N(S, cache)
print(count % divider)


