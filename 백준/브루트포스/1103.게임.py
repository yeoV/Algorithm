# https://www.acmicpc.net/problem/1103
import sys
read = sys.stdin.readline
n, m = map(int, read().split())
board = [[int(i) if i != 'H' else
          -1 for i in read().rstrip()] for _ in range(n)]
moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
dp = [[-1 for _ in range(m)] for _ in range(n)]
visit = [[False] * m for _ in range(n)]
visit[0][0] = True
res = 0


def dfs(x, y, cnt):
    global res
    res = max(res, cnt)
    dp[x][y] = max(dp[x][y], cnt)

    X = board[x][y]
    for dxy in moves:
        nx, ny = x + dxy[0] * X, y + dxy[1] * X
        if 0 <= nx < n and 0 <= ny < m:
            # 무한으로 겹치는 것이 있는 경우
            if visit[nx][ny]:
                print(-1)
                exit()
            # if not dp가 아닌 이유 : 이미 들어있는 값보다 더 큰값일 수 도 있음
            if dp[nx][ny] < cnt + 1 and board[nx][ny] != -1:
                visit[nx][ny] = True
                dfs(nx, ny, cnt+1)
                visit[nx][ny] = False


dfs(0, 0, 1)
print(res)
