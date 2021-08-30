# https://programmers.co.kr/learn/courses/30/lessons/72411
from collections import Counter, defaultdict
from itertools import combinations

def solution(orders, course):
    total = defaultdict(lambda : defaultdict(int))
    for order in orders:
        for count in course:
            for comb in combinations(order, count):
                total[count][comb] += 1
    # print(total)
    answer = []
    print(total)
    for key in total.keys():
        tmp_cnt, tmp_list = 0, []
        for menu, cnt in total[key].items():
            if cnt > 1 and cnt > tmp_cnt:
                tmp_list = ["".join(list(menu))]
                tmp_cnt = cnt
            elif cnt == tmp_cnt:
                tmp_list.append("".join(list(menu)))
        answer.extend(tmp_list)
        # print(answer)
    answer.sort()
    return answer




# solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
solution(["XYZ", "XWY", "WXA"], [2,3,4])