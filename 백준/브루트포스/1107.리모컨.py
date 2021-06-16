"""
https://www.acmicpc.net/problem/1107
"""
import sys
read = sys.stdin.readline
N = int(read().strip())
k = int(read().rstrip())
broken = set(map(int, read().split()))
# 최대 누를 수 있는 채널 999999
MAX = 10**6
ret = abs(100 - N)

for val in range(MAX):
    for v in str(val):
        if int(v) in broken:
            break
    else:
        ret = min(ret, abs(val - N) + len(str(val)))
print(ret)
