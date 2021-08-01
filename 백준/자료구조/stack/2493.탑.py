# https://www.acmicpc.net/problem/2493
import sys
read = sys.stdin.readline
n = int(read().rstrip())
buildings = list(map(int, read().split()))
buildings.reverse()
s, ans = [], [0] * (n+1)
for idx, val in enumerate(buildings):
    while s and val >= s[-1][1]:
        i, _ = s.pop()
        ans[n - i] = n - idx
    s.append((idx, val))
print(*ans[1:], sep=' ')
