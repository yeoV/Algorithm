from collections import deque
import sys
read = sys.stdin.readline
N, M = map(int, read().split())
graph = [list(map(int, read().rstrip())) for _ in range(N)]
visited = [[[0] * M for _ in range(N)] for _ in range(2)]
move = ((0, 1), (0, -1), (1, 0), (-1, 0))


def bfs(x, y):
    q = deque([])
    q.append((0, x, y))
    while q:
        wall, x, y = q.popleft()
        # 범위 검사
        if (x, y) == (N-1, M-1):
            return visited[wall][x][y] + 1
        for dx, dy in move:
            nxt_x, nxt_y = x+dx, y+dy
            if 0 <= nxt_x < N and 0 <= nxt_y < M:
                if graph[nxt_x][nxt_y] == 1:
                    # 벽 부수기
                    if wall < 1 and not visited[wall][nxt_x][nxt_y]:
                        visited[wall+1][nxt_x][nxt_y] = visited[wall][x][y] + 1
                        q.append((wall+1, nxt_x, nxt_y))

                elif not visited[wall][nxt_x][nxt_y]:
                    visited[wall][nxt_x][nxt_y] = visited[wall][x][y] + 1
                    q.append((wall, nxt_x, nxt_y))

    return -1


print(bfs(0, 0))
