# https://www.acmicpc.net/problem/1884
import sys
from heapq import heappop, heappush

read = sys.stdin.readline
k = int(read().rstrip())
n = int(read().rstrip())
r = int(read().rstrip())
cities = [[] for _ in range(n + 1)]
# 노드와 비용에 따른 거리 비용 담는 배열
dist = [[float('inf') for _ in range(k+1)] for _ in range(n + 1)]

for _ in range(r):
    s, d, l, t = map(int, read().split())
    cities[s].append((d, l, t))

# print(cities)


def go(l, t):
    q = []
    dist[1][0] = 0
    heappush(q, (l, t, 1))
    while q:
        # 최단 거리를 기준으로
        load, cost, node = heappop(q)
        if load > dist[node][cost]:
            continue

        for nxt_node, nxt_l, nxt_t in cities[node]:
            nxt_cost, nxt_load = cost + nxt_t, load + nxt_l

            if nxt_cost <= k:
                if dist[nxt_node][nxt_cost] > nxt_load:
                    dist[nxt_node][nxt_cost] = nxt_load
                    heappush(q, (nxt_load, nxt_cost, nxt_node))


go(0, 0)
print(min(dist[n]))