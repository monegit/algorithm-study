# 백준 알고리즘 10872번 풀이

팩토리얼을 이용해 문제를 풀이하는 문제이다.

학교에서는 밑 수식과 같이 배우지만 밑 식으로 단순 코드를 입력 했을때는 0!을 해결할 수 없다.
$$
n! = 1\times2\times3\times\cdots\times(n-1)\times n
$$
밑 수식을 참고해 0! = 1로 강제하고 코드를 작성했다.
$$
n!=n\times(n-1)!\\
1!=1\times(1-1)!\\
1!=1\times(0)!\\
1!=0!\\
1=0\\
0=1
$$




##### Code

```python
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
```

##### Result

```
0 => 1
1 => 1
2 => 2
3 => 6
4 => 24
5 => 120
6 => 720
7 => 5040
8 => 40320
9 => 362880
10 => 3628800
11 => 39916800
```

