import sys
read = sys.stdin.readline
N, M = map(int, input().split())
INF = int(1e9)
graph = [[INF if i != j else 0 for i in range(N+1)] for j in range(N+1)]
for idx in range(M):
    a, b = map(int, read().split())
    graph[a][b] = 1
    graph[b][a] = 1
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
ans_list = list()
ans_val = INF
for val in graph[1:]:
    tmp = sum(filter(lambda x: x is not INF, val))
    ans_list.append(tmp)
    ans_val = min(ans_val, tmp)
print(ans_list.index(ans_val) + 1)
