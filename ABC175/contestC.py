X, K, D = list(map(int, input().split()))

X = abs(X)

reach_zero_count = X // D

answer = 0
if reach_zero_count >= K:
    answer = abs(X - (K * D))
else:
    remain_count = K - reach_zero_count
    current_location = abs(X - reach_zero_count * D)
    if remain_count % 2 == 0:
        answer = current_location
    else:
        current_location = abs(current_location - D)
        answer = current_location

print(answer)

