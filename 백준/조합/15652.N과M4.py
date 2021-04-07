import sys
read = sys.stdin.readline
N, M = map(int, read().rstrip().split())
arr = [i for i in range(1, N+1)]
ans = []


def dfs(depth, now):
    # 기저 조건
    if depth == M:
        print(*ans)
        return
    # 반복 조건
    for i in range(N):
        if arr[i] >= now:
            ans.append(arr[i])
            dfs(depth+1, arr[i])
            ans.pop()


dfs(0, 1)
