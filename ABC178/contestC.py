N = int(input())
value = 10**9 + 7
if N == 1:
    print(0)
else:
    answer = 10 ** N - (9**N + 9**N - 8**N)
    print(answer % value)