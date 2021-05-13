import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline
n, m = map(int, read().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node):
    if graph[node]:
        for nxt in graph[node]:
            if not visited[nxt]:
                visited[nxt] = True
                dfs(nxt)
    else:
        return


ans = 0
for i in range(1, n+1):
    if not visited[i]:
        ans += 1
        visited[i] = True
        dfs(i)
print(ans)
