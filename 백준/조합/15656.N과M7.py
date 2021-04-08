import sys
read = sys.stdin.readline
N, M = map(int, read().rstrip().split())
arr = list(map(int, read().split()))
arr.sort()
ans = []


def dfs(depth):
    # 탈출 조건
    if depth == M:
        print(*ans)
        return

    # 조건 분기
    for i in range(N):
        ans.append(arr[i])
        dfs(depth+1)
        ans.pop()


dfs(0)
