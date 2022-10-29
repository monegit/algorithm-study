n, m = map(int, input().split())

min_count = 100
arr = []

for _ in range(n):
    arr.append(list(''.join(input())))

# 모델
board1 = []
board2 = []
for i in range(8):
    if (i % 2 == 0):
        board1.append('WBWBWBWB')
    else:
        board1.append('BWBWBWBW')

for i in range(8):
    if (i % 2 == 1):
        board2.append('WBWBWBWB')
    else:
        board2.append('BWBWBWBW')


for y in range(n-7):
    for x in range(m-7):
        paint = 0
        slicing = []
        # 8x8로 자른 배열
        for i in range(8):
            slicing.append(arr[i+y][0+x:8+x])

        # 칠하기
        count1 = 0
        count2 = 0
        for _y in range(8):
            for _x in range(8):
                if (slicing[_y][_x] != board1[_y][_x]):
                    count1 += 1
                if (slicing[_y][_x] != board2[_y][_x]):
                    count2 += 1

        paint = min(count1, count2)

        for i in range(len(slicing)):
            s = slicing[i]

        if (min_count > paint):
            min_count = paint


print(min_count)
