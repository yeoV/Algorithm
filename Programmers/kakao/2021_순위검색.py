# https://programmers.co.kr/learn/courses/30/lessons/72412
from collections import defaultdict
from itertools import combinations
from bisect import bisect_left
import re

info_table = defaultdict(list)


# 가능한 조합식 만들기
def make_table(data):
    # key 값 : 각각의 조합식, val 값 : 비용 값
    for idx in range(5):
        for comb in combinations(enumerate(data[:4]), idx):
            tmp = ['-'] * 4
            for e in comb:
                tmp[e[0]] = e[1]
            info_table["".join(tmp)].append(int(data[4]))


def solution(info, query):
    answer = []
    for val in info:
        val = val.split()
        make_table(val)

    for k in info_table.keys():
        info_table[k].sort()
    for q in query:
        q = re.sub('and', '', q).split()
        q, score = "".join(q[:4]), int(q[4])
        q = info_table[q]
        if q:
            piv_idx = bisect_left(q, score)
            answer.append(len(q) - piv_idx)
        else:
            answer.append(0)

    print(answer)
    return answer

solution(["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
          "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
         ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
          "- and - and - and - 150"])
