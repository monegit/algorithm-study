a, b = map(str, input().split())

result = len(b)

for i in range(len(b)-len(a)+1):
    n = 0

    for ii in range(len(a)):
        x = list(a)
        if x[ii] != b[i:len(a)+i][ii]:
            n += 1

    if result > n:
        result = n

print(result)
