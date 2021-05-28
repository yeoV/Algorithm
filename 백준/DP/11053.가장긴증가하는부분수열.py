import bisect
import sys
read = sys.stdin.readline
A = int(read().rstrip())
lst = list(map(int, read().split()))
# dp = [1] * len(lst)
# for i in range(1, len(lst)):
#     for j in range(i):
#         if lst[i] > lst[j]:
#             dp[i] = max(dp[i], dp[j]+1)
# print(max(dp))

"""
이분탐색을 이용한 LIS 풀이
-> nlogn 의 시간 복잡도를 가짐
"""

dp = [lst[0]]

for i in range(A):
    if lst[i] > dp[-1]:
        dp.append(lst[i])
    else:
        idx = bisect.bisect_left(dp, lst[i])
        dp[idx] = lst[i]

print(len(dp))
