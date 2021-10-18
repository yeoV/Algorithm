# https://www.acmicpc.net/problem/2870
import sys
import re

read = sys.stdin.readline

n = int(read().rstrip())


ans = []
for _ in range(n):
    _str = read().rstrip()
    target = map(int, re.findall("[0-9]+", _str))
    ans.extend(target)

ans.sort()
print(*ans, sep="\n")
