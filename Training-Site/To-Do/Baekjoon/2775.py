# 차트 만들기
apart = []

for i in range(15):
    apart.append([])

for i in range(14):
    apart[0].append(i+1)

for i in range(1, 15):
    apart[i].append(1)
    apart[i].append(i+2)

for y in range(1, 15):
    for x in range(2, 14):
        apart[y].append(
            apart[y-1 < 0 if 0 else y-1][x-1 < 0 if 0 else x] +
            apart[y][x-1 < 0 if 0 else x-1]
        )

# print(apart)
t = int(input())

for i in range(t):
    # 층
    k = int(input())
    # 호
    n = int(input())

    print(apart[k][n-1])
