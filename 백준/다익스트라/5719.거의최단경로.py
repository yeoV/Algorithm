# https://www.acmicpc.net/problem/5719
import sys
from heapq import heappush, heappop
from collections import deque, defaultdict

read = sys.stdin.readline


def find_first_path(start, end):
    q = []
    first_path = [[-1] for _ in range(n)]
    dist = [float('inf') for _ in range(n)]
    dist[start] = 0
    heappush(q, (0, start))
    while q:
        cost, node = heappop(q)

        if dist[node] < cost:
            continue

        for nxt_n, c in nodes[node].items():
            nxt_c = cost + c
            if dist[nxt_n] > nxt_c:
                dist[nxt_n] = nxt_c
                heappush(q, (nxt_c, nxt_n))
                first_path[nxt_n] = [node]
            elif dist[nxt_n] == nxt_c:
                first_path[nxt_n].append(node)
    return first_path, dist


def remove_path(r_graph,dist, end):
    queue = deque([end])
    while queue:
        node = queue.popleft()

        for nxt_n in r_graph[node]:
            if nxt_n in first_path[node]:
                try:
                    del nodes[nxt_n][node]
                except KeyError:
                    continue
                queue.append(nxt_n)
            # if dist[nxt_n] + nodes[nxt_n][node] == dist[node]:
            #     del nodes[nxt_n][node]
            #     print(nodes)
            #     queue.append(nxt_n)


while True:
    n, m = map(int, read().split())

    if (n, m) == (0, 0):
        break
    s, d = map(int, read().split())
    nodes = [defaultdict(int) for _ in range(n)]
    reverse_nodes = [[] for _ in range(n)]
    for _ in range(m):
        u, v, p = map(int, read().split())
        nodes[u][v] = p
        reverse_nodes[v].append(u)

    first_path, dist = find_first_path(s, d)
    remove_path(reverse_nodes,dist, d)
    _, ans = find_first_path(s, d)
    print(ans[d] if ans[d] != float('inf') else -1)
