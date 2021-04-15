N = int(input())
sequences = list(map(int, input().split()))
cumulative_sums = [0] * (N+1)
sums_max = [0] * (N+1)

for i in range(len(sequences)):
    cumulative_sums[i+1] = sequences[i] + cumulative_sums[i]
    sums_max[i+1] = max(sums_max[i], cumulative_sums[i+1])

current_loc = 0
loc_max = 0
for i in range(len(sequences)):
    loc_max = max(loc_max, current_loc + sums_max[i+1])
    current_loc += cumulative_sums[i+1]
# for i in range(len(cumulative_sums)):
#     current_loc += cumulative_sums[i]
    # print(current_loc, end=' ')
    # locations.append(cumulative_sums[i] + locations[i])



# print('sequences', sequences)
# print('cumulative_sums', cumulative_sums)
# print('sums_max', sums_max)
print(loc_max)