import sys
read = sys.stdin.readline

N, M = map(int, read().split())
arr = list(map(int, read().split()))
arr.sort()
tmp = []
ans = set()


def dfs(depth, now):
    if depth == M:
        ans.add(tuple(tmp))
        return

    for i in range(now, N):
        tmp.append(arr[i])
        dfs(depth+1, i)
        tmp.pop()


dfs(0, 0)
for val in sorted(list(ans)):
    print(*val, sep=' ')
