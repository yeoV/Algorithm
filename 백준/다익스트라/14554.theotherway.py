# https://www.acmicpc.net/problem/

import sys
from heapq import heappush, heappop

read = sys.stdin.readline
N, M, S, E = map(int, read().split())
nodes = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, read().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))

dist = [float('inf') for _ in range(N + 1)]
counts = [0] * (N+1)

def run(start, end):
    q = []
    heappush(q, (0, start))
    dist[start] = 0
    counts[start] = 1
    while q:
        cost, node = heappop(q)

        if dist[node] < cost:
            continue
        for nxt_node, c in nodes[node]:
            nxt_cost = cost + c
            if dist[nxt_node] > nxt_cost:
                counts[nxt_node] = counts[node]
                dist[nxt_node] = nxt_cost
                heappush(q, (nxt_cost, nxt_node))
            elif dist[nxt_node] == nxt_cost:
                counts[nxt_node] = (counts[node] + counts[nxt_node]) % 1000000009

run(S, E)
print(counts[E])
