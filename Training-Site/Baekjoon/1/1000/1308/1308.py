from datetime import date

ix = list(map(int, input().split()))
iy = list(map(int, input().split()))

x = date(ix[0], ix[1], ix[2])
y = date(iy[0], iy[1], iy[2])

if ((x-y).days >= -365242):
    print("D"+str((x-y).days))
else:
    print("gg")
