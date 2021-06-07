import sys
read = sys.stdin.readline
N = int(input())
target_a, target_b = map(int, input().split())
m = int(input())
graph = [[]for _ in range(N+1)]
isvisited = [False] * (N+1)
for _ in range(m):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)
ans = -1


def dfs(parent, cnt):
    global ans
    if parent == target_b:
        ans = cnt
        return

    # 자식이 있을 경우
    if graph[parent]:
        for child in graph[parent]:
            if not isvisited[child]:
                isvisited[child] = True
                dfs(child, cnt + 1)
                # isvisited[child] = False
    else:
        return


isvisited[target_a] = True
dfs(target_a, 0)
print(ans)
