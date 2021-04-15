import sys
read = sys.stdin.readline
N, M = map(int, read().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, read().rstrip())))
ans = 1
for x in range(N-1):
    for y in range(M-1):
        for k in range(1, N):
            tmp = graph[x][y]
            dx = x+k
            dy = y+k
            if 0 <= dx < N and 0 <= dy < M:
                if tmp == graph[dx][dy]:
                    if tmp == graph[dx][y] and tmp == graph[x][dy]:
                        ans = max(ans, (k+1)**2)
print(ans)
