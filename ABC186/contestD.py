N = int(input())
sequences = list(map(int, input().split()))
sequences.sort()

diffs = [0]
for i in range(1, len(sequences)):
    prev_diff = diffs[i-1]
    diffs.append(prev_diff + sequences[i] - sequences[i-1])

# print(diffs)
first_sum = sum(diffs)
diff_sum = first_sum
for i in range(1, len(sequences)):
    diff = sequences[i] - sequences[i-1]
    first_sum -= (diff * (len(sequences)-i))
    diff_sum += first_sum

print(diff_sum)