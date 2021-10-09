# https://www.acmicpc.net/problem/15881
import sys
import re

read = sys.stdin.readline
n = int(read().rstrip())
_str = read().rstrip()
print(len(re.findall("pPAp", _str)))
