# https://www.acmicpc.net/problem/2325
import sys
from heapq import heappop, heappush
from collections import deque

read = sys.stdin.readline
n, m = map(int, read().split())
nodes = [[] for _ in range(n + 1)]
path = [-1] * (n + 1)
for _ in range(m):
    a, b, c = map(int, read().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))


def run(start, broken_road):
    dist = [float('inf')] * (n + 1)
    q = []
    dist[start] = 0
    heappush(q, (0, start))
    while q:
        cost, node = heappop(q)

        if dist[node] < cost:
            continue

        for nxt_n, c in nodes[node]:
            nxt_c = cost + c
            if len(broken_road & {node, nxt_n}) == 2:
                continue
            if dist[nxt_n] > nxt_c:
                dist[nxt_n] = nxt_c
                heappush(q, (nxt_c, nxt_n))
                path[nxt_n] = node
    return dist[n]


run(1, set())
now = n
ans = 0
while path[now] != -1:
    broken_road = {now, path[now]}
    now = path[now]
    ans = max(ans, run(1, broken_road))
print(ans)
