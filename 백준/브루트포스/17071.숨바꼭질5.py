# https://www.acmicpc.net/problem/17071
import sys
from collections import deque

read = sys.stdin.readline
n, k = map(int, read().split())
MAX = 500000
# 홀수 짝수
dp = [[-1] * (MAX + 1) for _ in range(2)]
if n == k:
    print(0)
    exit()


def bfs(start, k):
    q = deque([])
    q.append((start, 0, k))
    dp[0][n] = 0
    while q:
        # print(q)
        d, t, nk = q.popleft()
        # 이미 체크된 경우, 저장된 값이 t보다 작거나 같은 경우
        # if dp[t % 2][nk] != -1 and (dp[t % 2][nk] or dp[t % 2][nk] == 0):
        if dp[t % 2][nk] != -1 and dp[t % 2][nk] <= t:
            print(t)
            exit()
        dist = [d + 1, d - 1, d * 2]
        for nxt_dist in dist:
            nxt_t = t + 1
            nxt_k = nk + nxt_t
            if (
                0 <= nxt_dist <= MAX
                and dp[nxt_t % 2][nxt_dist] == -1
                and nxt_k <= MAX
            ):
                dp[nxt_t % 2][nxt_dist] = nxt_t
                q.append((nxt_dist, nxt_t, nxt_k))
    return -1


print(bfs(n, k))
