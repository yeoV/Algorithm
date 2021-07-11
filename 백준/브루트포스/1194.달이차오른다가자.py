# https://www.acmicpc.net/problem/1194
import sys
from collections import deque
read = sys.stdin.readline
n, m = map(int, read().split())
moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
mazes = []
# 내가 고려해야할 상태 : x좌표, y좌표, key값
dp = [[[-1 for _ in range(m)]for _ in range(n)]
      for _ in range(1 << ord('F')-ord('A')+1)]
# print(len(dp), len(dp[0]), len(dp[0][0]))
start = 0
for i in range(n):
    tmp = list(read().rstrip())
    for j, val in enumerate(tmp):
        if val == '0':
            tmp[j] = '.'
            start = (i, j)
    mazes.append(tmp)


def bfs(start):
    ret = -1
    q = deque([])
    q.append((*start, 0, 0))
    dp[0][start[0]][start[1]] = 0
    while q:
        x, y, keys, cnt = q.popleft()
        # 방향 이동
        for (dx, dy) in moves:
            nx, ny = x + dx, y + dy
            # 범위 확인
            if 0 <= nx < n and 0 <= ny < m and dp[keys][nx][ny] == -1:
                nxt_val = mazes[nx][ny]
                # 1. 벽인지 확인
                if nxt_val == '#':
                    continue
                # 2. 키나 문인지 확인
                if nxt_val.isalpha():
                    # 문 인 경우
                    if nxt_val.isupper():
                        if keys & (1 << ord(nxt_val) - ord('A')):
                            # print(f'{keys}, {nx}, {ny}, {cnt}')
                            dp[keys][nx][ny] = cnt + 1
                            q.append((nx, ny, keys, cnt + 1))
                    # 키 인 경우 -> 대문자로 바꾸어서 비트마스킹
                    else:
                        # ! 주의할 점 : keys value는 공통으로 사용되기 때문에 변수를 따로 생성해 주어야함
                        nxt_keys = (keys | 1 << ord(
                            nxt_val.upper()) - ord('A'))
                        dp[nxt_keys][nx][ny] = cnt + 1
                        q.append((nx, ny, nxt_keys, cnt + 1))
                # 3. 그냥 . 인 경우
                elif nxt_val == '.':
                    dp[keys][nx][ny] = cnt + 1
                    q.append((nx, ny, keys, cnt + 1))
                # 4. 1인 경우
                elif nxt_val == '1':
                    ret = cnt+1
                    return ret

    return ret


print(bfs(start))
