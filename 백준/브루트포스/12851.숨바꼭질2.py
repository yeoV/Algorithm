# https://www.acmicpc.net/problem/12851
import sys
from collections import deque

read = sys.stdin.readline

n, k = map(int, read().split())
MAX = 10 ** 5
dp = [-1] * (MAX + 1)


def go(start):
    ans = 1
    q = deque([(0, start)])
    dp[start] = 0
    while q:
        time, dist = q.popleft()
        if dist == k and dp[dist] >= time:
            print(time, ans, sep='\n')
            return
        nxt_time = time + 1
        for nxt_dist in [dist + 1, dist - 1, dist * 2]:
            # 방문한적 없거나 다시 방문하는 경우
            if 0 <= nxt_dist <= MAX:
                if dp[nxt_dist] == -1 or dp[nxt_dist] >= nxt_time:
                    if nxt_dist == k:
                        if dp[nxt_dist] == nxt_time:
                            ans += 1
                    dp[nxt_dist] = nxt_time
                    q.append((nxt_time, nxt_dist))


go(n)
