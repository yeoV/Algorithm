# https://www.acmicpc.net/problem/1992
import sys

read = sys.stdin.readline
n = int(read().rstrip())
graph = [list(map(int, read().rstrip())) for _ in range(n)]
ans = ""


def quad_tree(sx, sy, n):
    global ans
    piv = graph[sx][sy]
    for i in range(sx, sx + n):
        for j in range(sy, sy + n):
            if piv != graph[i][j]:
                ans += "("
                quad_tree(sx, sy, n // 2)
                quad_tree(sx, sy + (n // 2), n // 2)
                quad_tree(sx + (n // 2), sy, n // 2)
                quad_tree(sx + (n // 2), sy + (n // 2), n // 2)
                ans += ")"
                return
    else:
        ans += "1" if piv else "0"


quad_tree(0, 0, n)
print(ans)
