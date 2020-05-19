input_factorial = int(input())

def factorial(num):
    result = 1
    if num == 0:
        return 1
    else:
        for i in range(1, num):
            result *= i
        return result * num

print(factorial(input_factorial))

# input_factorial = int(input())

# def factorial(num):
#     result = 1
#     if num == 0:
#         return 1
#     else:
#         for i in range(1, num):
#             result *= i
#         return result * num

# print(factorial(input_factorial))

# input_factorial = int(input())

# def factorial(num):
#     result = 1
#     for i in range(1, num):
#         result *= i
#     return result * num

# for i in range(12):
#     print(factorial(i))