# https://www.acmicpc.net/problem/2467
import sys
read = sys.stdin.readline
n = int(read().rstrip())
arr = list(map(int, read().split()))

ans = (float('inf'), 0, 0)
for i in range(n):
    s, e = i+1, len(arr)-1
    while s <= e:
        mid = (s + e) // 2
        tmp = abs(arr[mid] + arr[i])
        if tmp < ans[0]:
            ans = (tmp, arr[i], arr[mid])
        if (arr[mid] + arr[i]) > 0:
            e = mid - 1
        else:
            s = mid + 1

print(ans[1], ans[2])