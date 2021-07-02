# https://www.acmicpc.net/problem/15681
import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.readline
n, r, q = map(int, read().split())
graph = [[] for _ in range(n+1)]
dp = [None] * (n+1)
for _ in range(n-1):
    a, b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)
visit = [False] * (n+1)


def count_subtree(node):
    # 탈출 조건
    visit[node] = True
    if dp[node]:
        return dp[node]
    ret = 1
    for nxt_node in graph[node]:
        if not visit[nxt_node]:
            ret += count_subtree(nxt_node)
    dp[node] = ret
    return ret


count_subtree(r)
# print(dp)
for _ in range(q):
    num = int(read().rstrip())
    print(dp[num])
