# https://www.acmicpc.net/problem/3109
import sys

read = sys.stdin.readline

R, C = map(int, read().split())
graph = [list(read().rstrip()) for _ in range(R)]
# 최대한 우상향 방향으로 이동해야함
moves = ((-1, 1), (0, 1), (1, 1))
visit = [[False] * C for _ in range(R)]
piv_row = 0
answer = 0


def run(x, y):
    if y == (C - 1):
        return 1
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == ".":
            if not visit[nx][ny]:
                visit[nx][ny] = True
                # 최종 마지막 노드에 방문했을경우
                if run(nx, ny):
                    return 1
    return 0


ans = 0
for row in range(R):
    visit[row][0] = True
    if run(row, 0):
        ans += 1
print(ans)
