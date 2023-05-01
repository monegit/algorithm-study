# N: 바구니의 갯수
# M: 공을 넣을 횟수
N, M = map(int, input().split())

# 공이 담긴 상자
box = [0 for _ in range(N)]


# i번 바구니 부터 j번 바구니까지에 k번 번호가 적힌 공
def ball_input(i: int, j: int, k: int):
    # 조건 검사
    if 1 <= i <= j <= N and 1 <= k <= N:
        # i~j 박스에 k번 공을 box에 넣는다
        for index in range(i - 1, j):
            box[index] = k
    else:
        return


# M번 만큼 공의 정보를 반복해서 넣는다
for i in range(M):
    i, j, k = map(int, input().split())
    ball_input(i, j, k)

# 배열을 문자열로 바꿔준다
print(' '.join(str(s) for s in box))