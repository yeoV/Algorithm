# https://www.acmicpc.net/problem/7579
import sys

read = sys.stdin.readline

n, m = map(int, read().split())
apps = list(map(int, read().split()))
times = list(map(int, read().split()))
apps = list(zip(apps, times))
dp = [[0 for _ in range(sum(times) + 1)] for _ in range(n + 1)]
ans = sum(times)

for row in range(1, n + 1):
    mem, time = apps[row - 1]

    for col in range(sum(times) + 1):
        if time > col:
            dp[row][col] = dp[row - 1][col]
        else:
            dp[row][col] = max(dp[row - 1][col], dp[row - 1][col - time] + mem)

        if dp[row][col] >= m:
            ans = min(ans, col)

# print(dp)
print(ans)
