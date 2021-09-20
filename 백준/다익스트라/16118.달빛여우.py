# https://www.acmicpc.net/problem/16118
import sys
from heapq import heappop, heappush

read = sys.stdin.readline
n, m = map(int, read().split())
nodes = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, read().split())
    nodes[a].append((b, c * 2))
    nodes[b].append((a, c * 2))


def get_fox(start):
    q = []
    dist = [float("inf")] * (n + 1)
    dist[1] = 0
    heappush(q, (0, start))
    while q:
        cost, node = heappop(q)

        if dist[node] < cost:
            continue
        for nxt_n, c in nodes[node]:
            nxt_c = cost + c
            if dist[nxt_n] > nxt_c:
                dist[nxt_n] = nxt_c
                heappush(q, (nxt_c, nxt_n))
    return dist


def get_wolf(start):
    q = [(0, 1, 1)]
    # cnt 1 은 느리게 갔을 경우, 0은 빠르게 갔을 경우
    dist = [[float("inf")] * 2 for _ in range(n + 1)]
    dist[1][1] = 0
    while q:
        cost, node, cnt = heappop(q)
        if dist[node][cnt] < cost:
            continue

        for nxt_n, c in nodes[node]:
            nxt_c = cost + (c // 2 if cnt else c * 2)
            nxt_cnt = 1 - cnt
            if dist[nxt_n][nxt_cnt] > nxt_c:
                dist[nxt_n][nxt_cnt] = nxt_c
                heappush(q, (nxt_c, nxt_n, nxt_cnt))
    return dist


ans = 0
fox = get_fox(1)
wolf = get_wolf(1)
for f, w in zip(fox, wolf):
    if f < min(w):
        ans += 1
print(ans)
