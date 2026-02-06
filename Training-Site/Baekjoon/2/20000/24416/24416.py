count_recursion = 1
count_dp = 0


def fibonacci_recursion(n):
    global count_recursion

    if n == 1 or n == 2:
        return 1
    else:
        count_recursion += 1
        return (fibonacci_recursion(n-1)+fibonacci_recursion(n-2))


fibonacci_arr = [1, 1]


def fibonacci_dp(n):
    global fibonacci_arr, count_dp

    for i in range(2, n):
        count_dp += 1
        fibonacci_arr.append(fibonacci_arr[i-1]+fibonacci_arr[i-2])
    return


N = int(input())

fibonacci_recursion(N)
fibonacci_dp(N)

print(count_recursion, count_dp)
