import sys
read = sys.stdin.readline
N = int(read().rstrip())
# dp = []
# ans = N
# # dfs로 해결 가능


# def dfs(ans, cnt):
#     if ans == 0:
#         if cnt % 2 == 0:
#             print('CY')
#         else:
#             print('SK')
#         return
#     if ans >= 3:
#         dfs(ans-3, cnt+1)
#     else:
#         dfs(ans-1, cnt+1)


# dfs(N, 0)


"""
* DP를 이용한 풀이
"""
dp = [0] * 1001
dp[1] = 1
dp[3] = 1

for i in range(4, N + 1):
    if dp[i-1] == 1 and dp[i-3] == 1:
        dp[i] = 0
    else:
        dp[i] = 1
print("SK" if dp[N] == 1 else "CY")
