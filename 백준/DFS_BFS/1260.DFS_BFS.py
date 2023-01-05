# https://www.acmicpc.net/problem/1260
import sys
from collections import deque, defaultdict
from heapq import heappush

read = sys.stdin.readline

N, M, V = map(int, read().split())
graph = defaultdict(list)
res = [[V] for _ in range(2)]  # 0 : dfs, 1 : bfs
for _ in range(M):
    s, e = map(int, read().split())
    # heappush(graph[s], e)
    # heappush(graph[e], s)
    graph[e].append(s)
    graph[s].append(e)

for k, v in graph.items():
    v.sort()


def bfs(start):
    q = deque([start])
    bfs_visited = [False for _ in range(N + 1)]
    bfs_visited[start] = True
    while q:
        node = q.popleft()
        for nxt_node in graph[node]:
            if not bfs_visited[nxt_node]:
                bfs_visited[nxt_node] = True
                res[1].append(nxt_node)
                q.append(nxt_node)


visited = [False for _ in range(N + 1)]
visited[V] = True


def dfs(node):
    # 탈출조건
    if not graph[node]:
        return

    for nxt_node in graph[node]:
        if not visited[nxt_node]:
            visited[nxt_node] = True
            res[0].append(nxt_node)
            dfs(nxt_node)


bfs(V)
dfs(V)

for val in res:
    print(*val, sep=" ")
