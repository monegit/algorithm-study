_input = int(input())

count = 0

def cut(content: list):
    arr = content
    for i in range(len(content)):
        if arr[0] == 0:
            del arr[0]
        elif arr[0] == 1:
            break
    
    for i in range(len(content)):
        if arr[-1] == 0:
            del arr[-1]
        elif arr[-1] == 1:
            break
    return arr

def check(content: list):
    set_content = list(set(content))
    arr = []

    result = 0
    for i in range(len(set_content)):
        for ii in content:
            if ii == set_content[i]:
                arr.append(1)
            else:
                arr.append(0)
        
        if sum(arr) == len(cut(arr)):
            result+=1

        arr = []

    if result == len(set_content):
        return 1
    else:
        return 0

for f in range(_input):
    content = list(input())
    count += check(content)
print(count)