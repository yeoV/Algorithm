# https://www.acmicpc.net/problem/13913
import sys
from collections import deque

read = sys.stdin.readline
n, k = map(int, read().split())

MAX = 10 ** 5
dp = [-1] * (MAX + 1)
directions = (-1, 1, 0)
path = []


def run(start):
    q = deque([start])
    dp[start] = start
    while q:
        dist = q.popleft()

        if dist == k:
            now = k
            # 경로 추적하는 부분
            while now != n:
                path.append(now)
                now = dp[now]
            path.append(now)
            return
        for direction in directions:
            nxt_dist = dist * 2 if not direction else dist + direction
            if 0 <= nxt_dist <= MAX:
                if dp[nxt_dist] == -1:
                    dp[nxt_dist] = dist
                    q.append(nxt_dist)


run(n)
print(len(path) - 1)
print(*path[::-1], sep=" ")
# def find(start):
#     q = deque([(0, start, str(start))])
#     dp[start] = 0
#     while q:
#         time, dist, prev = q.popleft()
#         nxt_time = time + 1
#
#         if dist == k:
#             print(dp[dist])
#             print(prev)
#             return
#
#         for direction in directions:
#             nxt_dist = dist * 2 if not direction else dist + direction
#             if 0 <= nxt_dist <= MAX:
#                 if dp[nxt_dist] == -1 or dp[nxt_dist] >= nxt_time:
#                     dp[nxt_dist] = nxt_time
#                     q.append((nxt_time, nxt_dist, prev + " " + str(nxt_dist)))


# find(n)
