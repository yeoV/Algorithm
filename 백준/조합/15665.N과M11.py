import sys
read = sys.stdin.readline

N, M = map(int, read().split())
arr = list(map(int, read().split()))
arr.sort()
tmp = list()
ans = set()


def dfs(depth):
    if depth == M:
        ans.add(tuple(tmp))
        return

    for i in range(N):
        tmp.append(arr[i])
        dfs(depth+1)
        tmp.pop()


dfs(0)
for val in sorted(list(ans)):
    print(*val, sep=' ')
