# https://www.acmicpc.net/problem/17070
import sys

read = sys.stdin.readline
n = int(read().rstrip())
house = [list(map(int, read().split())) for _ in range(n)]
# 3 가지 상태 0 : 가로 1 : 세로 2 : 대각선
# dir = {"hor": 0, "ver": 1, "dia": 2}
# dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(3)]
ans = 0


def run(x, y, state):
    global ans
    if (x, y) == (n - 1, n - 1):
        ans += 1
        return
    # if dp[state][x][y]:
    #     return dp[state][x][y]
    if state == 0 or state == 2:
        if y + 1 < n and house[x][y + 1] != 1:
            run(x, y + 1, 0)

    if state == 1 or state == 2:
        if x + 1 < n and house[x + 1][y] != 1:
            run(x + 1, y, 1)

    if state == 0 or state == 1 or state == 2:
        if x + 1 < n and y + 1 < n:
            if (
                house[x][y + 1] != 1
                and house[x + 1][y] != 1
                and house[x + 1][y + 1] != 1
            ):
                run(x + 1, y + 1, 2)

    # dp[state][x][y] = ret
    # return ret


run(0, 1, 0)
print(ans)
# print(dp[0][0][1])
