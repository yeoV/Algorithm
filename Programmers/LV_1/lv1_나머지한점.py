from collections import Counter


def solution(v):
    answer = []
    for val in zip(*v):
        tmp = Counter(val)
        for i in tmp:
            if tmp[i] == 1:
                answer.append(i)
    return answer


solution([[1, 4], [3, 4], [3, 10]]	)
