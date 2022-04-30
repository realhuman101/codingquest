from numpy import broadcast_arrays


with open('practice/snakes-ladders/input.txt') as file: puzzle = [list(map(int,i.strip().split(' '))) for i in file.readlines()]

board = list(reversed([i for i in puzzle if len(i) > 2]))
steps = [i for i in puzzle if len(i) == 2]

game = []

for ind,row in enumerate(board):
    if ind % 2 != 0:
        for rowVal in reversed(row):
            game.append(rowVal)
    else:
        for rowVal in row:
            game.append(rowVal)

def findPlayer(board,steps,num):
    steps = list(map(lambda x: x[num-1],steps))
    piece = 0
    moves = 0
    for roll in steps:
        piece += roll
        moves += 1
        if piece < len(board):
            try:
                while board[piece] != 0:
                    piece += board[piece] if piece < len(board) else 0
            except Exception:
                pass
        if piece >= len(board):
            return moves
    return

print(findPlayer(game,steps,1))