N = int(input())

total_expected_value = 0

for i in range(1, N):
    total_expected_value += N/(N-i)

print(total_expected_value)