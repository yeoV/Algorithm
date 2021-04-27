import sys
read = sys.stdin.readline
n, k = map(int, read().split())
coins = [int(read().rstrip()) for _ in range(n)]
dp = [0] * (k+1)
dp[0] = 1
for coin in coins:
    for i in range(coin, k+1):
        if i - coin >= 0:
            dp[i] += dp[i-coin]
print(dp[-1])
