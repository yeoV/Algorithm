# https://school.programmers.co.kr/learn/courses/30/lessons/160586
def solution(keymap, targets):
    answer = []
    INF = 1e9
    alpa = [INF] * 26

    for key in keymap:
        for i, v in enumerate(key):
            alpa[ord(v) - ord("A")] = min(alpa[ord(v) - ord("A")], i + 1)

    for target in targets:
        index = map(lambda x: ord(x) - ord("A"), target)
        ans = sum(map(lambda x: alpa[x], index))
        if ans < INF:
            answer.append(ans)
        else:
            answer.append(-1)

    return answer
