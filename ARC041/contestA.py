x, y = list(map(int, input().split()))
k = int(input())

answer = 0
if k <= y:
    answer = x+k
else:
    remain = k-y
    answer = y + (x-remain)

print(answer)