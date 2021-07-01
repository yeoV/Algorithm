# https://www.acmicpc.net/problem/14588
import sys
read = sys.stdin.readline

n = int(read().rstrip())
lines = [list(map(int, read().split())) for _ in range(n)]
graph = [[float('inf') for _ in range(n)] for _ in range(n)]

# 겹치는 부분 확인
for i, (x, y) in enumerate(lines):
    for j, (nx, ny) in enumerate(lines[i:], start=i):
        if not (i == j or y < nx or x > ny):
            graph[i][j] = 1
            graph[j][i] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

Q = int(read().rstrip())
for _ in range(Q):
    a, b = map(int, read().split())
    print(graph[a-1][b-1] if not graph[a-1][b-1] == float('inf') else -1)
