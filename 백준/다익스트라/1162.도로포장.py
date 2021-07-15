# https://www.acmicpc.net/problem/1162
import sys
from heapq import heappop, heappush
read = sys.stdin.readline
n, m, k = map(int, read().split())
dist = [[float('inf') for i in range(n+1)] for _ in range(k+1)]
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, read().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def go(start):
    q = []
    heappush(q, (0, start, 0))
    dist[0][start] = 0
    while q:
        # load는 포장한 도로의 수
        w, node, load = heappop(q)
        if w > dist[load][node]:
            continue

        for (nxt_node, nxt_cost) in graph[node]:
            cost = w + nxt_cost
            if dist[load][nxt_node] > cost:
                dist[load][nxt_node] = cost
                heappush(q, (cost, nxt_node, load))
            # 도로 포장
            if load < k and dist[load+1][nxt_node] > w:
                dist[load+1][nxt_node] = w
                heappush(q, (w, nxt_node, load+1))


go(1)
res = float('inf')
for d in dist:
    res = min(res, d[n])
print(res)
