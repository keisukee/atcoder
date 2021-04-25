N = int(input())
sequences_A = list(map(int, input().split()))
sequences_B = list(map(int, input().split()))

required_range = [max(sequences_A), min(sequences_B)]
# print('required_range', required_range)
count = max(0, required_range[1] - required_range[0] + 1)
print(count)



