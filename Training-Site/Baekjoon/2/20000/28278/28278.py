import sys

N = int(input())

stack = []

for _ in range(N):
    command = list(map(int, sys.stdin.readline().split()))

    if command[0] == 2:
        if stack:
            sys.stdout.write(str(stack[-1])+'\n')
            stack.pop()
        else:
            sys.stdout.write(str(-1)+'\n')
    elif command[0] == 3:
        sys.stdout.write(str(len(stack))+'\n')
    elif command[0] == 4:
        if stack:
            sys.stdout.write(str(0)+'\n')
        else:
            sys.stdout.write(str(1)+'\n')
    elif command[0] == 5:
        if stack:
            sys.stdout.write(str(stack[-1])+'\n')
        else:
            sys.stdout.write(str(-1)+'\n')
    if command[0] == 1:
        stack.append(command[1])
