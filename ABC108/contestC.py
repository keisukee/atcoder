N, K = map(int, input().split())
num = 0
num2 = 0
count = 0
if K % 2 == 0:
    for i in range(N):
        if (i+1) % K == 0:
            num += 1
    for i in range(N):
        if (i+1) % K == K // 2:
            num2 += 1
    count = num + num*(num-1)*3 + num*(num-1)*(num-2) + num2 + num2*(num2-1)*3 + num2*(num2-1)*(num2-2)
else:
    for i in range(N):
        if (i+1) % K == 0:
            num += 1
    count = num + num*(num-1)*3 + num*(num-1)*(num-2)

print(count)
