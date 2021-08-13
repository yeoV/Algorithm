# https://www.acmicpc.net/problem/11952
import sys
from heapq import heappush, heappop

read = sys.stdin.readline
N, M, K, S = map(int, read().split())
p, q = map(int, read().split())
cities = [[] for _ in range(N + 1)]
zombies = set()
# 좀비에게 점령당한 도시
for _ in range(K):
    zombies.add(int(read().rstrip()))
# 도시 연결 정보
for _ in range(M):
    a, b = map(int, read().split())
    cities[a].append(b)
    cities[b].append(a)

# 각 도시별 cost 정의하기
danger_dist = [float("inf")] * (N + 1)
distance = [float("inf")] * (N + 1)


# 감염 지역과의 거리를 계산하는 함수
def check_safety(start):
    queue = []
    heappush(queue, (0, start))
    danger_dist[start] = 0
    while queue:
        cost, node = heappop(queue)
        if danger_dist[node] < cost:
            continue

        nxt_cost = cost + 1
        for nxt_node in cities[node]:
            if danger_dist[nxt_node] > nxt_cost:
                danger_dist[nxt_node] = nxt_cost
                heappush(queue, (nxt_cost, nxt_node))


for zombie in zombies:
    check_safety(zombie)


def run(start):
    queue = []
    heappush(queue, (0, start))
    distance[start] = 0
    while queue:
        cost, node = heappop(queue)
        if distance[node] < cost:
            continue
        for nxt_node in cities[node]:
            if nxt_node == N:
                nxt_cost = cost
            else:
                nxt_cost = cost + (p if danger_dist[nxt_node] > S else q)
            if not (nxt_node in zombies):
                if distance[nxt_node] > nxt_cost:
                    distance[nxt_node] = nxt_cost
                    heappush(queue, (nxt_cost, nxt_node))


run(1)
print(distance[N])
