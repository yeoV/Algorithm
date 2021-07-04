# https://www.acmicpc.net/problem/2342
import sys
read = sys.stdin.readline
sys.setrecursionlimit(1000005)
target = list(map(int, read().split()))[:-1]
n = len(target)
dp = [[[-1 for _ in range(5)] for _ in range(5)] for _ in range(n+1)]


def calc_weight(now, target):
    if now == 0:
        return 2
    elif abs(now - target) == 2:
        return 4
    else:
        return 3


def ddr(d, left, right):
    # print(d, left, right)

    if dp[d][left][right] != -1:
        return dp[d][left][right]
    if d == len(target):
        return 0
    if d != 0 and left == right:
        return 0
    ret = float('inf')
    # 왼발과 동일할 경우
    if target[d] == left:
        ret = min(ret, ddr(d+1, target[d], right) + 1)
    # 오른발과 동일할 경우
    elif target[d] == right:
        ret = min(ret, ddr(d+1, left, target[d]) + 1)
    else:
        # 왼발로 갈 경우 거리
        ret = min(ret, ddr(d+1, target[d], right) +
                  calc_weight(left, target[d]))
        # 오른발로 갈경우 거리
        ret = min(
            ret, ddr(d+1, left, target[d])
            + calc_weight(right, target[d]))

    dp[d][left][right] = ret
    return ret


print(ddr(0, 0, 0))
