_input = input().lower() # 알파벳을 lower을 이용해 모두 소문자로 바꾼다.
count = [0] * (ord('z') - 96) # 알파벳 만큼 배열을 만들고 카운트를 센다.
_maxCount = 0 # 최댓값을 셈

# _input의 알파벳을 count리스트에 1씩 증가
for i in range(len(_input)):
    count[ord(_input[i]) - 97] += 1

# count의 최댓값을 찾음
_max = max(count)

# 최대값이 2개 이상인가 체크
for i in range(len(count)):
    if _max == count[i]:
        _maxCount+=1

# 만약 최대값이 2개 이상이라면 "?"를 출력하고, 만약 아니라면 최대값의 알파벳을 출력
if _maxCount >= 2:
    print("?")
else:
    print(chr(count.index(_max)+97).upper())