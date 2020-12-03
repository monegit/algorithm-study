# todo
input=sys.stdin.readline

count = int(input())
_list = list()


def empty(list):
    if(len(list) <= 0):
        return 1
    else:
        return 0


def top(list):
    if(empty(list)):
        return -1
    else:
        return list[len(list) - 1]


def push(list, num):
    return list.append(num)


def size(list):
    return len(list)


def pop(list):
    _return = 0
    if (empty(_list)):
        _return = -1
    else:
        trunk = top(_list)
        _list.pop(len(_list)-1)
        _return = trunk
    return _return

def switch(case, list):
    if(case[0] == "empty"):
        print(empty(list))
    elif(case[0] == "top"):
        print(top(list))
    elif(case[0] == "push"):
        list.append(case[1])
    elif(case[0] == "size"):
        print(len(list))
    elif(case[0] == "pop"):
        if(empty(list)):
            print(-1)
        else:
            print(list[len(list)-1])
            list.pop(len(list)-1)


for i in range(0, count):
    switch(input().split(), _list)
