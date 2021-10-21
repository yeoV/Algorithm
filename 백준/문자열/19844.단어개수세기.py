# https://www.acmicpc.net/problem/19844
import sys
import re

read = sys.stdin.readline
vowel = ("a", "e", "i", "o", "u", "h")
start = ("c", "j", "n", "m", "t", "s", "l", "d", "qu")
s = read().rstrip()
s_arr = re.split("[ -]", s)
# s_arr = s.replace("-", " ").split()
ans = len(s_arr)
for e in s_arr:
    if "'" in e:
        tmp = e.split("'")
        if tmp[0] in start and tmp[1][0] in vowel:
            ans += 1
print(ans)
