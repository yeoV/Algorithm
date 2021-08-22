# https://www.acmicpc.net/problem/10217
import sys

read = sys.stdin.readline
T = int(read().rstrip())

for _ in range(T):
    n, m, k = map(int, read().split())
    nodes = [[] for _ in range(n + 1)]
    dist = [[float("inf") for _ in range(m + 1)] for _ in range(n + 1)]
    for _ in range(k):
        u, v, c, d = map(int, read().split())
        # u,v : 출발과 도착 도시, c : 비용, d : 소요시간
        nodes[u].append((v, c, d))

    dist[1][0] = 0
    for cost in range(m + 1):
        for node in range(n + 1):
            if dist[node][cost] == float("inf"):
                continue
            time = dist[node][cost]
            for nxt_n, c, t in nodes[node]:
                nxt_cost = cost + c
                nxt_time = time + t
                if nxt_cost > m:
                    continue
                dist[nxt_n][nxt_cost] = min(dist[nxt_n][nxt_cost], nxt_time)
    ans = min(dist[n])
    print(ans if ans != float("inf") else "Poor KCM")
