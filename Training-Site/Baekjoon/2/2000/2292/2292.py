_input = int(input())
sqrt = 1
count = 1

while (True):
    if sqrt>=_input:
        break
    sqrt+=6*count
    count+=1

print(count)
