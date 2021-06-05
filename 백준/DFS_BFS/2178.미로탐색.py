import sys
from collections import deque
read = sys.stdin.readline
N, M = map(int, input().split())
move_x = [0, -1, 0, 1]
move_y = [1, 0, -1, 0]
arr = [list(map(int, read().rstrip())) for _ in range(N)]
isvisited = [[0] * M for _ in range(N)]
ans = 1e9


def bfs(start):
    q = deque([start])
    # 시작점
    isvisited[0][0] = 1
    while q:
        x, y = q.popleft()
        if (x, y) == (N-1, M-1):
            return
        for vec in zip(move_x, move_y):
            dx = x + vec[0]
            dy = y + vec[1]
            if 0 <= dx < N and 0 <= dy < M:
                if isvisited[dx][dy] == 0 and arr[dx][dy] == 1:
                    isvisited[dx][dy] = isvisited[x][y] + 1
                    q.append((dx, dy))


bfs((0, 0))
print(isvisited[N-1][M-1])
