# https://www.acmicpc.net/problem/2473
import sys

read = sys.stdin.readline
n = int(read().rstrip())
arr = list(map(int, read().split()))
arr.sort()
ans = (float('inf'), 0, 0, 0)
for fir in range(n):
    for sec in range(fir + 1, n):
        s, e = sec + 1, n-1
        while s <= e:
            mid = (s+e) // 2
            tmp = arr[fir] + arr[sec] + arr[mid]
            if ans[0] > abs(tmp):
                ans = (abs(tmp), arr[fir], arr[sec], arr[mid])
            if tmp > 0:
                e = mid - 1
            else:
                s = mid + 1
print(ans[1],ans[2],ans[3])