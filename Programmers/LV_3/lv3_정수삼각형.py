# https://programmers.co.kr/learn/courses/30/lessons/43105


def solution(triangle):
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    dp[0][0] = triangle[0][0]
    for row in range(1, n):
        for col in range(len(triangle[row])):
            if col == 0:
                dp[row][col] = dp[row - 1][col] + triangle[row][col]
            else:
                dp[row][col] = max(
                    dp[row - 1][col - 1] + triangle[row][col],
                    dp[row - 1][col] + triangle[row][col],
                )
    print(max(dp[n - 1]))
    return max(dp[n - 1])


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
