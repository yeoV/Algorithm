# https://www.acmicpc.net/problem/17413
import sys
import re

read = sys.stdin.readline

s = read().rstrip()
# () <- keep the separators
s_arr = re.split("(\W)", s)
idx = 0
while idx < len(s_arr):
    if s_arr[idx] == "<":
        while s_arr[idx] != ">":
            idx += 1
    else:
        s_arr[idx] = s_arr[idx][::-1]
        idx += 1
print("".join(s_arr))
