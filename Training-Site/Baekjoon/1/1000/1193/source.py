input = int(input())

count = 0
while input>0:
    count += 1
    input -= count

if count%2==0:
    print("{0}/{1}".format(count+input,1+(-input)))
else:
    print("{0}/{1}".format(1+(-input),count+input))