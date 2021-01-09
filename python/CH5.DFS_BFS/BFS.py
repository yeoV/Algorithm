'''
큐 자료구조를 이용하여 구현한다.
'''
from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])

    # 큐가 빌 때까지 반복
    while queue:
        # 맨 왼쪽의 요소 제거,
        v = queue.popleft()
        print(v, end=' ')

        # 방문하지 않은 노드일 경우 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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

visited = [False] * 9
bfs(graph, 1, visited)
