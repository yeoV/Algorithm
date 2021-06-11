import sys
from collections import deque
read = sys.stdin.readline
N, M = map(int, read().split())
hx, hy = map(int, read().split())
ex, ey = map(int, read().split())
graph = [list(map(int, read().strip().split())) for _ in range(N)]
isvisited = [[[0] * M for _ in range(N)]for _ in range(2)]
move_x = [0, -1, 0, 1]
move_y = [-1, 0, 1, 0]


def bfs(x, y):
    q = deque([(x, y, 0)])
    # 시작부분 1
    isvisited[0][x][y] = 1
    while q:
        x, y, wall = q.popleft()

        if (x, y) == (ex-1, ey-1):
            print(isvisited[wall][ex-1][ey-1] - 1)
            return

        for dx, dy in zip(move_x, move_y):
            nx, ny = dx+x, dy+y
            if 0 <= nx < N and 0 <= ny < M and isvisited[wall][nx][ny] == 0:
                if graph[nx][ny] == 0:
                    isvisited[wall][nx][ny] = isvisited[wall][x][y] + 1
                    q.append((nx, ny, wall))
                elif wall == 0 and isvisited[wall+1][nx][ny] == 0:
                    isvisited[wall+1][nx][ny] = isvisited[wall][x][y] + 1
                    q.append((nx, ny, wall+1))

    print(-1)
    return


bfs(hx-1, hy-1)
