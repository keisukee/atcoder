from collections import deque
n = int(input())
array = list(map(int, input().split()))
answer = deque()

for i, num in enumerate(array):
    if i % 2 == 0:
        answer.append(str(num))
    else:
        answer.appendleft(str(num))

if n % 2 != 0:
    answer.reverse()
print(' '.join(answer))

