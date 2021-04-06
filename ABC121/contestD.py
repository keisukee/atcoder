a, b = list(map(int, input().split()))

def quickContinuousXOR(n):
    length = n + 1
    # if n % 2 == 0:
    #     if (n // 2) % 2 == 0:
    #         pass
    #     else:
    # else:

    if length % 4 == 0:
        return 0
    elif length % 4 == 1:
        return 0 ^ n
    elif length % 4 == 2:
        return 1
    else:
        return 1 ^ n

# print('a', quickContinuousXOR(a))
# print('b', quickContinuousXOR(b))
print(quickContinuousXOR(a-1) ^ quickContinuousXOR(b))