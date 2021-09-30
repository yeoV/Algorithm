# https://www.acmicpc.net/problem/9370
import sys
from heapq import heappop, heappush

read = sys.stdin.readline
T = int(read().rstrip())


def find_path(start):
    q = []
    dist = [int(1e9) for _ in range(n + 1)]
    heappush(q, (0, start))
    dist[start] = 0

    while q:
        cost, node = heappop(q)

        if cost > dist[node]:
            continue
        for nxt_n, c in graph[node]:
            nxt_c = cost + c
            if dist[nxt_n] > nxt_c:
                dist[nxt_n] = nxt_c
                heappush(q, (nxt_c, nxt_n))
    return dist


for _ in range(T):
    n, m, t = map(int, read().split())
    s, g, h = map(int, read().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, read().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    _s = find_path(s)
    _g = find_path(g)
    _h = find_path(h)
    ans = []
    for _ in range(t):
        target = int(read().rstrip())
        if (
            _s[g] + _g[h] + _h[target] == _s[target]
            or _s[h] + _h[g] + _g[target] == _s[target]
        ):
            ans.append(target)
    print(*sorted(ans))
