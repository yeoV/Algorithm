N = int(input())
# 홀수 일 경우
dp = [0]
if N % 2:
    print(0)
else:
    for i in range(2, N+1, 2):
        if i == 2:
            dp.append(3)
        else:
            tmp = sum(map(lambda x: x*2, dp[:-1]))
            tmp += dp[-1] * 3 + 2
            dp.append(tmp)
    print(dp[-1])
