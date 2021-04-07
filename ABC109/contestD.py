H, W = list(map(int, input().split()))
board = [[0 for _ in range(W)] for _ in range(H)]

for h in range(H):
    board[h] = list(map(int, input().split()))


def show(board):
    for i in range(len(board)):
        print(board[i])


# show(board)
# print()


def maximizeEvenCount(board):
    moves = []
    for h in range(len(board)):
        for w in range(len(board[0])):
            if board[h][w] % 2 == 1:
                if w+1 < len(board[0]) and board[h][w+1] % 2 == 1:
                    board[h][w] -= 1
                    board[h][w+1] += 1
                    moves.append([h+1, w+1, h+1, w+2])
                elif h+1 < len(board):
                    board[h][w] -= 1
                    board[h+1][w] += 1
                    moves.append([h+1, w+1, h+2, w+1])

    return moves

# def countEven(board):
#     evenCount = 0
#     for i in range(len(board)):
#         for j in range(len(board[0])):
#             if board[i][j] % 2 == 0:
#                 evenCount += 1
#     return evenCount


moves = maximizeEvenCount(board)
# evenCount = countEven(board)
# show(board)

print(len(moves))
for move in moves:
    for loc in move:
        print(loc, end=' ')
    print()


