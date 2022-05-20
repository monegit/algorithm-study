def solution(s: str):
    num = s
    num = num.replace("zero", "0")
    num = num.replace("one", "1")
    num = num.replace("two", "2")
    num = num.replace("three", "3")
    num = num.replace("four", "4")
    num = num.replace("five", "5")
    num = num.replace("six", "6")
    num = num.replace("seven", "7")
    num = num.replace("eight", "8")
    num = num.replace("nine", "9")

    return int(num)


print(solution("one4seveneight"))
