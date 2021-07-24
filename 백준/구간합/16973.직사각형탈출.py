# https://www.acmicpc.net/problem/16973
import sys
from collections import deque

read = sys.stdin.readline
N, M = map(int, read().split())

board = [list(map(int, read().split())) for _ in range(N)]
visit = [[False] * (M + 1) for _ in range(N + 1)]
prefix = [[0] * (M + 1) for _ in range(N + 1)]
H, W, Sx, Sy, Fx, Fy = map(int, read().split())
moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

# 구간합 만들기
for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix[i][j] = (
            prefix[i - 1][j]
            + prefix[i][j - 1]
            - prefix[i - 1][j - 1]
            + board[i - 1][j - 1]
        )


def check(nx, ny):
    nx, ny = nx + H - 1, ny + W - 1
    try:
        tmp = (
            prefix[nx][ny]
            - prefix[nx - H][ny]
            - prefix[nx][ny - W]
            + prefix[nx - H][ny - W]
        )
        # print(f"tmp:{tmp}, x: {nx}, y : {ny}")
        if tmp > 0:
            return False
        return True
    except IndexError:
        return False


def bfs(sx, sy):
    q = deque([])
    q.append((0, sx, sy))
    visit[sx][sy] = True
    while q:
        # print(q)
        cnt, x, y = q.popleft()

        if (x, y) == (Fx, Fy):
            return cnt

        for dx, dy in moves:
            nx, ny, ncnt = x + dx, y + dy, cnt + 1
            if 0 < nx <= N and 0 < ny <= M:
                # 구간합 검사
                if not visit[nx][ny] and check(nx, ny):
                    visit[nx][ny] = True
                    q.append((ncnt, nx, ny))
    return -1


print(bfs(Sx, Sy))
