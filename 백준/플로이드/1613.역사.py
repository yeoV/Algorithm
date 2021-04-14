import sys
read = sys.stdin.readline
n, k = map(int, read().split())
graph = [[0] * (n) for _ in range(n)]
for _ in range(k):
    a, b = map(int, read().split())
    graph[a-1][b-1] = -1
    graph[b-1][a-1] = 1
s = int(read().rstrip())
for k in range(n):
    for i in range(n):
        for j in range(n):
            if not graph[i][j]:
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    graph[j][i] = 1
                elif graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1

for _ in range(s):
    a, b = map(int, read().split())
    print(graph[a-1][b-1])
