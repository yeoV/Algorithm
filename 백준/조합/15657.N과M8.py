import sys
read = sys.stdin.readline
N, M = map(int, read().split())
arr = list(map(int, read().rstrip().split()))
arr.sort()
ans = []


def dfs(depth, now):
    # 탈출 조건
    if depth == M:
        print(*ans)
        return

    # 조건 분기
    for i in range(now, N):
        ans.append(arr[i])
        dfs(depth+1, i)
        ans.pop()


dfs(0, 0)
