height, width = list(map(int, input().split()))
board = []

for i in range(height):
    row = list(input())
    board.append(row)

def show(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end='')
        print()

def remove(board):
    for row in range(len(board)):
        doRemove = True
        for col in range(len(board[0])):
            if board[row][col] != '#':
                continue
            else:
                doRemove = False
                break
        if doRemove:
            for col in range(len(board[0])):
                board[row][col] = '-'

    for col in range(len(board[0])):
        doRemove = True
        for row in range(len(board)):
            if board[row][col] != '#':
                continue
            else:
                doRemove = False
                break
        if doRemove:
            for row in range(len(board)):
                board[row][col] = '-'

def extract(board):
    extractedBoard = []
    for row in board:
        filteredRow = list(filter(lambda x: x != '-', row))
        if len(filteredRow) > 0:
            extractedBoard.append(filteredRow)

    return extractedBoard

remove(board)
extractedBoard = extract(board)
# show(board)
show(extractedBoard)