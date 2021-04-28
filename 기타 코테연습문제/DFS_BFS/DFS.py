def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:  # 방문하지 않아  false 인 경우
            visited[i] = True
            dfs(graph, i, visited)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
# 방문 확인 리스트, 노드갯수 + 1
visited = [False] * 9
dfs(graph, 1, visited)
