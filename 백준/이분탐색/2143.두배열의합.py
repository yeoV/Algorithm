# https://www.acmicpc.net/problem/2143
import sys
# from bisect import bisect_left, bisect_right
read = sys.stdin.readline
T = int(read().rstrip())
n = int(read().rstrip())
A = list(map(int, read().split()))
m = int(read().rstrip())
B = list(map(int, read().split()))
# A와 B 배열의 연속된 부 배열의 합
AS, BS = [], []
# 시간복잡도 O(n^2)
for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += A[j]
        AS.append(tmp)
# 시간복잡도 O(n^2)
for i in range(m):
    tmp = 0
    for j in range(i, m):
        tmp += B[j]
        BS.append(tmp)
# print(AS, BS)
# 이분 탐색을 위한 Sort 시간복잡도 O(nlogn)
AS.sort()
BS.sort()
cnt = 0
# print(AS, BS)
# 이분 탐색 O(logn) T - AS = BS 인 경우를 찾기


def lower(arr, target):
    s, e = 0, len(arr) - 1

    while s <= e:
        mid = (s+e) // 2
        if arr[mid] >= target:
            e = mid - 1
        else:
            s = mid + 1
    return e


def upper(arr, target):
    s, e = 0, len(arr) - 1
    while s <= e:
        mid = (s+e) // 2
        if arr[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    return e


for val in AS:
    target = T - val
    up, low = upper(BS, target), lower(BS, target)
    if up != low:
        cnt += up - low
print(cnt)
# print(lower(AS, 4))
# print(upper(AS, 4))
