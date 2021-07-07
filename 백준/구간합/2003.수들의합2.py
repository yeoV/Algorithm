# https://www.acmicpc.net/problem/2003
import sys
read = sys.stdin.readline
n, m = map(int, read().split())
A = list(map(int, read().split()))


total = 0
end = 0
res = 0
for start in range(n):
    while total < m and end < n:
        total += A[end]
        end += 1

    if total == m:
        res += 1
    total -= A[start]
print(res)
