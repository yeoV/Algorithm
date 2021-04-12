import sys
read = sys.stdin.readline
N, M = map(int, read().split())
arr = list(map(int, read().split()))
arr.sort()
tmp = list()
ans = set()


def dfs(depth, now):
    # 탈출 조건
    if depth == M:
        ans.add(tuple(tmp))
        return

    # 반복 조건
    for i in range(now, N):
        tmp.append(arr[i])
        dfs(depth+1, i+1)
        tmp.pop()


dfs(0, 0)
for val in sorted(list(ans)):
    print(*val, sep=' ')
