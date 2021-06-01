# https://www.acmicpc.net/problem/17208
import sys
read = sys.stdin.readline
n, m, k = map(int, read().split())
orders = [list(map(int, read().split())) for _ in range(n)]
dp = [[[0 for _ in range(k+1)] for _ in range(m + 1)] for _ in range(n + 1)]
# print(dp)
# print(orders)


def cell(d, burger, fries):

    if d == n:
        return 0

    if dp[d][burger][fries]:
        return dp[d][burger][fries]
    ret = 0
    # 주문 처리 안함
    ret = cell(d+1, burger, fries)

    # 주문 처리 함
    if burger-orders[d][0] >= 0 and fries-orders[d][1] >= 0:
        # print(burger-orders[d][0], fries-orders[d][1])
        ret = max(ret, cell(d+1, burger-orders[d][0], fries-orders[d][1]) + 1)
    dp[d][burger][fries] = ret

    return ret


ans = cell(0, m, k)
print(ans)
