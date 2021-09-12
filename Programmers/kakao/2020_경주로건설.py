# https://programmers.co.kr/learn/courses/30/lessons/67259
from collections import deque

# h : 수평이동, v: 수작이동
moves = ((0, -1, 'h'), (0, 1, 'h'), (1, 0, 'v'), (-1, 0, 'v'))


def bfs(val, N, board):
    q = deque([])
    q.append(val)
    visit = [[float('inf')] * N for _ in range(N)]
    visit[0][0] = 0
    while q:
        x, y, cost, state = q.popleft()

        for dx, dy, nxt_stat in moves:
            nx, ny = x + dx, y + dy
            nxt_cost = cost + (600 if state != nxt_stat else 100)
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                if visit[nx][ny] >= nxt_cost:
                    visit[nx][ny] = nxt_cost
                    q.append((nx, ny, nxt_cost, nxt_stat))
    return visit[N - 1][N - 1]


def solution(board):
    N = len(board)
    # 수평으로 시작할 때와 수직으로 시작할때 따로 고려해주기
    ans = min(bfs((0, 0, 0, 'h'), N, board), bfs((0, 0, 0, 'v'), N, board))
    # print(ans)
    return ans

# solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]])
solution([[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1],
          [0, 0, 0, 0, 0, 0]])
