# https://www.acmicpc.net/problem/1854
import sys
from heapq import heappush, heappop
from collections import defaultdict

read = sys.stdin.readline
n, m, k = map(int, read().split())
INF = float("inf")
nodes = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, read().split())
    nodes[a].append((b, c))


def run(start):
    dist = [[INF] * (k) for _ in range(n + 1)]
    q = []
    dist[start][0] = 0
    heappush(q, (0, start))
    while q:
        cost, node = heappop(q)
        # if dist[cnt][node] > cost:
        # continue
        for nxt_n, c in nodes[node]:
            nxt_c = cost + c
            # k번째로 작은 값과 비교
            if dist[nxt_n][k - 1] > nxt_c:
                dist[nxt_n][k - 1] = nxt_c
                heappush(q, (nxt_c, nxt_n))
                # 각 node의 거리값들을 정렬, 혹은 - 를 붙여 heap이용
                dist[nxt_n].sort()
    return dist


dist = run(1)
for val in dist[1:]:
    print(val[k - 1] if val[k - 1] != INF else -1)
