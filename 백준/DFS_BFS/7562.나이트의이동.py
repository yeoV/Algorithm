from collections import deque
total = int(input())
move_x = (-1, -2, -2, -1, 1, 2, 2, 1)
move_y = (-2, -1, 1, 2, 2, 1, -1, -2)


def bfs(x, y, target, N):
    isvisited = [[False]*N for _ in range(N)]
    q = deque([(x, y, 0)])
    while q:
        now_x, now_y, cnt = q.popleft()
        if target == (now_x, now_y):
            return cnt
        for i, j in zip(move_x, move_y):
            dx = now_x + i
            dy = now_y + j
            if 0 <= dx < N and 0 <= dy < N and not isvisited[dx][dy]:
                q.append((dx, dy, cnt+1))
                isvisited[dx][dy] = True
            else:
                continue


for _ in range(total):
    N = int(input())
    x, y = map(int, input().split())
    end = tuple(map(int, input().split()))
    print(bfs(x, y, end, N))
