# https://www.acmicpc.net/problem/2437
import sys

read = sys.stdin.readline
n = int(read().rstrip())
arr = list(map(int, read().split()))

arr.sort()
# print(arr)
target = 1
for i in arr:
    if target < i:
        break
    target += i
print(target)
