count = int(input())

ball = 1

for i in range(count):
    cup = list(map(int, input().split()))

    # 공 위치 초기화
    if ball == -1:
        ball = cup[0]

    if ball == cup[0]:
        ball = cup[1]
    elif ball == cup[1]:
        ball = cup[0]

print(ball)
