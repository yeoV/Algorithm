import sys
read = sys.stdin.readline
N, M = map(int, read().rstrip().split())
arr = [i for i in range(1, N+1)]
isvisited = [False] * N
ans = list()


def dfs(depth, now):
    # 기저 조건
    if depth == M:
        print(*ans, sep=' ')
        return
    # 분기 조건
    # 1~4 까지 배열
    for i in range(N):
        if not isvisited[i]:
            if arr[i] >= now:
                isvisited[i] = True
                ans.append(arr[i])
                dfs(depth + 1, arr[i])
                isvisited[i] = False
                ans.pop()


dfs(0, 1)
