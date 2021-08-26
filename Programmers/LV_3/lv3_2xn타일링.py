def solution(n):
    dp = [1, 2]
    for i in range(2, n):
        tmp = (dp[i - 2] + dp[i - 1]) % 1000000007
        dp.append(tmp)
    print(dp[n - 1])
    return dp[n - 1]


solution(4)
