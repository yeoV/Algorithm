from collections import deque
import sys
read = sys.stdin.readline
# M 이 세로, N 이 가로
M, N, K = map(int, read().split())
graph = [[0] * N for _ in range(M)]
rec = []
for _ in range(K):
    y1, x1, y2, x2 = map(int, read().split())
    rec.append((x1, y1, x2, y2))
for val in rec:
    x1, y1, x2, y2 = val
    for i in range(x1, x2):
        for j in range(y1, y2):
            graph[i][j] = -1

move = ((0, -1), (0, 1), (1, 0), (-1, 0))


def bfs(start):
    area = 1
    q = deque([])
    q.append(start)
    graph[start[0]][start[1]] = 1
    while q:
        x, y = q.popleft()

        for dxy in move:
            dx, dy = x+dxy[0], y+dxy[1]
            if 0 <= dx < M and 0 <= dy < N:
                if not graph[dx][dy]:
                    area += 1
                    graph[dx][dy] = graph[x][y] + 1
                    q.append((dx, dy))
    return area


ans = list()
for i in range(M):
    for j in range(N):
        if not graph[i][j]:
            ans.append(bfs((i, j)))
print(len(ans))
print(*sorted(ans))
