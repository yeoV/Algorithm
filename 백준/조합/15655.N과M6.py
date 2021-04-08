import sys
read = sys.stdin.readline
N, M = map(int, read().rstrip().split())
arr = list(map(int, read().rstrip().split()))
arr.sort()
ans = []


def dfs(depth, now):
    # 탈출 조건
    if depth == M:
        print(*ans)
        return

    for i in range(now, N):
        ans.append(arr[i])
        dfs(depth+1, i+1)
        ans.pop()


dfs(0, 0)
