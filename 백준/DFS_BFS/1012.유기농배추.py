# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(10**9)


def dfs(graph, row, col, size):
    M, N = size
    dx, dy = 0, 0
    if 0 <= row < M and 0 <= col < N:
        if graph[row][col] == 1:
            graph[row][col] = 0
            for vec in vector:
                dx = row + vec[0]
                dy = col + vec[1]
                dfs(graph, dx, dy, size)
            return True
        else:
            return False
    else:
        return False


T = int(input())
vector = ((1, 0), (-1, 0), (0, 1), (0, -1))
res = []
for _ in range(T):
    count = 0
    M, N, K = map(int, input().split(" "))  # 가로, 세로, 갯수
    graph = [[0]*N for _ in range(M)]
    for _ in range(K):
        row, col = map(int, input().split(" "))
        graph[row][col] = 1
    for x in range(M):
        for y in range(N):
            if graph[x][y] == 1:
                if dfs(graph, x, y, (M, N)):
                    count += 1
    res.append(count)
print(*res, sep='\n')
