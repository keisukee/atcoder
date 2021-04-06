N = int(input())
heights = list(map(int, input().split()))

result = 0
while True:
    i = 0
    if max(heights) == 0: break

    while i < N:
        if heights[i] == 0:
            i += 1
        else:
            result += 1
            while i < N and heights[i] > 0:
                heights[i] -= 1
                i += 1


print(result)



