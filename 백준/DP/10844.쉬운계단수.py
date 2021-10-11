import sys
read = sys.stdin.readline
N = int(input())
MOD = 1000000000
dp = [[0] * 10 for _ in range(N)]
for i in range(1, 10):
    dp[0][i] = 1

if N == 1:
    print(sum(dp[0]))
else:
    for i in range(1, N):
        for j in range(10):
            if j == 0:
                dp[i][j] = dp[i-1][1]
            elif j == 9:
                dp[i][j] = dp[i-1][8]
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    print(sum(dp[N-1]) % MOD)
