N = int(input())
arr = []

for i in range(1, N + 1):
    num = str(i)
    dash = ''

    for n in range(len(num)):

        if num[n] == '3' or num[n] == '6' or num[n] == '9':
            dash += '-'

    if dash == '':
        arr.append(num)
    else:
        arr.append(dash)
        dash = ''

print(' '.join(arr))