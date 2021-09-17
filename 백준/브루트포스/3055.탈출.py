# https://www.acmicpc.net/problem/3055
import sys
from collections import deque
read = sys.stdin.readline
r, c = map(int, read().split())
# row, col 주의
visit = [[False for _ in range(c)] for _ in range(r)]
moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
forest = []
waterQ = deque()
# q에 넣어줄 값 -> x, y, day
q = deque()

for i in range(r):
    forest.append(list(read().rstrip()))
    for j, val in enumerate(forest[i]):
        if val == '*':
            waterQ.append((i, j, 0))
            visit[i][j] = True
        elif val == 'S':
            q.append((i, j, 0))
            visit[i][j] = True


def spread_water(day):
    while waterQ and waterQ[0][2] <= day:
        x, y, w = waterQ.popleft()
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if not visit[nx][ny] and forest[nx][ny] == '.':
                    waterQ.append((nx, ny, day+1))
                    visit[nx][ny] = True


def bfs():
    water_day = -1
    while q:
        x, y, day = q.popleft()
        if water_day < day:
            spread_water(day)
            water_day = day
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                if not visit[nx][ny] and forest[nx][ny] == '.':
                    q.append((nx, ny, day+1))
                    visit[nx][ny] = True
                if forest[nx][ny] == 'D':
                    return day + 1
    return -1


res = bfs()
print(res if res != -1 else 'KAKTUS')
