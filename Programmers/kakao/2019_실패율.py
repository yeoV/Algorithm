# https://programmers.co.kr/learn/courses/30/lessons/42889
from collections import Counter, defaultdict


def solution(N, stages):
    answer = []
    failure = defaultdict(float)
    stage_cnt = Counter(stages)
    print(stage_cnt)
    for idx in range(1, N + 1):
        tmp = sum([v for k, v in stage_cnt.items() if k >= idx])
        try:
            failure[idx] = stage_cnt[idx] / tmp
        except ZeroDivisionError:
            failure[idx] = 0
    print(failure)
    for k, v in sorted(failure.items(), key=lambda x: x[1], reverse=True):
        answer.append(k)
    print(answer)
    return answer


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
