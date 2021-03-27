H, W, X, Y = map(int,input().split())
board = []

for i in range(H):
    row = input()
    board.append(list(row))

# for i in range(H):
#     print(board[i])

count = 0

# print('board[X-1]', board[X-1])
# print('board[X-1][Y-1]', board[X-1][Y-2], board[X-1][Y-1], board[X-1][Y])

fixedX, fixedY = X-1, Y-1
def show(board, i, j):
    print('i, j', i, j, board[i][j])
for i in reversed(range(0, fixedX)):
    if board[i][fixedY] == '.':
        # show(board, i, fixedY)
        count += 1
    else:
        break
for i in range(fixedX, H):
    if board[i][fixedY] == '.':
        # show(board, i, fixedY)
        count += 1
    else:
        break

for i in reversed(range(0, fixedY)):
    if board[fixedX][i] == '.':
        # show(board, fixedX, i)
        count += 1
    else:
        break
for i in range(fixedY, W):
    if board[fixedX][i] == '.':
        # show(board, fixedX, i)
        count += 1
    else:
        break

print(count-1)


