# https://www.acmicpc.net/problem/14719
import sys

read = sys.stdin.readline
h, w = map(int, read().split())
blocks = list(map(int, read().split()))
s = []
ans = 0
piv = blocks[0]
for block in blocks[1:]:
    if piv <= block:
        while s:
            tmp = s.pop()
            ans += piv - tmp
        piv = block
    s.append(block)
# 맨 마지막 벽을 만났을 경우
piv = -1
while s:
    tmp = s.pop()
    if piv < tmp:
        piv = tmp
    else:
        ans += piv - tmp
print(ans)
