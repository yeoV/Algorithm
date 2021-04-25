# 그래프의 방향을 바꾸는 아주 기똥찬 풀이..

from heapq import heappush, heappop
import sys
read = sys.stdin.readline

N, M, X = map(int, input().split())
INF = int(1e9)
go_graph = [[] for _ in range(N+1)]
back_graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, read().split())
    go_graph[b].append((a, c))
    back_graph[a].append((b, c))


def dijkstra(graph, start) -> list:
    q = []
    distance = [INF] * (N+1)
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        w, now = heappop(q)

        if w > distance[now]:
            continue

        for j in graph[now]:
            cost = j[1] + distance[now]
            if distance[j[0]] > cost:
                distance[j[0]] = cost
                heappush(q, (cost, j[0]))
    return distance


go = dijkstra(graph=go_graph, start=X)
back = dijkstra(graph=back_graph, start=X)
res = [i+j for i, j in zip(go[1:], back[1:])]
print(max(res))
