# https://www.acmicpc.net/problem/5557
import sys
read = sys.stdin.readline
n = int(input())
arr = list(map(int, read().split()))
dp = [[None for _ in range(21)] for _ in range(n)]


def calc(d, res):
    if d == n-1:
        if res == arr[n-1]:
            return 1
        return 0

    if dp[d][res]:
        return dp[d][res]
    ret = 0
    # 덧셈
    if res+arr[d] <= 20:
        ret += calc(d+1, res+arr[d])
    # 뺄셈
    if res-arr[d] >= 0:
        ret += calc(d+1, res-arr[d])
    dp[d][res] = ret

    return ret


calc(0, 0)
print(dp[1][arr[0]])
"""
* 아래의 값이 오답이였던 이유 -> arr[0]의 값이 0 인 경우, 결과값이 2번 계산 됨
"""
# print(dp)
# print(dp[0][0])
