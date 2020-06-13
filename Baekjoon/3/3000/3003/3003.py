# chess[0] : King(max 1)
# chess[1] : Queen(max 1)
# chess[2] : Rook(max 2)
# chess[3] : Knight(max 2)
# chess[4] : Bishop(max 2)
# chess[5] : Pawn(max 8)
chess = [1, 1, 2, 2, 2, 8]
arr = list(map(int, input().split()))
if len(arr) < 6:
    print("기물의 갯수가 초과 되었습니다.")
else:
    for i in range(len(arr)):
        print(str.format("{0} ", chess[i] - arr[i]), end='')