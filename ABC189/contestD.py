N = int(input())
expressions = []
for i in range(N):
    flip = input()
    expressions.append(flip)

def count_all_pattern(expressions, end_idx):
    count = 0
    if end_idx == -1:
        return 1
    if expressions[end_idx] == 'AND':
        count += count_all_pattern(expressions, end_idx-1)
    elif expressions[end_idx] == 'OR':
        count += 2**(end_idx+1) + count_all_pattern(expressions, end_idx-1)

    return count

pattern_count = count_all_pattern(expressions, len(expressions)-1)
print(pattern_count)