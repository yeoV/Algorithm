# https://www.acmicpc.net/problem/17503
import sys
from heapq import heappop, heappush

read = sys.stdin.readline

N, M, K = map(int, read().split())

q = []
for _ in range(K):
    v, c = map(int, read().split())
    heappush(q, (c, v))


def run():
    prefer = 0
    ans = []  # 마신 맥주 도수
    while q:
        c, v = heappop(q)
        heappush(ans, (v, c))
        prefer += v
        if len(ans) == N:
            if prefer >= M:
                return c
            else:
                v, c = heappop(ans)
                prefer -= v
    return -1

print(run())
