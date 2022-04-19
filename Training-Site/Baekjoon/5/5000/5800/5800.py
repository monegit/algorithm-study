c = int(input())

for i in range(c):
    s = list(map(int, input().split()))
    s.remove(s[0])
    s.sort(reverse=True)

    result = 0
    for next in range(len(s)-1):
        if result < s[next]-s[next+1]:
            result = s[next]-s[next+1]

    print("Class {}".format(i+1))
    print("Max {}, Min {}, Largest gap {}".format(max(s), min(s), result))
