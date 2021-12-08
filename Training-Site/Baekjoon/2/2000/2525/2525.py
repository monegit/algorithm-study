h, m = map(int, input().split())
im = int(input())

m = m + im
h = h + int(m/60)
m = m % 60
h = h % 24

print(h,m)
