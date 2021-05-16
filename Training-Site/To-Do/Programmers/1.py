# https://programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings: list, n):
    strings.sort()
    answer = []

    for count in range(len(strings)):
        if len(answer) == 0:
            answer.append(strings[count])

        item = (lambda item, index: item[index])(strings[count], n)

        if ord(item) < ord(answer[count][n]):
            answer.insert(strings.index(strings[count])-1, strings[count])
        # elif ord(item) == ord(answer[count][n]):
        #     for step in range(len(strings[count])):
        #         item = (lambda item, index: item[index])(strings[count], step)
        #         if ord(item) < ord(answer[count][step]):
        #             answer.insert(count,strings[count])
        #             break
        #         else:
        #             answer.insert(count,answer[count])
        #             break
        else:
            answer.insert(strings.index(strings[count]), strings[count])

        # for step in range(len(answer)):
        #     item = (lambda item, index: item[index])(strings[count], n)
        #     print(item)
        #     if ord(list(answer[step])[n]) >= ord(item):
        #         answer.insert(step, strings[count])
            # break

    # print(ord("a")-96)
    answer.pop(len(answer)-1)
    return answer