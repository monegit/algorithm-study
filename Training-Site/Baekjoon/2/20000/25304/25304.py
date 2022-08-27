x = int(input())
n = int(input())
total = 0

for i in range(n):
    ab = list(map(int, input().split()))
    total += ab[0] * ab[1]

if x == total:
    print("Yes")
else:
    print("No")
