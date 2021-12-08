h, m, s = map(int, input().split())
input = int(input())

s = s + input
m = m + int(s/60)
h = h + int(m/60)
s = s % 60
m = m % 60
h = h % 24

print(h,m,s)
