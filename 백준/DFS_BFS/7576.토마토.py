from collections import deque
import sys
read = sys.stdin.readline
M, N = map(int, input().split())
move_x = [0, -1, 0, 1]
move_y = [-1, 0, 1, 0]
graph = [list(map(int, read().split())) for _ in range(N)]
tomato = deque()
day = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            tomato.append((i, j))


def bfs():
    global day
    while tomato:
        day += 1
        '''
        여기가 핵심. 하루에 append한 토마토의 갯수 만큼 pop 해주는 것
        '''
        for _ in range(len(tomato)):
            x, y = tomato.popleft()
            for xy in zip(move_x, move_y):
                dx = x + xy[0]
                dy = y + xy[1]
                if 0 <= dx < N and 0 <= dy < M:
                    if graph[dx][dy] == 0:
                        graph[dx][dy] = -1
                        tomato.append((dx, dy))
    for val in graph:
        if 0 in val:
            return -1
    return day - 1


print(bfs())
