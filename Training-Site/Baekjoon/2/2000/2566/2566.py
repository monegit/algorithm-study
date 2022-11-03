import sys

board = []
px = 1
py = 1
max = 0
for i in range(9):
    board.append(list(map(int, sys.stdin.readline().split())))

for y in range(9):
    for x in range(9):
        if (board[y][x] > max):
            max = board[y][x]
            px = x+1
            py = y+1

print(max)
print(py, px)
