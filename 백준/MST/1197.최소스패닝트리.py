from heapq import heappush, heappop
import sys
read = sys.stdin.readline

V, E = map(int, read().split())
graph = [[] for _ in range(V+1)]
visited = [False] * (V+1)
for _ in range(E):
    a, b, c = map(int, read().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

# print(graph)


def spanning_tree(start):
    total_w = 0
    q = []
    # visited[start[1]] = True
    heappush(q, start)
    # print(q)
    while q:
        weight, node = heappop(q)

        if not visited[node] and graph[node]:
            visited[node] = True
            total_w += weight
            for nxt_node_info in graph[node]:
                nxt_node, nxt_w = nxt_node_info
                if not visited[nxt_node]:
                    heappush(q, (nxt_w, nxt_node))
    return total_w


print(spanning_tree((0, 1)))
