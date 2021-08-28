# https://programmers.co.kr/learn/courses/30/lessons/42888
from collections import defaultdict


def solution(record):
    user_info = defaultdict(str)
    res = []
    for rec in record:
        rec = rec.split()
        if rec[0] == "Enter":
            user_info[rec[1]] = rec[2]
            res.append([rec[1], "님이 들어왔습니다."])
        elif rec[0] == "Leave":
            res.append([rec[1], "님이 나갔습니다."])
        elif rec[0] == "Change":
            user_info[rec[1]] = rec[2]
    print(user_info)

    for idx in range(len(res)):
        res[idx][0] = user_info[res[idx][0]]
        res[idx] = "".join(res[idx])
    print(res)
    return res


solution(
    [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan",
    ]
)
