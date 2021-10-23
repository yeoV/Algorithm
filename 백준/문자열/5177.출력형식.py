# https://www.acmicpc.net/problem/5177

import sys
import re

read = sys.stdin.readline

n = int(read().rstrip())


def clean_str(s) -> str:
    ret = re.sub("[ ]+", " ", s).strip().lower()
    ret = re.sub(r"[{\[]", "(", ret)
    ret = re.sub(r"[}\]]", ")", ret)
    ret = re.sub(";", ",", ret)
    # group() 함수를 이용하여 매칭된 결과값 받아오기 -> 받아온 후 strip
    ret = re.sub(r"(\s+[(),\.:])", lambda x: x.group().strip(), ret)
    ret = re.sub(r"([(),\.:]\s+)", lambda x: x.group().strip(), ret)
    return ret


for k in range(1, n + 1):
    s1 = read().rstrip()
    s2 = read().rstrip()
    s1 = clean_str(s1)
    s2 = clean_str(s2)
    print(f"Data Set {k}: equal" if s1 == s2 else f"Data Set {k}: not equal")
    print()
