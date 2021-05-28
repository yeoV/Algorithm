import sys
read = sys.stdin.readline
A = int(read().rstrip())
lst = list(map(int, read().split()))


def find(lst):
    dp = [1] * A
    for i in range(1, A):
        for j in range(i):
            if lst[i] > lst[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return dp


dp1 = find(lst)
dp2 = find(lst[::-1])
print(max([sum(i) for i in zip(dp1, dp2[::-1])])-1)
