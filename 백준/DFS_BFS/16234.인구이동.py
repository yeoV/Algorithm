# https://www.acmicpc.net/problem/16234
import sys
from collections import deque

read = sys.stdin.readline
moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

N, L, R = map(int, read().split())
arr = [list(map(int, read().split())) for _ in range(N)]


total = 0
cnt = 1
ans = 0


def bfs(start_x, start_y, start_v):
    global total, cnt, ans
    q = deque([(start_x, start_y, start_v)])
    group = [(start_x, start_y)]
    while q:
        x, y, v = q.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                if L <= abs(v - arr[nx][ny]) <= R:
                    visit[nx][ny] = True
                    total += arr[nx][ny]
                    cnt += 1
                    group.append((nx, ny))
                    q.append((nx, ny, arr[nx][ny]))
    if len(group) > 1:
        while group:
            x, y = group.pop()
            arr[x][y] = total // cnt
        return True
    else:
        return False


while True:
    can_group = False
    visit = [[False for _ in range(N)] for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if not visit[x][y]:
                visit[x][y] = True
                total, cnt = arr[x][y], 1
                check = bfs(x, y, arr[x][y])
                if check:
                    can_group = True
                # print(x, y, arr[x][y])
    if not can_group:
        break
    ans += 1

print(ans)
