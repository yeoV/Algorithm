'''
미로 탈출하는 문제. 1은 갈 수 있는 길.
5 6
101010
111111
000001
111111
111111
결과 10
'''
from collections import deque

n, m = map(int, input().split(' '))
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
step = 1
# 상, 하, 좌, 우
dxy = [(-1, 0), (1, 0), (0, -1), (0, +1)]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 4 방향 제어해주기
        for i in range(4):
            nx = x + dxy[i][0]
            ny = y + dxy[i][1]
            # 공간 벗어난 경우
            if nx >= n or ny >= m or nx < 0 or ny < 0:
                continue
            if graph[nx][ny] == 0:
                continue
            # 처음 방문하는 경우 최단 거리 기록..
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 마지막 최단거리 반환
    return graph[n-1][m-1]


print(bfs(0, 0))
