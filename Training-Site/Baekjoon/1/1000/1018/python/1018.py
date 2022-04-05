c = int(input())

p = [[] for _ in range(201)]

for i in range(c):
    age, name = map(str, input().split())
    p[int(age)].append(name)

for i in range(len(p)):
    if len(p[i]) == 0:
        continue
    else:
        for ii in range(len(p[i])):
            print(i, p[i][ii])
