import sys

arr = []


def writeline(s: str):
    sys.stdout.write(s)
    sys.stdout.write('\n')


def push_back(i):
    arr.append(i)


def push_front(i):
    arr.insert(0, i)


def pop_front():
    if (len(arr) < 1):
        writeline('-1')
    else:
        writeline(arr[0])
        arr.pop(0)


def pop_back():
    if (len(arr) < 1):
        writeline('-1')
    else:
        writeline(arr[-1])
        arr.pop(-1)


def size():
    writeline(str(len(arr)))


def front():
    if (len(arr) < 1):
        writeline('-1')
    else:
        writeline(arr[0])


def back():
    if (len(arr) < 1):
        writeline('-1')
    else:
        writeline(arr[-1])


def empty():
    if (len(arr) < 1):
        writeline('1')
    else:
        writeline('0')


def solution():
    for _ in range(int(input())):
        command = list(map(str, sys.stdin.readline().split()))

        if (command[0] == 'push_back'):
            push_back(command[1])
        elif (command[0] == 'push_front'):
            push_front(command[1])
        elif (command[0] == 'front'):
            front()
        elif (command[0] == 'back'):
            back()
        elif (command[0] == 'pop_front'):
            pop_front()
        elif (command[0] == 'pop_back'):
            pop_back()
        elif (command[0] == 'size'):
            size()
        elif (command[0] == 'empty'):
            empty()


solution()
