import sys
read = sys.stdin.readline
n = int(read().rstrip())
nums = list(map(int, read().split()))
dp = nums[:]
for i in range(1, n):
    dp[i] = max(dp[i], dp[i-1] + dp[i])
print(max(dp))
