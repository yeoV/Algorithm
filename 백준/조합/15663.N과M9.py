import sys
read = sys.stdin.readline
N, M = map(int, read().split())
arr = list(map(int, read().rstrip().split()))
# arr.sort()
answers = set()
ans = []
isvisited = [False] * N


def dfs(depth):
    # 탈출 조건
    if depth == M:
        answers.add(tuple(ans))
        return

    for i in range(N):
        if not isvisited[i]:
            isvisited[i] = True
            ans.append(arr[i])
            dfs(depth+1)
            isvisited[i] = False
            ans.pop()


dfs(0)
for val in sorted(list(answers)):
    print(*val)
