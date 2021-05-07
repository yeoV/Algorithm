from collections import deque
import sys
read = sys.stdin.readline
N = int(input())
graph = [list(read().rstrip()) for _ in range(N)]
move = ((0, 1), (0, -1), (1, 0), (-1, 0))
visited1 = [[False] * N for _ in range(N)]
visited2 = [[False] * N for _ in range(N)]


def bfs(start, color, blind, visited):
    q = deque([])
    q.append(start)
    visited[start[0]][start[1]] = True
    while q:
        x, y = q.popleft()
        # 적록색약
        if blind and (color == 'R' or color == 'G'):
            for dxy in move:
                dx, dy = x + dxy[0], y + dxy[1]
                if 0 <= dx < N and 0 <= dy < N and (graph[dx][dy] == 'R' or graph[dx][dy] == 'G'):
                    if not visited[dx][dy]:
                        visited[dx][dy] = True
                        q.append((dx, dy))
        else:
            for dxy in move:
                dx, dy = x + dxy[0], y + dxy[1]
                if 0 <= dx < N and 0 <= dy < N and graph[dx][dy] == color:
                    if not visited[dx][dy]:
                        visited[dx][dy] = True
                        q.append((dx, dy))


normal = 0
blind = 0
for x in range(N):
    for y in range(N):
        if not visited1[x][y]:
            normal += 1
            bfs((x, y), graph[x][y], False, visited1)

for x in range(N):
    for y in range(N):
        if not visited2[x][y]:
            blind += 1
            bfs((x, y), graph[x][y], True, visited2)
print(normal, blind)
