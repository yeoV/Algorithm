# https://www.acmicpc.net/problem/2748
n = int(input())
dp = [-1 for _ in range(91)]


def run(n):
    if n < 1:
        return 0
    if n < 2:
        return 1
    ret = 0
    if dp[n] != -1:
        return dp[n]
    ret = run(n-2) + run(n-1)
    dp[n] = ret
    return ret


print(run(n))
