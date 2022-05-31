r1, c1, r2, c2 = map(int, input().split())

max = max([abs(r1), abs(c1), abs(r2), abs(c2)])
# print(abs()

t = [[]]
i = 1

t[0].append("1")
i += 1

for x in range(max):
    # up
    t.insert(0, [])
    for y in range(len(t), 0, -1):
        t[y-1].append(str(i))
        i += 1

    # left
    for y in range(len(t)-1):
        t[0].insert(0, str(i))
        i += 1

    # down
    t.append([])
    for y in range(1, len(t)):
        t[y-1].insert(0, str(i))
        i += 1

    # right
    for y in range(len(t)):
        t[len(t)-1].append(str(i))
        i += 1

trunk = []

for i in range(r1+max, r2+max+1):
    line = []
    for y in t[i][c1+max:c2+max+1]:
        line.append(y)
    trunk.append(line)
    # print(t[i][c1+max:c2+max+1])

maxlen = 0

for i in trunk:
    for y in i:
        if maxlen < len(y):
            maxlen = len(y)

for i in trunk:
    for y in i:
        print((" "*(maxlen-len(y)))+y+" ", end='')
    print()
