import sys

n = sys.stdin.readline().split()[0]

count = 0

while(len(n) != 1):
    t = 0
    count += 1
    for i in range(len(n)):
        t += int(n[i])
    n = str(t)

print(count)
if(int(n) % 3 == 0 and int(n) < 10):
    print("YES")
else:
    print("NO")
