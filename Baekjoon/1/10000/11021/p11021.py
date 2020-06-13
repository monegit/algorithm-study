# problem NO.11021

count = int(input())
_list = []
for i in range(count):
    _input = input()
    _input.split()
    _list.append(int(_input[0]) + int(_input[2]))

for i in range(count):
    print("Case #{0}: {1}".format(i + 1, _list[i]))