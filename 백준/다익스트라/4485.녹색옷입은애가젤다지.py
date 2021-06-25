# https://www.acmicpc.net/problem/4485
import sys
from heapq import heappush, heappop
read = sys.stdin.readline

moves = ((0, 1), (1, 0), (-1, 0), (0, -1))


def do(n, graph, visit):
    q = []
    heappush(q, (graph[0][0], 0, 0))
    # TODO start  지점 방문처리
    visit[0][0] = graph[0][0]
    while q:
        w, x, y = heappop(q)

        if w > visit[x][y]:
            continue

        # 4개 방향
        for move in moves:
            dx, dy = x + move[0], y + move[1]
            if 0 <= dx < n and 0 <= dy < n:
                cost = graph[dx][dy] + w
                if visit[dx][dy] > cost:
                    visit[dx][dy] = cost
                    heappush(q, (cost, dx, dy))


idx = 1
while n := int(read().rstrip()):
    graph = [list(map(int, read().split())) for _ in range(n)]
    visit = [[float('inf') for _ in range(n)] for _ in range(n)]
    do(n, graph, visit)
    print(f"Problem {idx}: {visit[n-1][n-1]}")
    idx += 1
