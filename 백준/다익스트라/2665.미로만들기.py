# https://www.acmicpc.net/problem/2665
import sys
from heapq import heappop, heappush

read = sys.stdin.readline
n = int(read().rstrip())
moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
graph = [list(map(int, read().rstrip())) for _ in range(n)]
visit = [[float('inf') for _ in range(n)] for _ in range(n)]


def do(sx, sy):
    q = []
    heappush(q, (0, sx, sy))
    visit[sx][sy] = 0
    while q:
        w, x, y = heappop(q)

        if (x, y) == (n - 1, n - 1):
            return visit[x][y]

        if w > visit[x][y]:
            continue

        for move in moves:
            dx, dy = x + move[0], y + move[1]
            if 0 <= dx < n and 0 <= dy < n:
                cost = w if graph[dx][dy] == 1 else w + 1
                if visit[dx][dy] > cost:
                    visit[dx][dy] = cost
                    heappush(q, (cost, dx, dy))

    return visit[n - 1][n - 1]


print(do(0, 0))
