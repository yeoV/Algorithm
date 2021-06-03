from heapq import heappush, heappop
import sys
read = sys.stdin.readline
N, M = map(int, read().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
for _ in range(M):
    a, b, w = map(int, read().split())
    graph[a].append((b, w))
    graph[b].append((a, w))


def connect_city(start):
    total_w = 0
    max_w = 0
    q = []
    heappush(q, start)

    while q:
        w, node = heappop(q)
        if not visited[node] and graph[node]:
            total_w += w
            max_w = max(max_w, w)
            visited[node] = True
            for info in graph[node]:
                nxt_node, nxt_w = info
                if not visited[nxt_node]:
                    heappush(q, (nxt_w,  nxt_node))

    return total_w - max_w


print(connect_city((0, 1)))
