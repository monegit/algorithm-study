# problem 2753

# 입력을 정수형으로 받아옴
_input = int(input())

# 100으로 나누어지지 않고, 4로 나누어 지면 윤년
if _input % 100 != 0 and _input % 4 == 0:
    print(1)
# 100으로 나누어지지만, 400으로 나누어지지 않으면 평년
elif _input % 100 == 0 and _input % 400 != 0:
    print(0)
# 400으로 나누어 떨어지면 윤년
elif _input % 400 == 0:
    print(1)
else:
    print(0)