# https://www.acmicpc.net/problem/3197
import sys
from collections import deque

read = sys.stdin.readline
swan = []
moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
R, C = map(int, read().split())
arr = [list(read().rstrip()) for _ in range(R)]
water_visit = [[False for _ in range(C)] for _ in range(R)]
swan_visit = [[False for _ in range(C)] for _ in range(R)]

# water를 위한 큐와 백조를 위한 큐 2개 생성
water_q1, water_q2 = deque(), deque()
swan_q1, swan_q2 = deque(), deque()
# swan 도착지
ex, ey = 0, 0

# water 정보 담기, 주의 : 백조를 물로 바꿔주어야 함
for x in range(R):
    for y in range(C):
        if arr[x][y] == "L":
            if not swan_q1:
                swan_q1.append((x, y))
                swan_visit[x][y] = True
            else:
                ex, ey = x, y
            arr[x][y] = "."
        if arr[x][y] == ".":
            water_visit[x][y] = True
            water_q1.append((x, y))


def water() -> None:
    while water_q1:
        x, y = water_q1.popleft()

        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not water_visit[nx][ny]:
                water_visit[nx][ny] = True
                if arr[nx][ny] == ".":
                    water_q1.append((nx, ny))
                elif arr[nx][ny] == "X":
                    arr[nx][ny] = "."
                    water_q2.append((nx, ny))
    return


def swan() -> bool:
    while swan_q1:
        x, y = swan_q1.popleft()
        if (x, y) == (ex, ey):
            return True
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx < R and 0 <= ny < C and not swan_visit[nx][ny]:
                swan_visit[nx][ny] = True
                if arr[nx][ny] == ".":
                    swan_q1.append((nx, ny))
                elif arr[nx][ny] == "X":
                    swan_q2.append((nx, ny))
    return False


ans = 0
while True:
    if swan():
        break
    water()
    ans += 1
    water_q1 = water_q2
    swan_q1 = swan_q2
    water_q2 = deque()
    swan_q2 = deque()
print(ans)
