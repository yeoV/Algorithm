import sys
read = sys.stdin.readline
N, K = map(int, input().split())
# 배낭에 넣은 물품의 무게 합이 j일 때 얻을 수 있는 최대 가치
dp = [[0] * (K+1) for _ in range(N+1)]

for thing in range(1, N+1):
    weight, val = map(int, read().split())
    for j in range(1, K+1):
        if j >= weight:
            dp[thing][j] = max(dp[thing-1][j], dp[thing-1][j-weight] + val)
        else:
            dp[thing][j] = dp[thing-1][j]
print(dp[N][K])
