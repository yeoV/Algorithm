# https://www.acmicpc.net/problem/11779
import sys
from heapq import heappush, heappop

read = sys.stdin.readline
N = int(read().rstrip())
M = int(read().rstrip())

nodes = [[] for _ in range(N + 1)]
dist = [float("inf")] * (N + 1)
path = [0] * (N + 1)
for _ in range(M):
    a, b, c = map(int, read().split())
    nodes[a].append((b, c))


def run(start):
    q = []
    heappush(q, (0, start))
    dist[start] = 0
    while q:
        cost, node = heappop(q)
        if dist[node] < cost:
            continue

        for nxt_node, c in nodes[node]:
            nxt_cost = cost + c
            if dist[nxt_node] > nxt_cost:
                dist[nxt_node] = nxt_cost
                heappush(q, (nxt_cost, nxt_node))
                path[nxt_node] = node


start, target = map(int, read().split())
run(start)
ans_path = [target]
prev = path[target]
while prev != 0:
    ans_path.append(prev)
    prev = path[prev]
print(dist[target])
print(len(ans_path))
print(*ans_path[::-1], sep=" ")
