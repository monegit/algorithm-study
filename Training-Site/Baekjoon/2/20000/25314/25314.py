# 정수형으로 입력을 받습니다.
N = int(input())

# 밑 for문에서 'long '을 반복적으로 주입해주기 때문에 비워줍니다.
# 만약 입력이 2면 int만 출력해야하기 때문
l = ""

# int(~)를 사용하면 나누기를 했을때 소숫점은 버리기 때문에 3이하의 숫자는 0입니다.
for i in range(int(N / 4)):
    l += "long "

# {0}int를 한 이유는 3이하의 숫자를 입력받으면 ""(l 변수)+"int"(print 출력)기 때문에 띄움없는 int만 출력되기 때문
print("{0}int".format(l))
