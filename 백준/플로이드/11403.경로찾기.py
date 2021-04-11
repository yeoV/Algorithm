# https://www.acmicpc.net/problem/11403
# import sys
# read = sys.stdin.readline


# def dfs(graph, row, N):
#     for col in range(N):
#         if graph[row][col] == 1 and not isvisited[col]:
#             isvisited[col] = True
#             dfs(graph, col, N)
#     return


# N = int(input())
# graph = []
# for _ in range(N):
#     graph.append(list(map(int, read().split(" "))))
# for idx in range(N):
#     isvisited = [False] * N
#     dfs(graph, idx, N)
#     graph[idx] = list(map(int, isvisited))
# for val in graph:
#     print(*val, end=" \n")

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


# 플로이드-워셜 알고리즘
for k in range(N):  # 경로 for문이 가장 상위 단계여야 누락되지 않는다
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1
            print(f'j : {j}, i : {i}, k : {k}')

# 출력
for row in graph:
    for col in row:
        print(col, end=" ")
    print()
