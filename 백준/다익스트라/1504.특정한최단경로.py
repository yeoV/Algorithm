# https://www.acmicpc.net/problem/1504
import sys
from heapq import heappush, heappop

read = sys.stdin.readline
n, e = map(int, read().split())
nodes = [[] for _ in range(n + 1)]
for _ in range(e):
    a, b, c = map(int, read().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))
first, second = map(int, read().split())


def run(start, end):
    q = []
    dist = [float('inf')] * (n + 1)
    heappush(q, (0, start))
    dist[start] = 0

    while q:
        cost, node = heappop(q)
        if dist[node] < cost:
            continue
        for nxt_n, c in nodes[node]:
            nxt_cost = cost + c
            if dist[nxt_n] > nxt_cost:
                dist[nxt_n] = nxt_cost
                heappush(q, (nxt_cost, nxt_n))
    return dist[end]


ans = 0
ans = run(1, first) + run(first, second) + run(second, n)
ans = min(ans, run(1, second) + run(second, first) + run(first, n))
print(ans if ans != float('inf') else -1)