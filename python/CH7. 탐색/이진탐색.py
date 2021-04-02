# 10 7
# 1 3 5 7 9 11 13 15 17 19
# 4
import sys


def binary_search(arr, target, start, end):
    mid = (start + end) // 2
    if arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, end)
    else:
        return mid


N, target = map(int, input().split(" "))
arr = list(map(int, sys.stdin.readline().split(" ")))
# print(arr)
print(binary_search(arr, target, 0, N-1) + 1)
