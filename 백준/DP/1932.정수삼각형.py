import sys

read = sys.stdin.readline
N = int(input())
graph = [list(map(int, read().split())) for _ in range(N)]
graph = [[0]] + graph
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(0, N):
        if j < len(graph[i]):
            dp[i][j + 1] = max(
                dp[i - 1][j + 1] + graph[i][j], dp[i - 1][j] + graph[i][j]
            )
        else:
            break
print(dp)
print(max(dp[-1]))
