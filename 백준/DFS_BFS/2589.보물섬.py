# https://www.acmicpc.net/problem/2589
import sys
from collections import deque
read = sys.stdin.readline
N, M = map(int, read().rstrip().split(" "))   # 행 , 열
graph, result = [], []
vector = ((-1, 0), (1, 0), (0, 1), (0, -1))  # 상 하 좌 우
for _ in range(N):
    graph.append(list(read().rstrip()))


def bfs(graph, location):
    res = 0
    isvisited = [[0] * M for _ in range(N)]
    isvisited[location[0]][location[1]] = 1
    queue = deque([location])
    while queue:
        row, col = queue.popleft()
        for x, y in vector:
            dx = row + x
            dy = col + y
            if 0 <= dx < N and 0 <= dy < M:
                if graph[dx][dy] == 'L':
                    if isvisited[dx][dy] == 0:
                        isvisited[dx][dy] = isvisited[row][col] + 1
                        res = max(res, isvisited[dx][dy])
                        queue.append((dx, dy))
            else:
                continue
    return res-1


sol = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'L':
            # print(f"i, j = {(i,j)} {bfs(graph, (i, j))}")
            sol = max(sol, bfs(graph, (i, j)))
print(sol)
