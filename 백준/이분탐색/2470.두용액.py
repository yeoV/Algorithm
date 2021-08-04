# https://www.acmicpc.net/problem/2470
import sys
read = sys.stdin.readline
n = int(read().rstrip())
arr = list(map(int, read().split()))
arr.sort()
ans = (float('inf'), 0, 0)
for i in range(len(arr)):
    s, e = i+1, len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        tmp = arr[mid] + arr[i]
        if ans[0] > abs(tmp):
            ans = (abs(tmp), arr[i], arr[mid])
        if tmp > 0:
            e = mid - 1
        else:
            s = mid + 1
print(ans[1], ans[2])

