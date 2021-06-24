# from itertools import permutations
# N, M = map(int, input().split())
# arr = [i for i in range(1, N+1)]
# for val in list(permutations(arr, M)):
#     print(*val)

# N, M = map(int, input().split())
N, M = 4, 2
arr = ['1', '2', '3', '4']
# arr = [i for i in range(1, N+1)]
isvisited = [False] * N


def dfs(depth, ex_str):

    # 탈출조건
    if depth == M:
        print(ex_str, sep=" ")
        return

    for i in range(N):
        if not isvisited[i]:
            isvisited[i] = True
            dfs(depth+1, ex_str + arr[i])
            isvisited[i] = False


dfs(0, '')
