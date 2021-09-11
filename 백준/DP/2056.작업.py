# https://www.acmicpc.net/problem/2056
import sys
read = sys.stdin.readline
N = int(read().rstrip())
ans = 0
dp = [0] * (N + 1)
for idx in range(1, N+1):
    val = list(map(int, read().split()))
    cost = val[0]
    if val[1] > 0:
        for prev in val[2:]:
            dp[idx] = max(dp[idx], cost + dp[prev])
    else:
        dp[idx] = val[0]
    ans = max(ans, dp[idx])
print(ans)
