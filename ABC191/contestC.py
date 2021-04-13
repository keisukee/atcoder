
H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
for h in range(1, H):
    for w in range(1, W):
        cnt = 0
        for i in range(2):
            for j in range(2):
                if S[h - i][w - j] == '#':
                    cnt += 1
        if cnt % 2 == 1:
            # for i in reversed(range(2)):
            #     for j in reversed(range(2)):
            #         print(S[h-i][w-j], end='')
            #     print('')
            # print(h, w)
            # print('===========')

            ans += 1
print(ans)