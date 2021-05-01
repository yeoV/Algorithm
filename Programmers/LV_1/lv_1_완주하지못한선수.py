from collections import Counter
import time


def solution1(participant, completion):
    s = time.time()
    part = Counter(participant)
    comp = Counter(completion)
    ans = part - comp
    # print(list(ans.keys())[0])
    print(f'{time.time() - s:.30f}')
    return list(ans.keys())[0]


def solution2(participant, completion):
    s = time.time()
    d = {}
    for x in participant:
        d[x] = d.get(x, 0) + 1
    for x in completion:
        d[x] -= 1
    dnf = [k for k, v in d.items() if v > 0]
    print(f'{time.time() - s:.30f}')
    return dnf[0]


solution1(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
solution2(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])
