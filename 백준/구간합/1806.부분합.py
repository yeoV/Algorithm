# https://www.acmicpc.net/problem/1806
import sys
read = sys.stdin.readline
n, s = map(int, read().split())
start, end = 0, 0
arr = list(map(int, read().split()))
prefix = [0 for _ in range(n+1)]
# 구간합 만들기
for i in range(n):
    prefix[i+1] = prefix[i] + arr[i]

res = float('inf')
while end < n+1:
    # 5 - 3은 5와 4의 합을 의미함
    tmp = prefix[end] - prefix[start]
    if tmp < s:
        end += 1
    else:
        res = min(res, end-start)
        start += 1
print(res if not res == float('inf') else 0)
