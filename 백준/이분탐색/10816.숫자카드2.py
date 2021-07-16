# https://www.acmicpc.net/problem/10816
import sys

read = sys.stdin.readline
n = int(read().rstrip())
arr = list(map(int, read().split()))
m = int(read().rstrip())
arr.sort()


# lower, upper bounnd 만들기
def lower(arr, t):
    s, e = 0, len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] >= t:
            e = mid - 1
        else:
            s = mid + 1
    return e


def upper(arr, t):
    s, e = 0, len(arr) - 1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] > t:
            e = mid - 1
        else:
            s = mid + 1
    return e


ans = []
for val in list(map(int, read().split())):
    l, u = lower(arr, val), upper(arr, val)
    ans.append(u - l)
print(*ans, sep=' ')
