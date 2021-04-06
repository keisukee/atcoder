N, Q = list(map(int, input().split()))
string = list(input())
wordAppearance = [0 for i in range(N)]

for i in range(1, len(string)):
    if string[i-1] == 'A' and string[i] == 'C':
        wordAppearance[i] = wordAppearance[i-1] + 1
    else:
        wordAppearance[i] = wordAppearance[i-1]

for i in range(Q):
    l, r = list(map(int, input().split()))
    print(wordAppearance[r-1] - wordAppearance[l-1])
