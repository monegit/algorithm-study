_input = int(input())

zero = [1,0,1]
one = [0,1,1]

def fibonacci(n):
    init_len = len(zero)
    if(init_len<=n):
        for i in range(init_len, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("{} {}".format(zero[n],one[n]))

for _ in range(_input):
    fibonacci(int(input()))