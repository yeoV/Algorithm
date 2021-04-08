import sys
read = sys.stdin.readline
N, M = map(int, read().rstrip().split())
arr = list(map(int, read().rstrip().split()))
arr.sort()
isvisited = [False] * N
ans = []


def dfs(depth):
    # 기저 조건
    if depth == M:
        print(*ans)
        return

    # 분기 조건
    for i in range(N):
        if not isvisited[i]:
            isvisited[i] = True
            ans.append(arr[i])
            dfs(depth + 1)
            isvisited[i] = False
            ans.pop()


dfs(0)
