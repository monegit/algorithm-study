n = int(input())

for _ in range(n):
    test = input()
    print(str.format("{0}{1}", test[0], test[-1]))
