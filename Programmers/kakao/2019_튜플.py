# https://programmers.co.kr/learn/courses/30/lessons/64065
import re
from collections import Counter


# 가장 많이 언급된 순서대로 튜플이다
def solution(s):
    print(re.findall('\d', s))
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))


#
# def solution(s):
#     ans = []
#     s = [list(map(int, val.strip('{|}').split(','))) for val in s.split('},{')]
#     s.sort(key=lambda x: len(x))
#     for subset in s:
#         for val in subset:
#             if val not in ans:
#                 ans.append(val)
#     print(ans)


solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
# solution("{{20,111},{111}}")
# solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")
