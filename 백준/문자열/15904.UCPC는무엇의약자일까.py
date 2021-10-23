# https://www.acmicpc.net/problem/15904
import sys
import re

read = sys.stdin.readline

_str = read().rstrip()
clean_str = re.sub("[^UCPC]", "", _str)
for i in "UCPC":
    if i in clean_str:
        nxt_idx = clean_str.index(i)
        clean_str = clean_str[nxt_idx + 1 :]
        print(clean_str)
    else:
        print("I hate UCPC")
        break
else:
    print("I love UCPC")
