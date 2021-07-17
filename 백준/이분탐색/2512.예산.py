# https://www.acmicpc.net/problem/2512
import sys

read = sys.stdin.readline
n = int(read().rstrip())
arr = list(map(int, read().split()))
t = int(read().rstrip())

if t >= sum(arr):
    print(max(arr))
    exit()

def binsearch(arr, t):
    s, e = 0, t
    while s <= e:
        mid = (s + e) // 2
        tmp = 0
        for val in arr:
            tmp += min(val, mid)
        # 값이 더 큰 경우에만\
        if tmp > t:
            e = mid - 1
        else:
            s = mid + 1
    return e


print(binsearch(arr, t))
