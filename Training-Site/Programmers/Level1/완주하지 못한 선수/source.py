# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant: list, completion: list):

    # 순서대로 정렬해준다
    participant.sort()
    completion.sort()

    # zip함수를 이용해 묶어준다
    for p, c in zip(participant, completion):
        # 테스트
        # print(parti,comple)

        # 서로 맞는지 보고 틀리면 p를 반환해줌
        if p != c:
            return p

    return participant[-1]


print(
    solution(['leo', 'kiki', 'eden'], ['eden', 'kiki']))
print(
    solution(['marina', 'josipa', 'nikola', 'vinko', 'filipa'], [
        'josipa', 'filipa', 'marina', 'nikola']))
print(
    solution(
        ['mislav', 'stanko', 'mislav', 'ana'], ['stanko', 'ana', 'mislav']))
