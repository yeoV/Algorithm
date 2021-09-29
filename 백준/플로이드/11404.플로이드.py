# https://www.acmicpc.net/problem/11404
import sys

read = sys.stdin.readline

n = int(read().rstrip())
m = int(read().rstrip())
graph = [[float("inf") for _ in range(n)] for _ in range(n)]

for _ in range(m):
    i, j, c = map(int, read().split())
    graph[i - 1][j - 1] = min(graph[i - 1][j - 1], c)


for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(n):
    for j in range(n):
        print(graph[i][j] if graph[i][j] != float("inf") else 0, end=" ")
    print()
