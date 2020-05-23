_input = int(input())

for i in range(1,_input+1):
    for ii in range(i):
        print('*',end='')
    print()
for i in range(_input-1,0,-1):
    for ii in range(i):
        print('*',end='')
    print()