"""
! 한번더 의미를 상기해보기
"""
# https://www.acmicpc.net/problem/4811

import sys
read = sys.stdin.readline
# 메모이제이션 할 변수 -> 함수의 매개변수 차원만큼 생성, N은 30개 까지
dp = [[[None for _ in range(61)] for _ in range(31)] for _ in range(61)]
# print(len(dp), len(dp[0]), len(dp[0][0]))


def run(d, w_cnt, h_cnt):
    if dp[d][w_cnt][h_cnt]:
        return dp[d][w_cnt][h_cnt]

    if d == 2*N:
        return 1

    ret = 0
    # 알약 1개가 존재하는 경우
    if w_cnt > 0:
        ret += run(d+1, w_cnt - 1, h_cnt + 1)

    # 알약 0.5개가 존재하는 경우
    if h_cnt > 0:
        ret += run(d+1, w_cnt, h_cnt - 1)

    dp[d][w_cnt][h_cnt] = ret
    return ret


while (N := int(read().rstrip())):
    print(run(0, N, 0))
