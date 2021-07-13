# https://www.acmicpc.net/problem/2805
import sys
read = sys.stdin.readline
n, m = map(int, read().split())
arr = list(map(int, read().split()))
e = max(arr)
s = 1
while s <= e:
    mid = (e + s) // 2
    res = 0
    for tree in arr:
        res += tree - mid if tree - mid > 0 else 0
    if res >= m:
        s = mid + 1
    else:
        e = mid - 1
print(e)
