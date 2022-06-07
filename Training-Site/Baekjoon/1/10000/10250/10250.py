import math

count = int(input())

for i in range(count):
    h, w, n = map(int, input().split())
    floor = n % h
    unit = math.ceil(n/h)

    print("{0}{1:>02d}".format(h if floor == 0 else floor, unit))
