N, x = list(map(int, input().split()))
boxes = list(map(int, input().split()))

eatCount = 0
if boxes[0] > x:
    eatCount += boxes[0]-x
    boxes[0] -= (boxes[0]-x)

for i in range(1, N):
    if boxes[i-1] + boxes[i] > x:
        diff = boxes[i-1] + boxes[i] - x
        boxes[i] -= diff
        eatCount += diff

print(eatCount)

