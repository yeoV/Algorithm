n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
INF = int(1e9)
dp = [INF] * (k+1)
dp[0] = 0
for coin in coins:
    for i in range(coin, k+1):
        if i-coin >= 0:
            dp[i] = min(dp[i-coin] + 1, dp[i])

print(-1 if dp[-1] == INF else dp[-1])
