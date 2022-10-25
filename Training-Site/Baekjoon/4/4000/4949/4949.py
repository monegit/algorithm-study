import sys


def writeline(message: str):
    sys.stdout.write(message+'\n')


def check(s: str):
    letter = s
    arr = []

    for word in letter:
        if (word == '(' or word == '['):
            arr.append(word)
        elif (word == ')'):
            if (word == ')' and arr != [] and arr[-1] == '('):
                arr.pop()
            else:
                arr.append(')')
        elif (word == ']'):
            if (word == ']' and arr != [] and arr[-1] == '['):
                arr.pop()
            else:
                arr.append(']')

    if (len(arr) == 0):
        writeline('yes')
    else:
        writeline('no')


while (True):
    letter = sys.stdin.readline().split('.')
    if (letter[0] == ''):
        break
    else:
        check(letter[0])
