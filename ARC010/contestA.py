N, M, A, B = list(map(int, input().split()))
canComplete = True
for i in range(1, M+1):
    cardCount = int(input())
    if not canComplete:
        continue
    if N <= A:
        N += B

    if N < cardCount:
        print(i)
        canComplete = False
    else:
        N -= cardCount

if canComplete:
    print('complete')
