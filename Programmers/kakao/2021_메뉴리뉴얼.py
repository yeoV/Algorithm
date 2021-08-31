# https://programmers.co.kr/learn/courses/30/lessons/72411
from collections import defaultdict, Counter
from itertools import combinations


def solution(orders, course):
    ans = []
    for count in course:
        order_comb = defaultdict(int)
        tmp = []
        for order in orders:
            tmp += combinations(sorted(order), count)
        most_order = Counter(tmp).most_common()
        # 최대 갯수 추출하는 방법
        ans += [k for k, v in most_order if v > 1 and v == most_order[0][1]]

    return sorted(["".join(val) for val in ans])


# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
