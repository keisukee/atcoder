N = int(input())
K = int(input())

remainNodes = N-1
maxSeparetedNodes = 0
if remainNodes % 2 == 0:
    maxSeparetedNodes = (remainNodes) // 2
else:
    maxSeparetedNodes = (remainNodes) // 2 + 1

if maxSeparetedNodes >= K:
    print("YES")
else:
    print("NO")

