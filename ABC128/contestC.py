N, M = map(int, input().split())
s = [list(map(int, input().split()))[1:] for m in range(M)]
p = list(map(int, input().split()))
count = 0

for i in range(2**N):
    isValid = True
    for m in range(M):
        switch = 0
        for j in range(N):
            if (i >> j & 1) and j+1 in s[m]:
                switch += 1
        if switch % 2 != p[m]:
            isValid = False
            break
    if isValid:
        count += 1
