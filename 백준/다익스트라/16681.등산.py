# https://www.acmicpc.net/problem/16681
import sys
from heapq import heappush, heappop

read = sys.stdin.readline

N, M, D, E = map(int, read().split())
# 높이과 노드의 정보
graph = [[] for _ in range(N + 1)]
heights = [0] + list(map(int, read().split()))

for _ in range(M):
    a, b, n = map(int, read().split())
    graph[a].append((b, n))
    graph[b].append((a, n))


def run(start):
    dist = [float("inf") for _ in range(N + 1)]
    q = []
    dist[start] = 0
    heappush(q, (0, start))
    while q:
        cost, node = heappop(q)

        if dist[node] < cost:
            continue

        for nxt_node, c in graph[node]:
            nxt_cost = cost + c
            if heights[nxt_node] > heights[node]:
                if dist[nxt_node] > nxt_cost:
                    dist[nxt_node] = nxt_cost
                    heappush(q, (nxt_cost, nxt_node))
    return dist


go = run(1)
back = run(N)
ans = -float("inf")
for idx, val in enumerate(map(sum, zip(go[1:], back[1:]))):
    if val != float("inf"):
        ans = max(ans, (heights[idx + 1] * E) - (val * D))

print(ans if ans != -float("inf") else "Impossible")
