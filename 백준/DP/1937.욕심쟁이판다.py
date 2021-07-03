# https://www.acmicpc.net/problem/1937
import sys
sys.setrecursionlimit(10 ** 6)
read = sys.stdin.readline
n = int(read().rstrip())
moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
graph = [list(map(int, read().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]


def go(x, y):
    # 0인 경우도 반환해주어야 함
    if dp[x][y] != -1:
        return dp[x][y]

    ret = 0
    for move in moves:
        dx, dy = x + move[0], y + move[1]
        if 0 <= dx < n and 0 <= dy < n:
            if graph[dx][dy] > graph[x][y]:
                ret = max(ret, go(dx, dy) + 1)
    dp[x][y] = ret
    return ret


res = 0
for i in range(n):
    for j in range(n):
        res = max(res, go(i, j))
print(res + 1)