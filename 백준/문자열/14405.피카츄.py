# https://www.acmicpc.net/problem/14405
import sys
import re

read = sys.stdin.readline
data = read().rstrip()
data = re.sub("pi|ka|chu", "", data)
print("YES" if not data else "NO")
