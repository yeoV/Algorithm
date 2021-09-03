# https://www.acmicpc.net/problem/1182
from itertools import combinations
import sys

# 1. 조합을 이용한 풀이
read = sys.stdin.readline
n, s = map(int, read().split())
arr = list(map(int, read().split()))
ans = 0
for i in range(1, n + 1):
    for comb in combinations(arr, i):
        tmp = sum([c for c in comb])
        if tmp == s:
            ans += 1

print(ans)


# 2. 재귀를 이용한 풀이

import sys
read = sys.stdin.readline
n, s = map(int, read().split())
arr = list(map(int, read().split()))
ans = 0
def run(depth, idx, total):
    global ans
    if depth == n:
        if total == s:
            ans += 1
        return
    
    # 포함
    run(depth + 1, idx + 1, total + arr[idx])
    # 미 포함
    run(depth + 1, idx + 1, total)

run(0, 0, 0)
# 공집합 제외하기
print(ans if s != 0 else ans-1)