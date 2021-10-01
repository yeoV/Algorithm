from heapq import heappop, heappush


def solution(N, road, K):
    if N < 2:
        return 0
    INF = int(1e9)
    dis = [INF] * (N+1)
    graph = [[] for _ in range(N+1)]
    for val in road:
        a, b, w = val
        graph[a].append((b, w))
        graph[b].append((a, w))

    def dijkstra(graph, dis):
        q = []
        heappush(q, (0, 1))
        dis[1] = 0
        while q:
            w, node = heappop(q)
            if w > dis[node]:
                continue

            if graph[node]:
                for nxt_val in graph[node]:
                    nxt_node, nxt_w = nxt_val
                    cost = nxt_w + w
                    if cost < dis[nxt_node]:
                        dis[nxt_node] = cost
                        heappush(q, (cost, nxt_node))
    dijkstra(graph, dis)
    # print(dis)
    # print(len(list(filter(lambda x: x <= K, dis[1:]))))
    return len(list(filter(lambda x: x <= K, dis[1:])))


solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
             [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)
solution(1, [[1, 1, 0]], 3)
# solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
#          3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4)
