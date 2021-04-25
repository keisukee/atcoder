import math
r, x, y = list(map(int, input().split()))

distance = math.sqrt(x**2 + y**2)
if distance < r:
    steps = 2
else:
    steps = int((distance // r))
    remain = 1 if distance % r != 0 else 0
    steps += remain
print(steps)
