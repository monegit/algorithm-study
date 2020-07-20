_input = input()
arr = [-1] * (ord('z') - 96) # 알파벳 개수만큼 -1로 초기화

for i in range(len(_input)):
    # 1. _input 알파벳의 숫자를 찾고 arr의 배열로 설정한다.
    # 2. _input의 알파벳 위치를 찾는다.
    # 3. arr의 배열에 _input의 알파벳 위치를 대입한다.
    arr[ord(_input[i]) - 97] = _input.index(_input[i])

for i in range(26):
    print(arr[i], end = " ")