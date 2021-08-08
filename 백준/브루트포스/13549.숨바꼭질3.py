# https://www.acmicpc.net/problem/13549
import sys
from collections import deque

read = sys.stdin.readline
n, k = map(int, read().split())
MAX = 10 ** 5
dp = [-1] * (MAX + 1)
directions = (0, -1, 1)


def go(start):
    q = deque([(0, start)])
    dp[start] = 0
    while q:
        time, dist = q.popleft()
        if dist == k:
            return dp[dist]
        for direction in directions:
            nxt_dist = dist + direction if direction else dist * 2
            if 0 <= nxt_dist <= MAX:
                nxt_time = time if not direction else time + 1
                if dp[nxt_dist] == -1 or dp[nxt_dist] >= nxt_time:
                    dp[nxt_dist] = nxt_time
                    q.append((nxt_time, nxt_dist))


print(go(n))

