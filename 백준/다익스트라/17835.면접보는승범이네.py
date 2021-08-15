# https://www.acmicpc.net/problem/17835
import sys
from heapq import heappop, heappush

read = sys.stdin.readline
N, M, K = map(int, read().split())
nodes = [[] for _ in range(N + 1)]
# 간선 정보 입력
for _ in range(M):
    u, v, c = map(int, read().split())
    # 모든 노드로부터 x 까지의 거리를
    nodes[v].append((u, c))
company = list(map(int, read().split()))
distance = [float("inf")] * (N + 1)
q = []
for val in company:
    distance[val] = 0
    q.append((0, val))


def run():
    while q:
        cost, node = heappop(q)
        if distance[node] < cost:
            continue

        for nxt_n, c in nodes[node]:
            nxt_cost = cost + c
            if distance[nxt_n] > nxt_cost:
                distance[nxt_n] = nxt_cost
                heappush(q, (nxt_cost, nxt_n))


ans = [0, 0]
run()
for idx, val in enumerate(distance[1:], start=1):
    if ans[1] < val:
        ans[1] = val
        ans[0] = idx
print(*ans, sep="\n")
