# https://www.acmicpc.net/problem/14503
import sys
from collections import deque

read = sys.stdin.readline

r, c = map(int, read().split())
sx, sy, h = map(int, read().split())

graph = [list(map(int, read().split())) for _ in range(r)]

moves = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
n = len(moves)
q = deque([(sx, sy, h)])
graph[sx][sy] = 2
ans = 1
while q:
    # 1번 조건
    x, y, h = q.popleft()
    for _ in range(4):
        h = ((h + n) - 1) % n
        nx, ny = x + moves[h][0], y + moves[h][1]
        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == 0:
            graph[nx][ny] = 2
            ans += 1
            q.append((nx, ny, h))
            break
    # 4방향 모두 청소된 경우
    else:
        # 뒤 방햑ㅇ
        nxt_h = ((h + n) - 2) % n
        bx, by = x + moves[nxt_h][0], y + moves[nxt_h][1]
        if not graph[bx][by] == 1:
            q.append((bx, by, h))
            continue

print(ans)

