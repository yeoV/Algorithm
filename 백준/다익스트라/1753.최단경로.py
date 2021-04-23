
import heapq
import sys
read = sys.stdin.readline
INF = int(1e9)
# 노드 개수, 간선의 개수 입력
n, m = map(int, read().split())
start = int(input())
graph = [[] for i in range(n+1)]
isvisited = [False] * (n+1)
distance = [INF] * (n+1)

for _ in range(m):
    a, b, c = map(int, read().split())
    graph[a].append((b, c))


def dijkstra(start):
    # 시작 노드 구성
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        dis, node = heapq.heappop(heap)
        # 이미 거친 노드라면 반영 x
        if dis > distance[node]:
            continue
        # 그래프의 값을 반복
        for j in graph[node]:
            # 해당 노드를 거쳐갈 경우의 값
            cost = j[1] + dis
            # 만약 최소의 값일 경우 업데이트
            if distance[j[0]] > cost:
                distance[j[0]] = cost
                # 현재 가장 가까운 노드를 저장하기 위한 목적
                heapq.heappush(heap, (cost, j[0]))


dijkstra(start)
for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
        continue
    print(distance[i])
