# https://www.acmicpc.net/problem/10819
from itertools import permutations
import sys

read = sys.stdin.readline

ans = 0
n = int(read().rstrip())
arr = list(map(int, read().split()))
visit = [False] * n


def run(depth, perm):
    global ans
    if depth == n:
        ret = sum([abs(perm[i] - perm[i+1]) for i in range(n-1)])
        ans = max(ans, ret)
        return

    for i in range(n):
        if not visit[i]:
            visit[i] = True
            perm.append(arr[i])
            run(depth + 1, perm)
            visit[i] = False
            perm.pop()


run(0, [])
print(ans)
