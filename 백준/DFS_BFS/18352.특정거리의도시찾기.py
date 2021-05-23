from collections import deque
import sys
read = sys.stdin.readline
N, M, K, X = map(int, read().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N+1)
ans = []
for _ in range(M):
    a, b = map(int, read().split())
    graph[a].append(b)


def bfs(start):
    visited[start] = True
    q = deque([(start, 0)])
    while q:
        # K를 벗어나는 경우
        node, dis = q.popleft()
        if dis == K:
            ans.append(node)
        if dis > K:
            return
        if graph[node]:
            for nxt_node in graph[node]:
                if not visited[nxt_node]:
                    visited[nxt_node] = True
                    q.append((nxt_node, dis+1))


bfs(X)
if ans:
    ans.sort()
    print(*ans, sep='\n')
else:
    print(-1)
