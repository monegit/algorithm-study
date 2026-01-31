import sys

S1 = sys.stdin.readline().strip()
S2 = sys.stdin.readline().strip()

stack = []
len_S2 = len(S2)

for c in S1:
    stack.append(c)

    if len(stack) >= len_S2:
        if ''.join(stack[-len_S2:]) == S2:
            for _ in range(len_S2):
                stack.pop()

result = ''.join(stack)

if result:
    sys.stdout.write(result)
else:
    sys.stdout.write('FRULA')
