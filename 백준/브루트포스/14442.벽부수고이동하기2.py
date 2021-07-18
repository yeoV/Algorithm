# https://www.acmicpc.net/problem/14442
import sys
from collections import deque

read = sys.stdin.readline
n, m, k = map(int, read().split())
graph = [list(map(int, read().rstrip())) for _ in range(n)]
moves = ((0, 1), (0, -1), (1, 0), (-1, 0))


def bfs(start):
    q = deque([(start[0], start[1], 0)])
    visit = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]
    visit[0][0][0] = 1
    while q:
        x, y, wall = q.popleft()
        # 마지막에 도달했을 경우
        if (x, y) == (n - 1, m - 1):
            return visit[wall][x][y]
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                if not visit[wall][nx][ny]:
                    # 벽이 아닐 결우
                    if graph[nx][ny] == 0:
                        visit[wall][nx][ny] = visit[wall][x][y] + 1
                        q.append((nx, ny, wall))
                    # 벽인 경우
                    else:
                        if wall < k:
                            visit[wall + 1][nx][ny] = visit[wall][x][y] + 1
                            q.append((nx, ny, wall + 1))
    return -1

print(bfs((0, 0, 0)))
