# from heapq import heappush, heappop
# import sys

# read = sys.stdin.readline
# INF = int(1e9)
# M, N = map(int, read().split())
# maze = [(list(map(int, read().rstrip()))) for _ in range(N)]
# distance = [[INF] * M for _ in range(N)]
# vec_x, vec_y = [0, 0, -1, 1], [-1, 1, 0, 0]


# def dijkstra():
#     q = []
#     heappush(q, [0, 0, 0])
#     distance[0][0] = 0
#     while q:
#         w, x, y = heappop(q)
#         # 마지막 부분 탈출
#         if x == N-1 and y == M-1:
#             print(w)
#         # distnace 값 더 작은값인 경우 넘기기
#         if distance[x][y] < w:
#             continue
#         for a, b in zip(vec_x, vec_y):
#             dx = x + a
#             dy = y + b
#             if 0 <= dx < N and 0 <= dy < M:
#                 cost = w + maze[dx][dy]
#                 if distance[dx][dy] > cost:
#                     distance[dx][dy] = cost
#                     heappush(q, [distance[dx][dy], dx, dy])
#                     # print(distance)


# dijkstra()

'''
알고스팟 2번째 버전
'''
import sys
from collections import deque


read = sys.stdin.readline
INF = int(1e9)
M, N = map(int, read().split())
maze = [(list(map(int, read().rstrip()))) for _ in range(N)]
isvisited = [[False] * M for _ in range(N)]
distance = [[0] * M for _ in range(N)]
vec_x, vec_y = [0, 0, -1, 1], [-1, 1, 0, 0]


def bfs(maze):
    q = deque([(0, 0)])
    while q:
        x, y = q.popleft()
        if x == N-1 and y == M-1:
            print(distance[x][y])
            break
        for a, b in zip(vec_x, vec_y):
            dx = x + a
            dy = y + b

            if 0 <= dx < N and 0 <= dy < M:
                if not isvisited[dx][dy]:
                    isvisited[dx][dy] = True
                    if maze[dx][dy] == 1:
                        distance[dx][dy] = distance[x][y] + 1
                        q.append((dx, dy))
                    else:
                        distance[dx][dy] = distance[x][y]
                        q.appendleft((dx, dy))


bfs(maze)
