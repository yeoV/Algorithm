from collections import deque
from itertools import combinations
import sys
import copy
read = sys.stdin.readline
N, M = map(int, input().split())
move_x = [-1, 0, 1, 0]
move_y = [0, 1, 0, -1]

board = []
clean_list = []
virus_list = []
for _ in range(N):
    board.append(list(map(int, read().split())))
for x in range(N):
    for y in range(M):
        if board[x][y] == 0:
            # 벽을 세울 0의 위치
            clean_list.append((x, y))
        elif board[x][y] == 2:
            # 바이러스의 위치 표시
            virus_list.append((x, y))
        # 2번의 위치도 표시
clean_list = combinations(clean_list, 3)
print(list(clean_list))


def spread_virus(x, y, isvisited) -> int:
    cnt = 0
    q = deque([(x, y)])
    while q:
        now_x, now_y = q.popleft()

        for i, j in zip(move_x, move_y):
            dx = now_x + i
            dy = now_y + j
            if 0 <= dx < N and 0 <= dy < M and isvisited[dx][dy] == 0:
                q.append((dx, dy))
                cnt += 1
                isvisited[dx][dy] = -1
            else:
                continue
    return cnt


answer = []
ans = 0
for clean in clean_list:
    res = 0
    isvisited = copy.deepcopy(board)
    for x, y in clean:
        isvisited[x][y] = 1
    for i, j in virus_list:
        res += spread_virus(i, j, isvisited)
    ans = max(ans, sum(list(map(lambda x: x.count(0), isvisited))))
print(ans)
