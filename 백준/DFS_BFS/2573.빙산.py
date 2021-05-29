import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10**6)
read = sys.stdin.readline
N, M = map(int, read().split())
move = ((0, -1), (-1, 0), (1, 0), (0, 1))
iceberg = [list(map(int, read().split())) for _ in range(N)]

# 빙산이 2개로 쪼개져 있는지 확인


def is_iceberg(x, y, sea_info, visited):
    q = deque([(x, y)])
    visited[x][y] = True

    while q:

        x, y = q.popleft()
        for dxy in move:
            nxt_x, nxt_y = x+dxy[0], y+dxy[1]
            # 범위 검사
            if 0 <= nxt_x < N and 0 <= nxt_y < M:
                if not visited[nxt_x][nxt_y]:
                    if iceberg[nxt_x][nxt_y] > 0:
                        visited[nxt_x][nxt_y] = True
                        q.append((nxt_x, nxt_y))
                    else:
                        sea_info[(x, y)] += 1


sea_info = defaultdict(int)
year = 0
while True:
    # 빙하 녹이기
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if iceberg[i][j] > 0 and not visited[i][j]:
                if cnt > 0:
                    print(year)
                    exit()
                cnt += 1
                is_iceberg(i, j, sea_info, visited)
                # 2덩이로 분리 되었다면
    year += 1
    for key, val in sea_info.items():
        iceberg[key[0]][key[1]] -= val
    sea_info.clear()

    if cnt == 0:
        print(0)
        break
