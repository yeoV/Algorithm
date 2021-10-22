# https://www.acmicpc.net/problem/1543
import sys
import re

read = sys.stdin.readline

s = read().rstrip()
target = read().rstrip()

print(len(re.findall(target, s)))
