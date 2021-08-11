# https://www.acmicpc.net/problem/2096
import sys

read = sys.stdin.readline
n = int(read().rstrip())
max_dp = list(map(int, read().split()))
min_dp = max_dp[:]

for _ in range(n - 1):
    a, b, c = map(int, read().split())
    max_dp = [
        max(max_dp[:2]) + a,
        max(max_dp[:]) + b,
        max(max_dp[1:]) + c,
    ]
    min_dp = [
        min(min_dp[:2]) + a,
        min(min_dp[:]) + b,
        min(min_dp[1:]) + c,
    ]
print(max(max_dp), min(min_dp))
