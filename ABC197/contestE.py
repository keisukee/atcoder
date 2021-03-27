N = int(input())

balls = []
for i in range(N):
    coordinate, color = list(map(int, input().split()))
    balls.append([coordinate, color])

balls.sort(key = lambda x: (x[1], x[0]))

def joinRange(balls):
    joinedRange = []
    locL, color = balls[0]
    locR = locL
    idx = 1
    while idx < len(balls):
        while idx < len(balls) and color == balls[idx][1]:
            locR = balls[idx][0]
            idx += 1
        joinedRange.append([locL, locR])
        if idx >= len(balls):
            break
        locL, color = balls[idx]
        locR = locL
    return joinedRange

joinedRange = joinRange(balls)

print('balls', balls)
print('joinedRange', joinedRange)

def getMinMove(joinedRange):
    dp = [[0, 0] for i in range(len(joinedRange))]
    prevLeft, prevRight = joinedRange[0]
    dp[0] = [abs(prevLeft), abs(prevRight)]
    for i in range(1, len(joinedRange)):
        l, r = joinedRange[i]
        print('prevLeft, prevRight', prevLeft, prevRight)
        print('l, r', l, r)
        # R -> L2 -> R2
        prlr = abs(prevRight-l) + abs(l-r)
        print('R -> L2 -> R2', prlr)

        # R -> R2 -> L2
        prrl = abs(prevRight-r) + abs(l-r)
        print('R -> R2 -> L2', prrl)

        # L -> L2 -> R2
        pllr = abs(prevLeft-l) + abs(l-r)
        print('L -> L2 -> R2', pllr)

        # L -> R2 -> L2
        plrl = abs(prevLeft-r) + abs(l-r)
        print('L -> R2 -> L2', plrl)

        prevLeftMove, prevRightMove = dp[i-1]
        curLeftMinMove = min(prevLeftMove + plrl, prevRightMove + prrl)
        curRightMinMove = min(prevLeftMove + pllr, prevRightMove + prlr)
        print('[prevLeftMove, prevRightMove]', [prevLeftMove, prevRightMove])
        print('[curLeftMinMove, curRightMinMove]', [curLeftMinMove, curRightMinMove])
        dp[i] = [curLeftMinMove, curRightMinMove]
        prevLeft, prevRight = l, r

    return dp

dp = getMinMove(joinedRange)

print('dp', dp)





