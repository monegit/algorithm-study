import sys
input = sys.stdin.readline

# 맹수 좌표
Bx, By = map(int, input().split())
# 구름 좌표
Gx, Gy = map(int, input().split())

# 거리 조건 먼저 확인 (제곱 거리 사용)
dx = Bx - Gx
dy = By - Gy
if dx * dx + dy * dy < 25:
    print("NO")
    sys.exit(0)

# 덫 개수
N = int(input())

# 직사각형 범위
xmin, xmax = min(Bx, Gx), max(Bx, Gx)
ymin, ymax = min(By, Gy), max(By, Gy)

count = 0

for _ in range(N):
    x, y = map(int, input().split())
    if xmin <= x <= xmax and ymin <= y <= ymax:
        count += 1
        if count >= 3:
            print("YES")
            sys.exit(0)

print("NO")