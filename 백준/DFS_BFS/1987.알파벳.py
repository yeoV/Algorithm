import sys
read = sys.stdin.readline
R, C = map(int, read().split())
graph = [list(read().rstrip()) for _ in range(R)]
move = ((0, 1), (0, -1), (1, 0), (-1, 0))
ans = 1


def bfs(start_x, start_y, alphabet):
    global ans
    q = set([(start_x, start_y, alphabet)])
    while q:
        x, y, alpha = q.pop()
        ans = max(ans, len(alpha))
        for dxy in move:
            dx, dy = x + dxy[0], y + dxy[1]

            if 0 <= dx < R and 0 <= dy < C and graph[dx][dy] not in alpha:
                q.add((dx, dy, alpha + graph[dx][dy]))
            else:
                continue

bfs(0, 0, graph[0][0])
print(ans)
