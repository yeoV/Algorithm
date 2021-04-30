N = int(input())
dp = []

for i in range(N):
    if i == 0:
        dp.append(1)
    elif i == 1:
        dp.append(3)
    else:
        dp.append(dp[i-1] + 2 * dp[i-2])
print(dp[-1] % 10007)
