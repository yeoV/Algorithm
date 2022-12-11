from collections import deque
import sys
read = sys.stdin.readline

H, W = map(int, read().split())
graph = [list(map(str, read().strip())) for _ in range(H)]
vector = ((1, 0), (-1, 0), (0, 1), (0, -1))
res = 1e9

def bfs(sx, sy, svalue, is_change):
    change = is_change
    q = deque([(sx,sy,svalue)])
    visited = [[False for _ in range(W)] for _ in range(H)]
    visited[sx][sy] = True
    while q:
        x, y, value = q.popleft()
        for dx, dy in vector:
            nx = x + dx
            ny = y + dy
            if sx <= nx < sx+8 and sy <= ny < sy+8:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    if graph[nx][ny] == value:
                        change += 1
                        nxt_value = 'W' if value == 'B' else 'B'
                        q.append((nx, ny, nxt_value))
                    q.append((nx, ny, graph[nx][ny]))
    return change

for sx in range(0,H-7):
    for sy in range(0,W-7):
        res = min(res, bfs(sx, sy, graph[sx][sy], 0))
        if graph[sx][sy] == "W":
            res = min(res, bfs(sx, sy, "B", 1))
        else:
            res = min(res, bfs(sx, sy, "W", 1))

print(res)