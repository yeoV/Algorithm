# https://programmers.co.kr/learn/courses/30/lessons/42890
from itertools import combinations


def solution(relation):
    col_cnt = len(relation[0])
    candidate_key = []
    for idx in range(1, col_cnt + 1):
        for comb in combinations(range(col_cnt), idx):
            hist = []
            for rec in relation:
                tmp_query = [rec[i] for i in comb]
                if tmp_query in hist:
                    break
                else:
                    hist.append(tmp_query)
            else:
                for key in candidate_key:
                    if set(key).issubset(set(comb)):
                        break
                else:
                    candidate_key.append(comb)
    return len(candidate_key)


solution(
    [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"],
    ]
)
