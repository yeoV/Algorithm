import sys
import heapq
read = sys.stdin.readline

INF = int(1e9)
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N+1)
# isvisited = [False] * (N+1)

for _ in range(M):
    a, b, c = map(int, read().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # isvisited[start] = True
    # q가 존재하면
    while q:
        dist, now = heapq.heappop(q)
        # isvisited[now] = True
        if dist > distance[now]:
            continue

        for j in graph[now]:
            # if isvisited[j[0]]:
            #     continue
            cost = dist + j[1]
            if distance[j[0]] > cost:
                print(now, dist)
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))


start, end = map(int, input().split())
dijkstra(start)
print(distance[end])
