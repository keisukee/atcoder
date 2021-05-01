from collections import deque
string = input()
queue = deque()

from_right = True
for i in range(len(string)):
    char = string[i]
    if char == 'R':
        from_right = not from_right
    else:
        if from_right:
            queue.append(char)
        else:
            queue.appendleft(char)

idx = 0
max_len = len(queue)

if from_right:
    queue = list(queue)
else:
    queue = list(reversed(queue))

stack = []

for i in range(len(queue)):
    char = queue[i]
    if not stack or stack[-1] != char:
        stack.append(char)
    else:
        stack.pop()

print(''.join(stack))
