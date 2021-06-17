"""
https://www.acmicpc.net/problem/11049
"""
import sys
read = sys.stdin.readline
N = int(read().rstrip())
matrics = [tuple(map(int, read().split())) for _ in range(N)]
dp = [[None for _ in range(N)] for _ in range(N)]


def calc(start, end):
    if start == end:
        return 0
    if dp[start][end]:
        return dp[start][end]
    ret = 1e9
    mat_mul = 0
    for mid in range(start, end):
        # 호엥
        mat_mul = matrics[start][0] * matrics[mid][1] * matrics[end][1]
        ret = min(ret, calc(start, mid) + calc(mid+1, end) + mat_mul)
    dp[start][end] = ret
    return ret


print(calc(0, N-1))
