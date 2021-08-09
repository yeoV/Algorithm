from heapq import heappush, heappop
import sys
read = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    a, b, c = map(int, read().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
# print(graph)


def network_connect(start):
    total_w = 0
    q = []
    heappush(q, start)

    while q:
        w, node = heappop(q)
        # 이미 방문한 노드라면 pass
        # 연결된 노드의 정보가 있다면
        if not visited[node] and graph[node]:
            visited[node] = True
            total_w += w
            for info in graph[node]:
                nxt_node, nxt_w = info
                if not visited[nxt_node]:
                    visited[nxt_node]
                    heappush(q, (nxt_w, nxt_node))
        else:
            continue

    return total_w


print(network_connect((0, 1)))
