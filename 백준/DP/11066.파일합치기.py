# https://www.acmicpc.net/problem/11066
import sys
read = sys.stdin.readline
T = int(read().rstrip())


def do(start, end):
    # 탈출 조건 인덱스가 하나일 경우
    if dp[start][end]:
        return dp[start][end]

    if start == end:
        return 0

    ret = float('inf')

    tmp = prefix[end+1] - prefix[start]
    for mid in range(start, end):
        ret = min(ret, do(start, mid) + do(mid+1, end) + tmp)
    dp[start][end] = ret
    return ret


for _ in range(T):
    k = int(read().rstrip())
    pages = list(map(int, read().split()))
    dp = [[None for _ in range(k+1)] for _ in range(k+1)]
    prefix = [0]
    e = 0
    for val in pages:
        e += val
        prefix.append(e)
    # print(prefix)

    print(do(0, k-1))
